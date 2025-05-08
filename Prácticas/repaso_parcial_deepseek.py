# Ejercicios 1.1 a 1.3
def ejercicio_1():
    # Algoritmo 1a: 150 menúes con distribución aleatoria
    import random
    E = D = O = 0
    for _ in range(150):
        tipo = random.choice(['E', 'D', 'O'])
        if tipo == 'E': E +=1
        elif tipo == 'D': D +=1
        else: O +=1
    print("\nAlgoritmo 1a (150 menúes):")
    print(f"Estudiantil: {E}, Docente: {D}, Otro: {O}")

    # Algoritmo 1b: Cantidad ingresada por usuario
    E = D = O = 0
    n = int(input("\nIngrese cantidad total de menúes: "))
    for _ in range(n):
        while True:
            tipo = input("Tipo (E/D/O): ").upper()
            if tipo in ['E','D','O']: break
        if tipo == 'E': E +=1
        elif tipo == 'D': D +=1        
        else: O +=1
    print("\nAlgoritmo 1b (con validación):")
    print(f"Estudiantil: {E}, Docente: {D}, Otro: {O}")
    
    # Algoritmo 1c: Datos hasta ingresar 'fin'
    E = D = O = 0
    while True:
        dato = input("\nIngrese tipo (E/D/O) o 'fin': ").upper()
        if dato == 'FIN': break
        if dato in ['E','D','O']:
            if dato == 'E': E +=1
            elif dato == 'D': D +=1
            else: O +=1
    total = E + D + O
    print("\nAlgoritmo 1c (proporción estudiantes):")
    print(f"Proporción E: {E/total if total >0 else 0:.2%}")

# Ejercicio 2.1 Globalizador
def ingresoDeDatos() -> dict:
    dicc = {}
    soportes = ['Celular', 'Tablet', 'PC', 'Consola']
    for soporte in soportes:
        porcentaje = float(input(f"Ingrese % para {soporte}: "))
        dicc[soporte] = porcentaje
    return dicc

def soporte_mas_usado(datos: dict) -> tuple:
    soporte_max = max(datos, key=datos.get)
    return soporte_max, datos[soporte_max]

def principal_globalizador():
    datos = ingresoDeDatos()
    soporte, porcentaje = soporte_mas_usado(datos)
    print(f"\nSoporte más usado: {soporte} ({porcentaje}%)")

# Ejercicio 2.2 Notas de estudiantes
def ingresoDeDatos() -> list:
    notas = []
    while True:
        nombre = input("Nombre (vacío para terminar): ")
        if not nombre: break
        nota = int(input("Nota: "))
        notas.append((nombre, nota))
    return notas

def promMax(listaNotas: list) -> tuple:
    total = sum(nota for _, nota in listaNotas)
    prom = total / len(listaNotas) if listaNotas else 0
    max_nota = max(nota for _, nota in listaNotas) if listaNotas else 0
    return prom, max_nota

def principal_notas():
    datos = ingresoDeDatos()
    if not datos:
        print("No se ingresaron datos")
        return
    promedio, maxima = promMax(datos)
    print(f"\nNota promedio: {promedio:.2f}")
    print("Mejores estudiantes:")
    for nombre, nota in datos:
        if nota == maxima:
            print(nombre)

# Ejercicio 2.3 Guardería canina
def ingresoDeDatos() -> list:
    registros = []
    while True:
        mascota = input("ID mascota (vacío para terminar): ")
        if not mascota: break
        monto = float(input("Monto estadía: "))
        registros.append((mascota, monto))
    return registros

def total_x_mascota(registros: list) -> dict:
    totales = {}
    for mascota, monto in registros:
        if mascota in totales:
            totales[mascota] += monto
        else:
            totales[mascota] = monto
    return totales

def promedio(totxmasc: dict) -> float:
    if not totxmasc: return 0
    return sum(totxmasc.values()) / len(totxmasc)

def principal_mascotas():
    datos = ingresoDeDatos()
    if not datos:
        print("No se ingresaron datos")
        return
    totales = total_x_mascota(datos)
    print("\nTotal por mascota:")
    for mascota, total in totales.items():
        print(f"{mascota}: ${total:.2f}")
    prom = promedio(totales)
    print(f"\nPromedio totales: ${prom:.2f}")

# Ejecutar todos los programas
if __name__ == "__main__":
    ejercicio_1()
    principal_globalizador()
    principal_notas()
    principal_mascotas()