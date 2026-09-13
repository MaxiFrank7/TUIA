import json
import secrets
from typing import Dict, Optional
from collections import deque
from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import JSONResponse
import uvicorn

# Instanciamos nuestra API
app = FastAPI(title="API Premios Nobel - Servidor")

# ==============================================================================
# 1. CONFIGURACIÓN DE SEGURIDAD Y RED (ETAPA 4)
# ==============================================================================

# A. Autenticación Básica (Para POST y DELETE)
security = HTTPBasic()
# Base de usuarios simulada. En producción esto iría encriptado en una base real.
USUARIOS: Dict[str, str] = {"jtp_redes": "tuia2025"}

def verificar_credenciales(credenciales: HTTPBasicCredentials = Depends(security)) -> str:
    """
    Valida las credenciales. Usa secrets.compare_digest para evitar ataques de timing.
    Lanza HTTP 401 Unauthorized si el usuario/contraseña no coinciden.
    """
    pwd_correcta = USUARIOS.get(credenciales.username)
    if not pwd_correcta or not secrets.compare_digest(credenciales.password, pwd_correcta):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, # La solicitud no tiene credenciales válidas
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credenciales.username

# B. Limitación de Tasa (Rate Limiting) - Algoritmo de Ventana Fija
VENTANA = timedelta(seconds=10) # Definimos la ventana de tiempo
MAX_PETICIONES = 5              # Máximo de peticiones permitidas en esa ventana
cubos_ip = {}

@app.middleware("http")
async def limitador_tasa(request: Request, call_next):
    """
    Middleware que intercepta cada solicitud entrante para evitar ataques DoS.
    """
    ip = request.client.host
    ahora = datetime.utcnow()
    cubo = cubos_ip.setdefault(ip, deque())
    
    # Limpiamos las peticiones que quedaron fuera de la ventana de tiempo
    while cubo and (ahora - cubo[0]) > VENTANA:
        cubo.popleft()
        
    # Si la cola superó el límite, rechazamos la conexión con un 429
    if len(cubo) >= MAX_PETICIONES:
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS, 
            content={"detail": "Límite de velocidad excedido. Máximo 5 req/10s."}
        )
        
    cubo.append(ahora)
    return await call_next(request)


# ==============================================================================
# 2. MANEJO DE LA BASE DE DATOS LOCAL
# ==============================================================================
ARCHIVO_LOCAL = "nobel_prizes.json"

def cargar_db():
    with open(ARCHIVO_LOCAL, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_db(datos):
    with open(ARCHIVO_LOCAL, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4)


# ==============================================================================
# 3. ENDPOINTS DE LA API (ETAPA 2)
# ==============================================================================

# Endpoint GET: Público. Recupera detalles de recursos.
@app.get("/prizes")
def get_prizes(year: Optional[str] = None, category: Optional[str] = None):
    db = cargar_db()
    premios = db.get("prizes", [])
    
    # Procesamos los parámetros de consulta (Query params)
    if year:
        premios = [p for p in premios if p.get("year") == year]
    if category:
        premios = [p for p in premios if p.get("category") == category]
        
    if not premios:
        # 404 No se encontró: El recurso no existe en el servidor
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron premios con esos filtros")
        
    # 200 OK implícito
    return {"cantidad": len(premios), "resultados": premios}


# Endpoint GET: Público. Búsqueda anidada.
@app.get("/laureates")
def buscar_laureates(name: str):
    db = cargar_db()
    resultados = []
    
    # Iteración exhaustiva por los arreglos anidados
    for premio in db.get("prizes", []):
        for laureado in premio.get("laureates", []):
            # Manejamos diccionarios que pueden no tener el campo 'surname' (como las organizaciones)
            nombre_completo = f"{laureado.get('firstname', '')} {laureado.get('surname', '')}".lower()
            if name.lower() in nombre_completo:
                # Validamos que no se dupliquen laureados que ganaron más de una vez (ej. Marie Curie)
                if not any(l['id'] == laureado['id'] for l in resultados):
                    resultados.append(laureado)
                    
    if not resultados:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laureado no encontrado")
        
    return {"cantidad": len(resultados), "resultados": resultados}


# Endpoint POST: Protegido. Crea un nuevo recurso.
@app.post("/prizes", status_code=status.HTTP_201_CREATED)
def crear_premio(nuevo_premio: dict, usuario: str = Depends(verificar_credenciales)):
    db = cargar_db()
    
    # Validamos estructura básica
    if "year" not in nuevo_premio or "category" not in nuevo_premio:
        # 400 Solicitud no válida
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El cuerpo debe incluir 'year' y 'category'")
        
    db["prizes"].insert(0, nuevo_premio)
    guardar_db(db)
    
    return {"mensaje": f"Premio creado exitosamente por {usuario}", "premio": nuevo_premio}


# Endpoint DELETE: Protegido. Elimina un recurso del sistema.
@app.delete("/prizes/{year}/{category}")
def borrar_premio(year: str, category: str, usuario: str = Depends(verificar_credenciales)):
    db = cargar_db()
    premios = db.get("prizes", [])
    
    # Filtramos eliminando la coincidencia exacta
    premios_filtrados = [p for p in premios if not (p.get("year") == year and p.get("category") == category)]
    
    if len(premios) == len(premios_filtrados):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El premio no existe o ya fue eliminado")
        
    db["prizes"] = premios_filtrados
    guardar_db(db)
    return {"mensaje": f"Premio de {category} en {year} eliminado por {usuario}"}

# Arranque del servidor
if __name__ == "__main__":
    uvicorn.run("servidor_api:app", host="0.0.0.0", port=8000, reload=True)