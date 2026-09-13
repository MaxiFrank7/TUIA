import requests
import time
from requests.auth import HTTPBasicAuth

# Configuración del host remoto (nuestro servidor local por ahora)
BASE_URL = "http://localhost:8000"

def probar_endpoints():
    print("==============================================================")
    # 1. PRUEBA GET PÚBLICO: Filtrado por Año y Categoría (Query Params)
    # ==============================================================
    url_prizes = f"{BASE_URL}/prizes"
    parametros = {"year": "2023", "category": "physics"}
    
    print(f"[*] Ejecutando GET a {url_prizes} con parámetros: {parametros}")
    try:
        # Enviamos la solicitud de lectura sincrónica
        response = requests.get(url_prizes, params=parametros, timeout=5)
        
        # Validamos código de estado de red (Esperamos 200 OK)
        if response.status_code == 200:
            data = response.json() # Deserializamos el cuerpo JSON
            print(f"[+] Respuesta 200 OK. Premios encontrados: {data['cantidad']}")
            # Mostramos el primer resultado estructurado
            print(f"    Primer laurato: {data['resultados'][0]['laureates'][0]['firstname']}")
        else:
            print(f"[-] Error inesperado. Código de estado: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Fallo en la capa de transporte/red: {e}")

    print("==============================================================")
    # 2. PRUEBA GET PÚBLICO: Búsqueda Anidada de Laureados
    # ==============================================================
    url_laureates = f"{BASE_URL}/laureates"
    print(f"[*] Ejecutando GET a {url_laureates} buscando a 'Curie'...")
    try:
        response = requests.get(url_laureates, params={"name": "Curie"}, timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"[+] Respuesta 200 OK. Laureados que coinciden: {data['cantidad']}")
            for l in data['resultados']:
                print(f"    - ID {l['id']}: {l.get('firstname')} {l.get('surname', '')}")
        else:
            print(f"[-] Código de estado devuelto: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error de red: {e}")

    print("==============================================================")
    # 3. PRUEBA POST PROTEGIDO: Inserción con Credenciales Incorrectas
    # ==============================================================
    nuevo_premio = {
        "year": "2026",
        "category": "artificial_intelligence",
        "laureates": [{"id": "999", "firstname": "TUIA", "surname": "UNR", "share": "1"}]
    }
    
    print("[*] Intentando POST a /prizes con credenciales INCORRECTAS...")
    try:
        # Enviamos credenciales falsas para forzar el rechazo de autorización
        auth_invalida = HTTPBasicAuth("alumno_redes", "clave_erronea")
        response = requests.post(url_prizes, json=nuevo_premio, auth=auth_invalida, timeout=5)
        
        # Esperamos un código 401 Unauthorized
        print(f"[+] Código de estado devuelto: {response.status_code} (Esperado: 401)")
        print(f"    Detalle del servidor: {response.json().get('detail')}")
        
    except requests.exceptions.RequestException as e:
        print(f"[-] Error de red: {e}")

    print("==============================================================")
    # 4. PRUEBA POST PROTEGIDO: Inserción Exitosa (HTTP Basic Auth)
    # ==============================================================
    print("[*] Intentando POST a /prizes con credenciales VÁLIDAS...")
    try:
        # Usamos las credenciales configuradas en la base del servidor
        auth_valida = HTTPBasicAuth("jtp_redes", "tuia2025")
        response = requests.post(url_prizes, json=nuevo_premio, auth=auth_valida, timeout=5)
        
        # Esperamos un código 201 Created
        if response.status_code == 201:
            print(f"[+] Respuesta {response.status_code} Created exitosa!")
            print(f"    Mensaje: {response.json().get('mensaje')}")
        else:
            print(f"[-] Código de estado devuelto: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Error de red: {e}")

    print("==============================================================")
    # 5. PRUEBA DE RED: Forzar el Rate Limiter (Ataque DoS simulado)
    # ==============================================================
    print("[*] Bombardeando la API con ráfagas rápidas para forzar el Rate Limiting...")
    # Ejecutamos 7 peticiones seguidas inmediatamente para romper el límite de 5 req / 10s
    for i in range(1, 8):
        try:
            response = requests.get(url_prizes, params={"year": "2023"}, timeout=5)
            print(f"    Petición #{i} -> Código de respuesta HTTP: {response.status_code}")
            if response.status_code == 429:
                print(f"[+] ¡Éxito! El middleware bloqueó la inundación de red correctamente.")
                print(f"    Detalle del 429: {response.json().get('detail')}")
        except requests.exceptions.RequestException as e:
            print(f"    [-] Error en petición #{i}: {e}")


if __name__ == "__main__":
    probar_endpoints()