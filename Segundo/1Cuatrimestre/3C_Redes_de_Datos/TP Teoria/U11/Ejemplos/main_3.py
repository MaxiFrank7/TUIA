# rate_limited_api.py
"""
API de demostración con limitación de tasa (Rate Limiting).
Permite 10 peticiones por segundo y por IP.
"""

from collections import deque
from datetime import datetime, timedelta
from typing import Deque, Dict

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(
    title="Demo API – Rate Limiting",
    description="Límite de 10 solicitudes por segundo por dirección IP.",
)

# -------------------------------------------------------------------------
# 1)  Parámetros del limitador
# -------------------------------------------------------------------------
VENTANA = timedelta(seconds=1)   # Ventana de tiempo
MAX_PETICIONES = 10             # Máximo de peticiones dentro de la ventana

cubos_ip: Dict[str, Deque[datetime]] = {}

@app.middleware("http")
async def limitador(request: Request, call_next):
    ip = request.client.host
    ahora = datetime.utcnow()

    cubo = cubos_ip.setdefault(ip, deque())

    # Eliminar timestamps fuera de la ventana
    while cubo and (ahora - cubo[0]) > VENTANA:
        cubo.popleft()

    if len(cubo) >= MAX_PETICIONES:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Demasiadas solicitudes: límite 10 req/s",
        )

    cubo.append(ahora)
    respuesta = await call_next(request)
    return respuesta

# -------------------------------------------------------------------------
# 2)  Endpoint de prueba
# -------------------------------------------------------------------------
@app.get("/ping")
async def ping():
    return JSONResponse({"msg": "pong", "ts": datetime.utcnow().isoformat()})

# -------------------------------------------------------------------------
# 3)  Arranque del servidor
# -------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("main_3:app", host="0.0.0.0", port=8001, reload=True)
