#!/usr/bin/python3

#############################################################################################################################
# La siguiente es una API que:                                                                                              #
#           - Con un comando "GET /api1" devuelve un "¡Hola!"                                                               #
#           - Con un comnado "GET /api1?nombre=Pepe" devuelve un "¡Hola Pepe!"                                              #
#           - Con un comnado "PUT /api1?nombre=Pepe" crea un archivo "Pepe.txt" vacío dentro de la carpeta /home/juan/API1  #
#############################################################################################################################

from fastapi import FastAPI

app1 = FastAPI()

@app1.get("/api1")
def hello(nombre = None):
    if nombre is None:
     texto = '¡Hola!'
    else:
     texto = '¡Hola '+ nombre +'!'
    return texto
@app1.put("/api1")
def poner(nombre = str()):
    open('/home/juan/API1/'+ nombre +'.txt', 'w')
    return None
