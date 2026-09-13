"""
scraper_lectulandia.py
=======================

Scraper de metadatos y sinopsis para el género "Clásico" del sitio
https://ww3.lectulandia.co/genero/clasico/

Criterio de selección de la categoría: se eligió "Clásico" por la gran
cantidad de libros disponibles (~16 páginas de listado) y la variedad de
autores y títulos reconocidos mundialmente que contiene.

Objetivo de extracción: los primeros 150 libros de la categoría, en el
orden en que aparecen en el listado.

Cumple con el diseño de la práctica:
    1. Abre la categoría con Playwright (Chromium, headless configurable).
    2. Recorre las páginas de la categoría (paginación /page/N/).
    3. Obtiene el HTML renderizado con Playwright.
    4. Lo analiza con BeautifulSoup.
    5. Extrae las URLs de las fichas de los libros (primeras 150).
    6. Visita cada ficha con Playwright.
    7. Extrae metadatos y sinopsis con BeautifulSoup.
    8. Limpia y valida los datos.
    9. Elimina duplicados (por url_libro).
    10. Guarda el resultado (incremental + CSV final) con pandas.

IMPORTANTE:
    - No se descarga ningún EPUB/PDF ni contenido protegido: solo se leen
      los metadatos públicos de la ficha (título, autor/es, géneros,
      serie, sinopsis, portada opcional).
    - Se agrega una pausa aleatoria entre requests para no sobrecargar el
      servidor.
    - Los errores en libros/páginas individuales no detienen la ejecución:
      se registran en un log y se continúa con el siguiente elemento.

Requisitos:
    pip install playwright beautifulsoup4 pandas
    playwright install chromium

Uso:
    python scraper_lectulandia.py --cantidad 150
"""

from __future__ import annotations

import argparse
import csv
import logging
import random
import re
import sys
import time
from dataclasses import dataclass, fields
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
from bs4 import BeautifulSoup
from playwright.sync_api import (
    Browser,
    Page,
    TimeoutError as PlaywrightTimeoutError,
    sync_playwright,
)

# --------------------------------------------------------------------------
# Configuración general
# --------------------------------------------------------------------------

BASE_URL = "https://ww3.lectulandia.co"
CATEGORY_URL = f"{BASE_URL}/genero/clasico/"
CATEGORY_PAGE_TEMPLATE = f"{BASE_URL}/genero/clasico/page/{{n}}/"
CATEGORIA_ORIGEN = "Clásico"

OUTPUT_DIR = Path(__file__).resolve().parent
CSV_INCREMENTAL = OUTPUT_DIR / "libros_incremental.csv"
CSV_FINAL = OUTPUT_DIR / "libros.csv"
LOG_FILE = OUTPUT_DIR / "scraping.log"

# Rango de pausas (segundos) entre requests, para no saturar el servidor.
PAUSA_MIN = 1.5
PAUSA_MAX = 3.5

# Reintentos por página/ficha ante error transitorio.
MAX_REINTENTOS = 2

# Tope de elementos a recorrer hacia adelante dentro de una ficha al buscar
# autor/géneros/serie/sinopsis, como salvaguarda extra ante páginas atípicas.
TOPE_ELEMENTOS_FICHA = 300

NA = "N/D"  # valor consistente para campos ausentes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler(LOG_FILE, encoding="utf-8"), logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger("lectulandia")


# --------------------------------------------------------------------------
# Modelo de datos
# --------------------------------------------------------------------------

@dataclass
class Libro:
    titulo: str = NA
    autores: str = NA
    generos: str = NA
    serie: str = NA
    sinopsis: str = NA
    url_libro: str = NA
    categoria_origen: str = NA
    fecha_extraccion: str = NA
    imagen_portada: str = NA  # campo opcional

    def as_dict(self) -> dict:
        return {f.name: getattr(self, f.name) for f in fields(self)}


FIELDNAMES = [f.name for f in fields(Libro)]


# --------------------------------------------------------------------------
# Utilidades de limpieza
# --------------------------------------------------------------------------

