# main_2.py
"""
API de demostración con autenticación Basic.
- /public  (GET)  → accesible sin credenciales
- /protected (POST) → requiere usuario y contraseña
"""

from typing import Dict

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import JSONResponse
import secrets
import uvicorn

app = FastAPI(
    title="Demo API – Autenticación Basic",
    description=(
        "Ejemplo sencillo: algunos endpoints son públicos y otros requieren "
        "autenticación Basic."
    ),
)

# ------------------------------------------------------------------------------
# 1)  Configuración del esquema Basic
# ------------------------------------------------------------------------------
security = HTTPBasic()

# Base de usuarios simulada (¡en un proyecto real cifra las contraseñas!).
USUARIOS: Dict[str, str] = {
    "ivan": "ivan123",
}

def verificar_credenciales(
    credenciales: HTTPBasicCredentials = Depends(security),
) -> str:
    """
    Valida las credenciales enviadas por el cliente.

    - Usa `secrets.compare_digest` para evitar ataques de *timing*.
    - Lanza HTTP 401 si usuario/contraseña no son correctos.
    """
    pwd_correcta = USUARIOS.get(credenciales.username)
    if not pwd_correcta or not secrets.compare_digest(
        credenciales.password, pwd_correcta
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credenciales.username  # Devuelve el nombre del usuario autenticado

# ------------------------------------------------------------------------------
# 2)  Endpoints
# ------------------------------------------------------------------------------

@app.get("/public")
async def endpoint_publico():
    """Recurso accesible sin autenticación."""
    return {"mensaje": "Hola, mundo. Este endpoint es público."}

@app.post("/protected")
async def endpoint_protegido(usuario: str = Depends(verificar_credenciales)):
    """
    Recurso protegido con Basic Auth.
    El parámetro `usuario` contiene el nombre autenticado.
    """
    return JSONResponse(
        {
            "mensaje": f"Acceso concedido a «{usuario}». "
                       "Has llamado a un endpoint protegido 😎"
        }
    )

# ------------------------------------------------------------------------------
# 3)  Arranque del servidor
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("main_2:app", host="0.0.0.0", port=8000, reload=True)
