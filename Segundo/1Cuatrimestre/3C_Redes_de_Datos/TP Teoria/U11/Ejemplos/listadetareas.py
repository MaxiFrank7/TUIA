# Para usar se debe instalar fastapi y uvicorn
# Servidor de lista de tareas con FastAPI
# Ejecutar con:
#  uvicorn listadetareas:app --reload
# Luego acceder a la dirección indicada por uvicorn para probar su ejecución
# Probablemente sea http://127.0.0.1:8000
# Para practicar el uso de la api se puede usar el link http://127.0.0.1:8000/docs


from fastapi import FastAPI

app = FastAPI()

from fastapi import HTTPException

tareas=["estudiar redes","pasear al perro"]


# Ejemplo muy básicos de acceso
# cuando accedemos a http://127.0.0.1:8000/saludar?nombre=nombre responde Hola nombre!
@app.get("/saludar")
def hola(nombre = None):
    if nombre is None:
        text = 'Hola!'
    else:
        text = 'Hola ' + nombre + '!'
    return text


@app.get("/tareas")
def get_tareas():
    return tareas

@app.post("/tareas")
def crear_tarea(tarea: str):
    tareas.append(tarea)
    return {"message": "Tarea creada"}

@app.put("/tareas/{tarea_id}")
def update_tarea(tarea_id: int, tarea: str):
    if tarea_id < 0 or tarea_id >= len(tareas):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    tareas[tarea_id] = tarea
    return {"message": "Tarea actualizada"}

@app.delete("/tareas/{tarea_id}")
def delete_tarea(tarea_id: int):
    if tareas_id < 0 or tarea_id >= len(tareas):
        raise HTTPException(status_code=404, detail="Tarea no encontrada. Indice fuera de rango")
    del tareas[tarea_id]
    return {"message": "Tarea eliminada"}