def limpiar_texto(texto: str | None) -> str:
    """Quita saltos de línea, espacios repetidos y espacios al borde."""
    if not texto:
        return NA
    texto = texto.replace("\xa0", " ")
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto if texto else NA


def es_url_valida(url: str | None) -> bool:
    if not url or url == NA:
        return False
    return url.startswith("http://") or url.startswith("https://")


def pausa_aleatoria() -> None:
    time.sleep(random.uniform(PAUSA_MIN, PAUSA_MAX))


# --------------------------------------------------------------------------
# Paso 1-5: recorrer la categoría y obtener las URLs de las fichas
# --------------------------------------------------------------------------

def obtener_html(page: Page, url: str, espera_selector: str = "body") -> str | None:
    """Navega con Playwright y devuelve el HTML renderizado, con reintentos."""
    for intento in range(1, MAX_REINTENTOS + 1):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=20000)
            page.wait_for_selector(espera_selector, timeout=10000)
            return page.content()
        except PlaywrightTimeoutError:
            log.warning("Timeout cargando %s (intento %d/%d)", url, intento, MAX_REINTENTOS)
        except Exception as exc:  # noqa: BLE001 - queremos capturar cualquier error de red
            log.warning("Error cargando %s: %s (intento %d/%d)", url, exc, intento, MAX_REINTENTOS)
        pausa_aleatoria()
    log.error("No se pudo obtener el HTML de %s tras %d intentos", url, MAX_REINTENTOS)
    return None


def extraer_urls_de_pagina(html: str) -> list[str]:
    """Con BeautifulSoup, extrae las URLs de las fichas de libro de una página
    de listado de la categoría."""
    soup = BeautifulSoup(html, "html.parser")
    urls: list[str] = []

    # Cada libro del listado se representa con un <h2> que contiene el link
    # a la ficha: <h2><a href="https://.../book/slug/">Título</a></h2>
    for h2 in soup.select("h2"):
        a = h2.find("a", href=True)
        if not a:
            continue
        href = urljoin(BASE_URL, a["href"])
        if "/book/" in href:
            urls.append(href.rstrip("/") + "/")

    return urls


def recolectar_urls_categoria(page: Page, cantidad_objetivo: int, max_paginas: int) -> list[str]:
    """Recorre las páginas de la categoría, en orden, hasta juntar las
    primeras `cantidad_objetivo` URLs de fichas (o hasta agotar max_paginas)."""
    urls_vistas: list[str] = []
    urls_set: set[str] = set()

    for num_pagina in range(1, max_paginas + 1):
        url_pagina = CATEGORY_URL if num_pagina == 1 else CATEGORY_PAGE_TEMPLATE.format(n=num_pagina)
        log.info("Recorriendo página de categoría %d: %s", num_pagina, url_pagina)

        html = obtener_html(page, url_pagina, espera_selector="h2 a")
        if html is None:
            log.warning("Se omite la página %d por error de carga", num_pagina)
            continue

        nuevas = extraer_urls_de_pagina(html)
        if not nuevas:
            log.info("No se encontraron más fichas en la página %d; se detiene la paginación", num_pagina)
            break

        for u in nuevas:
            if u not in urls_set:
                urls_set.add(u)
                urls_vistas.append(u)

        log.info("Total de fichas únicas acumuladas: %d", len(urls_vistas))

        if len(urls_vistas) >= cantidad_objetivo:
            break

        pausa_aleatoria()

    # Nos quedamos con las primeras `cantidad_objetivo`, respetando el orden
    # de aparición en el listado (consigna: "los primeros N libros").
    return urls_vistas[:cantidad_objetivo]


# --------------------------------------------------------------------------
# Paso 6-7: visitar cada ficha y extraer metadatos + sinopsis
# --------------------------------------------------------------------------

