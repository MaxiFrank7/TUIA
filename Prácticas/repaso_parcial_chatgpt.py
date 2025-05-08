# Resolución del PDF: Repaso Parcial - Programación 1 (FCEIA - UNR)

# === 1.1 - Menúes vendidos ===

# a) Se vendieron 150 menúes (cantidad fija)
from random import choice
print("Opción A - Menúes predefinidos")
menues = [choice(["E", "D", "O"]) for _ in range(150)]
est = menues.count("E")
doc = menues.count("D")
otr = menues.count("O")
print("Estudiantiles:", est, "Docentes:", doc, "Otros:", otr)

# b) Cantidad ingresada por usuario
print("\nOpción B - Menúes ingresados por usuario")
cant = int(input("Ingrese cantidad de menúes vendidos: "))
est = doc = otr = 0
for _ in range(cant):
    tipo = input("Ingrese tipo de menú (E/D/O): ").upper()
    if tipo == "E": est += 1
    elif tipo == "D": doc += 1
    elif tipo == "O": otr += 1
print("Estudiantiles:", est, "Docentes:", doc, "Otros:", otr)

# c) Fin de datos
print("\nOpción C - Fin de datos")
est = doc = otr = 0
while True:
    tipo = input("Ingrese tipo de menú (E/D/O) o FIN para terminar: ").upper()
    if tipo == "FIN": break
    if tipo == "E": est += 1
    elif tipo == "D": doc += 1
    elif tipo == "O": otr += 1
print("Estudiantiles:", est, "Docentes:", doc, "Otros:", otr)

# === 1.2 - Validación del tipo ===
# Agregado en las opciones b y c (solo se cuentan si el tipo es válido)

# === 1.3 - Proporción de Estudiantiles ===
total = est + doc + otr
if total > 0:
    print("Proporción de menúes estudiantiles:", round(est / total, 2))
else:
    print("No se ingresaron menúes válidos")

# === 2.1 - Soporte más usado ===
def ingresoDeDatos() -> dict:
    dicc = {}
    while True:
        soporte = input("Ingrese soporte (o FIN para terminar): ")
        if soporte.upper() == "FIN": break
        porcentaje = float(input(f"Ingrese porcentaje de uso de {soporte}: "))
        dicc[soporte] = porcentaje
    return dicc

def soporte_mas_usado(datos: dict) -> tuple:
    soporte_max = max(datos, key=datos.get)
    return soporte_max, datos[soporte_max]

def principal_soportes() -> None:
    datos = ingresoDeDatos()
    soporte, uso = soporte_mas_usado(datos)
    print(f"Soporte más usado: {soporte} con {uso}%")

# principal_soportes()

# === 2.2 - Notas de alumnos ===
def ingresoNotas() -> list:
    notas = []
    while True:
        nombre = input("Ingrese nombre (o FIN para terminar): ")
        if nombre.upper() == "FIN": break
        nota = float(input(f"Ingrese nota de {nombre}: "))
        notas.append((nombre, nota))
    return notas

def promMax(listaNotas: list) -> tuple:
    total = sum(n[1] for n in listaNotas)
    prom = total / len(listaNotas) if listaNotas else 0
    notaMaxima = max(listaNotas, key=lambda x: x[1])[1] if listaNotas else 0
    return prom, notaMaxima

def principal_notas() -> None:
    lista = ingresoNotas()
    prom, maxNota = promMax(lista)
    print("Promedio del curso:", prom)
    print("Nota máxima:", maxNota)
    print("Estudiantes con nota máxima:")
    for nombre, nota in lista:
        if nota == maxNota:
            print("-", nombre)

# principal_notas()

# === 2.3 - Guardería canina ===
def ingresoMascotas() -> list:
    lista = []
    while True:
        id = input("Ingrese identificador (o FIN para terminar): ")
        if id.upper() == "FIN": break
        monto = float(input(f"Ingrese monto para {id}: "))
        lista.append((id, monto))
    return lista

def total_x_mascota(registros: list) -> dict:
    dicc = {}
    for id, monto in registros:
        if id in dicc:
            dicc[id] += monto
        else:
            dicc[id] = monto
    return dicc

def promedio(totxmasc: dict) -> float:
    if not totxmasc:
        return 0
    return sum(totxmasc.values()) / len(totxmasc)

def principal_guarderia() -> None:
    registros = ingresoMascotas()
    totales = total_x_mascota(registros)
    print("Montos totales por mascota:")
    for k, v in totales.items():
        print(f"{k}: ${v:.2f}")
    print("Promedio de montos totales:", promedio(totales))

# principal_guarderia()