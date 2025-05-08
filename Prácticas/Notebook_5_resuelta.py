# Ejercicio 1 - Listas (Suma acumulada)
def acumularSuma(lista):
    suma_acumulada = []
    total = 0
    for num in lista:
        total += num
        suma_acumulada.append(total)
    return suma_acumulada

# Ejemplo de uso
print(acumularSuma([1, 2, 3]))  # Salida: [1, 3, 6]

# Ejercicio 2 - Listas (Datos personales)
def generarDatosPersonales():
    datos_solicitados = ['Nombre', 'Apellido', 'Localidad', 'Edad', 'DNI', 'Carrera en curso', 'Año de inicio de la carrera']
    datosPersonales = []
    
    for dato in datos_solicitados:
        valor = input(f"Ingrese su {dato}: ")
        if dato in ['Edad', 'Año de inicio de la carrera']:
            valor = int(valor)
        datosPersonales.append(valor)
    
    return datosPersonales

# Ejemplo de uso
# datos_personales = generarDatosPersonales()
# print(datos_personales)

# Ejercicio 3 - Listas (Base de datos)
def imprimirBaseDatos(base_datos):
    for i, persona in enumerate(base_datos, 1):
        print(f"\nDatos de la persona {i}:")
        for dato, valor in zip(['Nombre', 'Apellido', 'Localidad', 'Edad', 'DNI', 'Carrera', 'Año de inicio'], persona):
            print(f"{dato}: {valor}")

# Ejemplo de uso
# base_datos = [datos_personales1, datos_personales2]  # lista de listas de datos personales
# imprimirBaseDatos(base_datos)

# Ejercicio 4 - Listas (Contar vocales)
def cuenta(frase: str) -> list:
    '''Función que recibe una frase de tipo string y devuelve una lista con la cantidad de ocurrencias de cada vocal'''
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in frase.lower():
        if letra in vocales:
            vocales[letra] += 1
    return [vocales['a'], vocales['e'], vocales['i'], vocales['o'], vocales['u']]

resultado = cuenta("hola, como estas tu")
print(resultado)  # Ejemplo de salida: [2, 1, 0, 3, 1]

# Ejercicio 5 - Listas (Eliminar duplicados)
def elimina_duplicados(lista):
    return list(set(lista))

lista = [1, 2, 4, 4, 6, 'a']
nueva_lista = elimina_duplicados(lista)
print(nueva_lista)  # Ejemplo de salida: [1, 2, 4, 6, 'a']

# Ejercicio 6 - Listas (Palíndromos)
def palindromo(lista_palabras):
    return [palabra for palabra in lista_palabras if palabra == palabra[::-1]]

lista = ['rojo', 'cara', 'oro', 'somos', 'gato']
print(palindromo(lista))  # Salida: ['oro', 'somos']

# Ejercicio 1 - Tuplas (Días de la semana)
dias_semana = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo')
print(dias_semana)
print(f"Longitud de la tupla: {len(dias_semana)}")

# Ejercicio 2 - Tuplas (Precios productos)
precios = (1500, 200, 3500, 800, 1200)
maximo = max(precios)
minimo = min(precios)
print(f"Precio más alto: {maximo}, Precio más bajo: {minimo}")

# Ejercicio 3 - Tuplas (Frutas y precios)
frutas = ('manzana', 'plátano', 'cereza')
precios_frutas = (150, 200, 350)

for fruta, precio in zip(frutas, precios_frutas):
    print(f"{fruta}: ${precio}")

# Ejercicio 4 - Tuplas (Personas por edad)
personas = (('Juan', 25), ('María', 30), ('Carlos', 20))
personas_ordenadas = tuple(sorted(personas, key=lambda x: x[1]))
print(personas_ordenadas)

# Ejercicio 5 - Tuplas (Suma números pares)
numeros_pares = tuple(range(2, 21, 2))
suma = sum(numeros_pares)
print(f"Suma de los primeros 10 números pares: {suma}")

# Ejercicio 1 - Diccionarios (Contar palabras)
def contar_palabras(cadena):
    palabras = cadena.split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

print(contar_palabras("la peluca de la abuela"))  # Salida: {'la': 2, 'peluca': 1, 'de': 1, 'abuela': 1}

# Ejercicio 2 - Diccionarios (Verdulería)
def crear_verduleria():
    verduleria = {}
    while True:
        producto = input("Ingrese el nombre del producto: (* para salir) ")
        if producto == '*':
            break
        precio = int(input("Ingrese el precio del producto: "))
        verduleria[producto] = precio
    return verduleria

# Ejemplo de uso
# verduleria = crear_verduleria()
# print(verduleria)

# Ejercicio 3 - Diccionarios (Imprimir verdulería)
def imprimir_verduleria(verduleria):
    for producto, precio in verduleria.items():
        print(f"{producto}: ${precio}")

# Ejercicio 4 - Diccionarios (Consultar producto)
def consultar_producto(verduleria):
    producto = input("Ingrese la fruta/verdura que desea consultar: ")
    if producto in verduleria:
        print(f"El precio de {producto} es ${verduleria[producto]}")
    else:
        respuesta = input(f"{producto} no está en stock. ¿Desea agregarla? (s/n) ")
        if respuesta.lower() == 's':
            precio = int(input(f"Ingrese el precio de {producto}: "))
            verduleria[producto] = precio
            print(f"{producto} agregada al stock con precio ${precio}")

# Ejercicio 5 - Diccionarios (Notas alumnos)
def ingresar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    return nombre, notas

def calcular_promedios(alumnos):
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {nombre} es {promedio:.6f}")

# Ejemplo de uso
# alumnos = {}
# for _ in range(3):  # Supongamos 3 alumnos
#     nombre, notas = ingresar_alumno()
#     alumnos[nombre] = notas
# calcular_promedios(alumnos)

# Ejercicio 6 - Diccionarios (Cartas)
import random

def crear_mazo():
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    mazo = [{'palo': palo, 'valor': valor} for palo in palos for valor in valores]
    return mazo

def es_poker(cartas):
    valores = [carta['valor'] for carta in cartas]
    conteo = {}
    for valor in valores:
        conteo[valor] = conteo.get(valor, 0) + 1
    return 4 in conteo.values()

def barajar_poker():
    mazo = crear_mazo()
    random.shuffle(mazo)
    mano = mazo[:5]
    return mano, es_poker(mano)

# Ejemplo de uso
mano, resultado = barajar_poker()
print("Cartas:", [f"{c['valor']} de {c['palo']}" for c in mano])
print("¿Es poker?", resultado)