def extraer_titulo(soup: BeautifulSoup) -> str:
    """Extrae el título real del libro (no el logo del sitio).

    Estrategia 1: meta og:title, que en este sitio sigue siempre el patrón
    fijo "<Título> - Epub y PDF".
    Estrategia 2 (fallback): el último <h1> de la página que no sea el
    logo del sitio ("Lectulandia"), ya que el primer <h1> de toda página
    corresponde al logo (una imagen sin texto visible).
    Estrategia 3 (fallback): la etiqueta <title> del documento.
    """
    og_title = soup.find("meta", attrs={"property": "og:title"})
    if og_title and og_title.get("content"):
        titulo = re.sub(r"\s*-\s*Epub y PDF\s*$", "", og_title["content"], flags=re.IGNORECASE)
        titulo = limpiar_texto(titulo)
        if titulo != NA:
            return titulo

    candidatos_h1 = [limpiar_texto(h.get_text()) for h in soup.find_all("h1")]
    candidatos_h1 = [t for t in candidatos_h1 if t != NA and t.lower() != "lectulandia"]
    if candidatos_h1:
        return candidatos_h1[-1]

    if soup.title and soup.title.string:
        bruto = soup.title.string
        partes = re.split(r"\s*-\s*Descargar|\s*\|\s*Lectulandia", bruto)
        if partes and limpiar_texto(partes[0]) != NA:
            return limpiar_texto(partes[0])

    return NA


def extraer_bloque_ficha(soup: BeautifulSoup) -> dict:
    """Extrae autores, géneros, serie y sinopsis de la ficha real del libro.

    La página de una ficha en Lectulandia también muestra una lista de
    "libros relacionados" ANTES de los datos del libro solicitado, cada
    uno con sus propios enlaces a /autor/ y /genero/. Por eso no alcanza
    con buscar "el primer enlace de autor" en toda la página: hay que
    ubicarse primero en el bloque de la ficha real.

    Se usa como ancla el texto literal "Autor:", que en este sitio SOLO
    aparece en la ficha propia del libro (los libros relacionados se
    listan sin ese prefijo). A partir de esa ancla se recorre hacia
    adelante, deteniéndose al llegar a la sección de comentarios, para no
    mezclar datos con contenido posterior no relacionado.
    """
    resultado = {"autores": NA, "generos": NA, "serie": NA, "sinopsis": NA}

    marcador = soup.find(string=re.compile(r"Autor:"))
    if marcador is None:
        # Fallback poco preciso, mejor que nada si cambia el maquetado.
        a_autor = soup.find("a", href=re.compile(r"/autor/"))
        if a_autor:
            resultado["autores"] = limpiar_texto(a_autor.get_text())
        return resultado

    # --- Autor/es: pueden ser uno o varios enlaces en el mismo contenedor.
    contenedor_autor = marcador.find_parent()
    autores_tags = contenedor_autor.find_all("a", href=re.compile(r"/autor/")) if contenedor_autor else []
    if not autores_tags:
        siguiente = marcador.find_next("a", href=re.compile(r"/autor/"))
        if siguiente:
            autores_tags = [siguiente]
    if autores_tags:
        nombres = [limpiar_texto(a.get_text()) for a in autores_tags]
        nombres = [n for n in nombres if n != NA]
        if nombres:
            resultado["autores"] = ", ".join(nombres)

    # --- Recorrido hacia adelante: géneros, serie y sinopsis -------------
    generos_encontrados: list[str] = []
    serie_encontrada: str | None = None
    parrafos_candidatos: list[str] = []

    marcadores_de_corte = ("coment", "registrate para participar", "esperamos que disfrutes")

    for i, el in enumerate(marcador.find_all_next()):
        if i >= TOPE_ELEMENTOS_FICHA:
            break

        nombre_tag = getattr(el, "name", None)

        if nombre_tag in ("h2", "h3"):
            texto_heading = el.get_text(strip=True).lower()
            if any(m in texto_heading for m in marcadores_de_corte):
                break

        if nombre_tag == "a" and el.get("href"):
            href = el["href"]
            if "/genero/" in href:
                nombre = limpiar_texto(el.get_text())
                if nombre != NA and nombre not in generos_encontrados:
                    generos_encontrados.append(nombre)
            elif "/serie/" in href and serie_encontrada is None:
                serie_encontrada = limpiar_texto(el.get_text())

        if nombre_tag == "p":
            texto = limpiar_texto(el.get_text())
            if texto != NA and not texto.endswith(("[…]", "[...]")):
                parrafos_candidatos.append(texto)

    if generos_encontrados:
        resultado["generos"] = ", ".join(generos_encontrados)
    if serie_encontrada:
        resultado["serie"] = serie_encontrada
    if parrafos_candidatos:
        resultado["sinopsis"] = max(parrafos_candidatos, key=len)

    return resultado


