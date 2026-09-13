# Estrategia de extracción — Género "Clásico" (Lectulandia)

**Sitio y categoría elegida:** https://ww3.lectulandia.co/genero/clasico/

**Criterio de selección de la categoría:** se eligió "Clásico" por la
gran cantidad de libros disponibles para extraer (~16 páginas de
listado, más de 350 fichas en total) y por la variedad de autores y
títulos reconocidos mundialmente (Shakespeare, Dickens, Austen, Dumas,
Pérez Galdós, etc.) que contiene.

**Alcance de la extracción:** se propone extraer los **primeros 150
libros** de esta categoría, en el orden en que aparecen en el listado
paginado del sitio.

## Herramientas

- **Playwright** (Chromium): navega el listado de la categoría y cada
  ficha de libro, y entrega el HTML ya renderizado.
- **BeautifulSoup**: analiza ese HTML y extrae los datos concretos.
- **pandas**: consolida, limpia y exporta el dataset final (`libros.csv`).
- **Git**: versiona el script y este documento en el repositorio del grupo.

## Procedimiento implementado

1. Se abre `https://ww3.lectulandia.co/genero/clasico/` con Playwright
   (Chromium, headless por defecto).
2. Se recorren las páginas siguientes de la categoría usando el patrón
   de paginación real del sitio: `.../genero/clasico/page/2/`,
   `.../page/3/`, etc. (24 fichas por página).
3. Por cada página de listado se obtiene el HTML con `page.content()`.
4. Ese HTML se analiza con BeautifulSoup para localizar los bloques de
   cada libro (`<h2><a href=".../book/slug/">Título</a></h2>`).
5. Se extraen las URLs de las fichas individuales (`/book/<slug>/`), en
   orden, deduplicando a medida que se acumulan, hasta juntar las
   primeras 150.
6. Se visita cada una de esas 150 fichas con Playwright.
7. Con BeautifulSoup se extraen de cada ficha:
   - **Título**: a partir del meta `og:title` (formato fijo del tema del
     sitio: `"<Título> - Epub y PDF"`), con reintentos alternativos
     (último `<h1>` distinto del logo del sitio, o la etiqueta `<title>`)
     por si el maquetado cambia.
   - **Autor/es**: el o los enlaces a `/autor/...` ubicados junto al
     texto "Autor:" propio de la ficha.
   - **Géneros**: los enlaces a `/genero/...` que siguen a ese punto.
   - **Serie**: enlace a `/serie/...`, si el libro pertenece a una
     colección (si no, queda `N/D`).
   - **Sinopsis completa**: el párrafo de texto principal de la ficha.
   - **Imagen de portada** (campo opcional): del meta `og:image`.
   - **`url_libro`**: URL de la propia ficha.
   - **`categoria_origen`**: constante `"Clásico"`.
   - **`fecha_extraccion`**: fecha y hora en que se obtuvo cada registro.

   **Detalle importante del sitio:** la página de cada ficha también
   muestra, más arriba en el HTML, una lista de "libros relacionados"
   (cada uno con sus propios enlaces a autor/género). Por eso la
   extracción no busca "el primer enlace de autor de la página", sino
   que se ubica primero en el bloque real de la ficha —usando como
   referencia el texto literal `"Autor:"`, que solo aparece ahí— y
   recorre desde ese punto hacia adelante hasta la sección de
   comentarios. Esto evita mezclar datos del libro consultado con los de
   los libros relacionados que aparecen antes en el documento.

8. Se limpian los textos (se eliminan saltos de línea y espacios
   repetidos) y se valida que cada registro tenga al menos título y una
   URL de ficha bien formada (`http(s)://...`).
9. Se descartan duplicados por `url_libro`.
10. Los resultados se guardan **incrementalmente** (`libros_incremental.csv`,
    un `append` por libro procesado) y, al finalizar, se genera el
    archivo consolidado `libros.csv` con pandas (deduplicado y validado).

## Alcance y límites éticos/técnicos

- Solo se recolectan **metadatos públicos y la sinopsis** que ya se
  muestran en la ficha del libro.
- **No se descarga** ningún EPUB, PDF ni se sigue ningún enlace de
  `download.php`: esos enlaces se ignoran explícitamente.
- Se incluye una **pausa aleatoria** (1.5–3.5 s) entre cada request
  (tanto entre páginas de categoría como entre fichas) para no
  sobrecargar el servidor.
- Los errores de red o de parseo en una página o ficha puntual **no
  detienen la ejecución**: se registran en `scraping.log` y el proceso
  continúa con la siguiente ficha (hasta 2 reintentos por URL).
- El campo ausente se representa siempre con el valor constante `N/D`
  (nunca vacío, `NaN` o `None`), para mantener consistencia en el CSV.

## Columnas del dataset final (`libros.csv`)

| Columna            | Descripción                                                   |
|--------------------|----------------------------------------------------------------|
| `titulo`           | Título del libro                                                |
| `autores`          | Autor o autores (separados por coma si hay más de uno)          |
| `generos`          | Género o géneros asociados, separados por coma                  |
| `serie`            | Serie/colección a la que pertenece (si aplica; si no, `N/D`)    |
| `sinopsis`         | Texto completo de la sinopsis publicada en la ficha              |
| `url_libro`        | Dirección de la ficha (clave usada para deduplicar)              |
| `categoria_origen` | Categoría seleccionada por el grupo (`"Clásico"`)                |
| `fecha_extraccion` | Fecha y hora en que se obtuvo el registro                        |
| `imagen_portada`   | *(Opcional)* URL de la imagen de portada                         |

## Controles mínimos aplicados antes de dar por cerrado el dataset

- Sin duplicados por `url_libro`.
- 100 % de los registros con `titulo` presente.
- 100 % de los registros con `url_libro` válida (`http`/`https`).
- Mayoría de los registros con `sinopsis` distinta de `N/D`.
- Textos limpios: sin `\n`, `\t` ni espacios múltiples.
- Valores ausentes representados de forma consistente (`N/D`).
- Cantidad final de libros cercana al objetivo de 150 (puede ser algo
  menor si alguna ficha puntual falla por error de red o de parseo; el
  script deja registrado el detalle en `scraping.log`).

Estos controles se verifican automáticamente al final de la ejecución
del script (función `ejecutar_controles_calidad`), que deja un resumen
en `scraping.log` y por consola.

## Cómo ejecutar

```bash
pip install -r requirements.txt
playwright install chromium

# Ejecución estándar: primeros 150 libros, headless
python .\TP1\scraper_lectulandia.py

# Cambiar la cantidad objetivo
python .\TP1\scraper_lectulandia.py --cantidad 100

# Ver el navegador mientras corre (debug)
python .\TP1\scraper_lectulandia.py --con-ventana
```

Salidas generadas:
- `libros_incremental.csv`: se va escribiendo libro a libro durante la
  ejecución (guardado incremental, sirve también de checkpoint si el
  proceso se interrumpe).
- `libros.csv`: archivo final, deduplicado y validado.
- `scraping.log`: registro completo de la ejecución, incluyendo
  advertencias, errores controlados y el resumen de los controles de
  calidad.
