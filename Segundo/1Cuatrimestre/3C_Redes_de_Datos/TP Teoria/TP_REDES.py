import requests
import json
import sys

URL_NOBEL = "https://api.nobelprize.org/v1/prize.json"
ARCHIVO_LOCAL = "nobel_prizes.json"

def inicializar_base_datos():
    print(f"[*] Iniciando solicitud GET sincrónica a {URL_NOBEL}...")
    
    # 1. Definimos los Encabezados (Headers) de la petición HTTP.
    # Engañamos al servidor haciéndole creer que somos un navegador web (Chrome en Windows).
    encabezados = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        # 2. Pasamos el diccionario de encabezados en el parámetro 'headers'
        response = requests.get(URL_NOBEL, headers=encabezados, timeout=10)

        # Validamos explícitamente el status HTTP
        response.raise_for_status() 

        print(f"[+] Código de respuesta del servidor remoto: {response.status_code} OK")

        datos_nobel = response.json()

        with open(ARCHIVO_LOCAL, 'w', encoding='utf-8') as f:
            json.dump(datos_nobel, f, indent=4)

        cantidad_premios = len(datos_nobel.get('prizes', []))
        print(f"[+] Se descargaron exitosamente {cantidad_premios} premios históricos.")
        print(f"[+] Archivo '{ARCHIVO_LOCAL}' generado y listo para la Etapa 1.")

    except requests.exceptions.HTTPError as http_err:
        print(f"[-] Error HTTP devuelto por la API: {http_err}")
    except requests.exceptions.ConnectionError:
        print("[-] Error de Conexión: No se pudo alcanzar el host remoto de NobelPrize.")
    except requests.exceptions.Timeout:
        print("[-] Tiempo de espera agotado (Timeout) en la capa de red.")
    except requests.exceptions.RequestException as req_err:
        print(f"[-] Error catastrófico en la petición de red: {req_err}")
        sys.exit(1)

if __name__ == "__main__":
    inicializar_base_datos()