def extraer_imagen_portada(soup: BeautifulSoup) -> str:
    """Campo opcional: URL de la portada, tomada del meta og:image (la
    imagen grande de la ficha, no las miniaturas de libros relacionados)."""
    og_image = soup.find("meta", attrs={"property": "og:image"})
    if og_image and og_image.get("content"):
        return og_image["content"]
    img_grande = soup.find("img", src=re.compile(r"/big\.jpg"))
    if img_grande and img_grande.get("src"):
        return img_grande["src"]
    return NA


def extraer_datos_ficha(html: str, url_libro: str) -> Libro:
    soup = BeautifulSoup(html, "html.parser")
    libro = Libro(
        url_libro=url_libro,
        categoria_origen=CATEGORIA_ORIGEN,
        fecha_extraccion=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    libro.titulo = extraer_titulo(soup)
    libro.imagen_portada = extraer_imagen_portada(soup)

    bloque = extraer_bloque_ficha(soup)
    libro.autores = bloque["autores"]
    libro.generos = bloque["generos"]
    libro.serie = bloque["serie"]
    libro.sinopsis = bloque["sinopsis"]

    return libro


def scrapear_ficha(page: Page, url_libro: str) -> Libro | None:
    html = obtener_html(page, url_libro, espera_selector="body")
    if html is None:
        return None
    try:
        return extraer_datos_ficha(html, url_libro)
    except Exception as exc:  # noqa: BLE001
        log.error("Error parseando %s: %s", url_libro, exc)
        return None


# --------------------------------------------------------------------------
# Paso 8-9: limpieza, validación y deduplicación
# --------------------------------------------------------------------------

def libro_es_valido(libro: Libro) -> bool:
    if libro.titulo == NA or not libro.titulo.strip():
        return False
    if not es_url_valida(libro.url_libro):
        return False
    return True


# --------------------------------------------------------------------------
# Paso 10: guardado incremental y CSV final
# --------------------------------------------------------------------------

def inicializar_csv_incremental() -> None:
    with open(CSV_INCREMENTAL, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()


def guardar_incremental(libro: Libro) -> None:
    with open(CSV_INCREMENTAL, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(libro.as_dict())


def generar_csv_final() -> pd.DataFrame:
    try:
        df = pd.read_csv(CSV_INCREMENTAL, dtype=str, keep_default_na=False)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=FIELDNAMES)

    # Aseguramos que existan todas las columnas esperadas, sin importar
    # qué haya quedado escrito en el CSV incremental (evita KeyError si
    # el archivo quedó vacío o con columnas incompletas).
    df = df.reindex(columns=FIELDNAMES)
    df = df.fillna(NA)
    df = df.replace(r"^\s*$", NA, regex=True)

    # Eliminar duplicados por url_libro, conservando la primera aparición
    antes = len(df)
    df = df.drop_duplicates(subset=["url_libro"], keep="first")
    despues = len(df)
    if antes != despues:
        log.info("Se eliminaron %d registros duplicados por url_libro", antes - despues)

    # Descartar registros sin título o sin URL válida
    df = df[df["titulo"] != NA]
    df = df[df["url_libro"].apply(es_url_valida)]

    df.to_csv(CSV_FINAL, index=False, encoding="utf-8")
    return df


# --------------------------------------------------------------------------
# Controles mínimos de calidad (se ejecutan al final del proceso)
# --------------------------------------------------------------------------

def ejecutar_controles_calidad(df: pd.DataFrame, cantidad_objetivo: int) -> None:
    log.info("----- Controles mínimos de calidad -----")

    if df.empty:
        log.warning(
            "El dataset final quedó vacío. Revisar 'scraping.log' para ver "
            "si hubo errores sistemáticos de carga o de parseo por ficha."
        )
        return

    duplicados = df["url_libro"].duplicated().sum()
    log.info("Duplicados por url_libro: %d (esperado 0)", duplicados)

    sin_titulo = (df["titulo"] == NA).sum()
    log.info("Registros sin título: %d (esperado 0)", sin_titulo)

    urls_invalidas = (~df["url_libro"].apply(es_url_valida)).sum()
    log.info("URLs inválidas: %d (esperado 0)", urls_invalidas)

    con_sinopsis = (df["sinopsis"] != NA).sum()
    porcentaje_sinopsis = 100 * con_sinopsis / max(len(df), 1)
    log.info(
        "Registros con sinopsis: %d/%d (%.1f%%) (se espera mayoría)",
        con_sinopsis, len(df), porcentaje_sinopsis,
    )

    con_autor = (df["autores"] != NA).sum()
    con_generos = (df["generos"] != NA).sum()
    log.info("Registros con autor: %d/%d", con_autor, len(df))
    log.info("Registros con géneros: %d/%d", con_generos, len(df))

    total = len(df)
    log.info("Cantidad final de libros: %d (objetivo: %d)", total, cantidad_objetivo)
    if total < cantidad_objetivo:
        log.warning(
            "Se obtuvieron %d libros de los %d solicitados; algunas fichas "
            "pudieron descartarse por error de carga o datos inválidos. "
            "Ver 'scraping.log' para el detalle.",
            total, cantidad_objetivo,
        )


# --------------------------------------------------------------------------
# Orquestación principal
# --------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Scraper Lectulandia - género Clásico")
    parser.add_argument(
        "--cantidad", type=int, default=150,
        help="Cantidad de libros a extraer (los primeros N de la categoría). Default: 150",
    )
    parser.add_argument(
        "--max-paginas", type=int, default=10,
        help="Tope de páginas de categoría a recorrer para juntar las URLs (default: 10, ~24 fichas c/u)",
    )
    parser.add_argument("--headless", action="store_true", default=True, help="Ejecutar sin ventana visible (por defecto)")
    parser.add_argument("--con-ventana", dest="headless", action="store_false", help="Mostrar el navegador (debug)")
    args = parser.parse_args()

    log.info("Inicio del scraping. Objetivo: los primeros %d libros de la categoría '%s'", args.cantidad, CATEGORIA_ORIGEN)
    inicializar_csv_incremental()

    procesados: list[Libro] = []
    urls_procesadas: set[str] = set()

    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=args.headless)
        contexto = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
            )
        )
        page = contexto.new_page()

        # --- 1-5: recolectar las primeras N URLs de fichas desde la categoría
        urls_fichas = recolectar_urls_categoria(
            page, cantidad_objetivo=args.cantidad, max_paginas=args.max_paginas
        )
        log.info("URLs de fichas recolectadas: %d", len(urls_fichas))

        if not urls_fichas:
            log.error("No se pudo recolectar ninguna URL de ficha. Abortando.")
            browser.close()
            sys.exit(1)

        # --- 6-9: visitar cada ficha, extraer, limpiar, deduplicar --------
        for i, url in enumerate(urls_fichas, start=1):
            if url in urls_procesadas:
                continue  # evita duplicados antes de scrapear

            log.info("(%d/%d) Procesando ficha: %s", i, len(urls_fichas), url)
            libro = scrapear_ficha(page, url)

            if libro is None:
                log.warning("Ficha omitida por error de carga/parseo: %s", url)
                pausa_aleatoria()
                continue

            if not libro_es_valido(libro):
                log.warning("Ficha descartada por datos inválidos (sin título o URL): %s", url)
                pausa_aleatoria()
                continue

            urls_procesadas.add(url)
            procesados.append(libro)
            guardar_incremental(libro)  # guardado incremental, libro a libro
            log.info("Guardado: %s — %s", libro.titulo, libro.autores)

            pausa_aleatoria()

        browser.close()

    log.info("Scraping finalizado. Libros válidos guardados: %d", len(procesados))

    # --- 10: CSV final + controles -----------------------------------------
    df_final = generar_csv_final()
    ejecutar_controles_calidad(df_final, cantidad_objetivo=args.cantidad)
    log.info("Archivo final generado en: %s", CSV_FINAL)


if __name__ == "__main__":
    main()
