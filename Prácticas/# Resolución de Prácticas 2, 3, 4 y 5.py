# Resolución de Prácticas 2, 3, 4 y 5
# Programación 1 - Tecnicatura Universitaria en Inteligencia Artificial (FCEIA - UNR)

# === PRÁCTICA 2 ===

# Ejercicio 1a - Corregido
saludo = "Hola"
destino = "Mundo"
puntuacion = "!"
print(saludo + " " + destino + puntuacion)

# Ejercicio 1b
cateto1 = 3
cateto2 = 4
hipotenusa = (( cateto1 ** 2) + (cateto2 ** 2)) ** 0.5
del cateto1
del cateto2
print(hipotenusa)

# Ejercicio 1c - Corregido
tengo_hambre = False
del tengo_hambre
tengo_hambre = True

# Ejercicio 2
print(3 == 3.0)                          # True
print(3 == (0.1 + 0.2) * 10)             # False
print(22 / 7 == 22 // 7)                # False

# Ejercicio 3
print(type(10 + 5))      # int
print(type(10 + 5.0))    # float
print(type(10 + 5.))     # float
print(11 / 2)            # 5.5
print(11 // 2)           # 5
print(11.0 // 2)         # 5.0

# Ejercicio 4
print(+1)
print(-1)
print(+-1)
print(--1)

# Ejercicio 5a
t1 = 18
t2 = 22
print("Temperatura promedio:", (t1 + t2) / 2)

# Ejercicio 5b
personas = 5
tiempo = personas * (personas - 1) * 4.5
print("Tiempo total:", tiempo)

# Ejercicio 5c
n1 = "Alejandro"
n2 = "Alejandra"
print(len(n1) == len(n2))
print(n1 == n2)

# Ejercicio 6
print(len("Hola, mundo") == 14)                      # False
print(5**2 == 625**0.5)                               # True
print(6.5 < 7 and 6.5 > 6)                            # True
#print(22 / 7 > 3 and 2 + 2 == 5)                     # False
#print(10 > 5 or 0 / 0 == 0)                          # Error
#print(len("Python") == 5 and 1+"1" == 2)            # Error

# Ejercicio 7
print(3 * 5 - 7 * 4 / 14 + 3 / 1)                    # float
print(2 ** 1 + 3 / 5 // 4)                           # float
print(8 / 4 / 2 ** 2 ** 2)                           # float

# === PRÁCTICA 3 ===

# Ejercicio 1
password = input("Ingrese su contraseña: ")
if len(password) > 8:
    print("Contraseña válida")
else:
    print("Contraseña demasiado corta")

# Ejercicio 2
numero = int(input("Ingrese un número: "))
if numero % 4 == 0:
    print("Es divisible por 4")
else:
    print("No es divisible por 4")

# Ejercicio 3
nums = [int(input(f"Número {i+1}: ")) for i in range(3)]
mayor = max(nums)
print("El mayor es:", mayor)

# Ejercicio 4
l1 = int(input("Lado 1: "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))
if l1 == l2 == l3:
    print("Equilátero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Isósceles")
else:
    print("Escaleno")

# Ejercicio 5
letra = input("Ingrese calificación (I, A, B, M, D, E): ").upper()
conversor = {'I': 5, 'A': 6, 'B': 7, 'M': 8, 'D': 9, 'E': 10}
print(conversor.get(letra, "Error: calificación inexistente"))

# Ejercicio 6
fecha = input("Ingrese su fecha de cumpleaños (DD/MM): ")
try:
    dia, mes = map(int, fecha.split("/"))
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20): signo = "Aries"
    else: signo = "(otro signo aquí)"
    print("Signo:", signo)
except:
    print("Formato incorrecto")

# Ejercicio 7
zona = input("Zona (A, B, C): ").upper()
horas = int(input("Horas de estacionamiento: "))
costos = {
    'A': [57.00, 71.20, 85.50],
    'B': [47.00, 58.70, 70.50],
    'C': [37.00, 46.20, 55.50]
}
if zona in costos and 1 <= horas <= 3:
    print("Total:", sum(costos[zona][:horas]))
else:
    print("Error: zona inválida o tiempo excedido")

# Ejercicio 8 y 9
item = input("Item (zapatillas, remeras, pantalones): ").lower()
sede = input("Sede (rosario, funes, roldan): ").lower()
dia = input("Día (lunes, miércoles, jueves): ").lower()
descuentos = {
    'rosario': {'zapatillas': 30, 'remeras': 20, 'pantalones': 10},
    'funes': {'zapatillas': 40, 'remeras': 30, 'pantalones': 5},
    'roldan': {'zapatillas': 25, 'remeras': 15, 'pantalones': 20}
}
adicional = {'lunes': 10, 'miércoles': 8, 'jueves': 5}
if sede in descuentos and item in descuentos[sede]:
    total = descuentos[sede][item] + adicional.get(dia, 0)
    print("Descuento total:", total, "%")
else:
    print("Error en los datos ingresados")


# === PRÁCTICA 4 ===

# Ejercicio 1
for i in range(1, 21):
    print(i)

# Ejercicio 2
for i in range(11):
    print(f"5 x {i} = {5 * i}")

# Ejercicio 3
for i in range(-10, 0):
    print(i)

# Ejercicio 4
numeros = [12, 75, 150, 180, 145, 525, 50]
for n in numeros:
    if n % 5 == 0 and n < 150:
        print(n)

# Ejercicio 5
fibo = [0, 1]
while len(fibo) < 10:
    fibo.append(fibo[-1] + fibo[-2])
print(fibo)

# Ejercicio 6
fact = 1
for i in range(1, 6):
    fact *= i
print("Factorial de 5:", fact)

# Ejercicio 7
lista = []
for j in lista:
    print(j)
# No imprime nada

i = 1
for i in [1, 2, 3]:
    print(i)
print(i)  # Imprime último valor: 3

# Ejercicio 8
a = [x**2 for x in range(10)]
print("Cuadrados:", a)

print("Suma 0-100:", sum(range(101)))
pares = [x for x in range(100) if x % 2 == 0]
print("Suma pares:", sum(pares), "Cantidad:", len(pares))
impares = [x for x in range(100) if x % 2 != 0]
print("Suma impares:", sum(impares), "Cantidad:", len(impares))

# Ejercicio 9
# while x < 5: print(x) → Bucle infinito porque x no se incrementa

# Ejercicio 10
umbral = 34
valores = [3, 5, 4, 4, 5, 5, 3, 5, 2, 7]
suma = 0
for x in valores:
    suma += x
    if suma >= umbral:
        break
print("Suma acumulada:", suma)

# Ejercicio 11
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0
i = 0
while i < len(valores):
    if valores[i] % 2 != 0:
        i += 1
        continue
    suma += valores[i]
    i += 1
print("Suma de pares:", suma)

# Ejercicio 12
while True:
    entrada = input("Ingrese un número o 'salir': ")
    if entrada.lower() == 'salir':
        break
    if entrada.isdigit():
        n = int(entrada)
        print("La suma es", sum(range(n)))

# Ejercicio 13
billete_grosor = 0.11 * 0.001
altura_monumento = 70
billetes_n = 1
dia = 1
altura = billetes_n * billete_grosor
while altura < altura_monumento:
    billetes_n *= 2
    dia += 1
    altura = billetes_n * billete_grosor
print("Días necesarios:", dia)

# Ejercicio 14a
n1 = 3
n2 = 20
contador = 0
for i in range(n1, n2):
    if i % n1 == 0:
        contador += 1
print("Múltiplos con for:", contador)

# Ejercicio 14b
i = 1
contador = 0
while n1 * i < n2:
    contador += 1
    i += 1
print("Múltiplos con while:", contador)

# === PRÁCTICA 5 ===

# Ejercicio 1a
lista = [11, 25, 3, -4, 95]
n = 3
indice = -1
for i in range(len(lista)):
    if lista[i] == n:
        indice = i
        break
print(indice)

# Ejercicio 1b
minimo = lista[0]
maximo = lista[0]
for num in lista:
    if num < minimo:
        minimo = num
    if num > maximo:
        maximo = num
print("Mínimo:", minimo, "Máximo:", maximo)

# Ejercicio 1c
nueva = [x + 1 for x in [0, 1, 2, 3, 4]]
print(nueva)

# Ejercicio 1d
palabras = ["arbol", "barco", "artificial", "casa", "dado", "a"]
filtradas = [p for p in palabras if p.startswith("a")]
print(filtradas)

# Ejercicio 1e
numeros = [0, 1, 2, 3, 4, 5]
suma_par = sum(numeros[i] for i in range(0, len(numeros), 2))
producto_impar = 1
for i in range(1, len(numeros), 2):
    producto_impar *= numeros[i]
print("Suma pares:", suma_par)
print("Producto impares:", producto_impar)

# Ejercicio 1f
reversa = []
for i in range(len(numeros)-1, -1, -1):
    reversa.append(numeros[i])
print(reversa)

# Ejercicio 2
lista = [1, 2, 3]
acumulada = []
suma = 0
for x in lista:
    suma += x
    acumulada.append(suma)
print(acumulada)

# Ejercicio 3
lista = [1, 2, 3, 4, 2, 5]
repetidos = []
for i in range(len(lista)):
    if lista[i] in lista[i+1:]:
        repetidos.append(lista[i])
print("Repetidos:", repetidos)

# Ejercicio 4
fibo = [0, 1]
while len(fibo) < 10:
    fibo.append(fibo[-1] + fibo[-2])
print(fibo)

# Ejercicio 5a
nombre = input("Nombre: ")
apellido = input("Apellido: ")
localidad = input("Localidad: ")
edad = int(input("Edad: "))
dni = int(input("DNI: "))
carrera = input("Carrera universitaria: ")
anio_inicio = int(input("Año de inicio de la carrera: "))
datos_personales = [nombre, apellido, localidad, edad, dni, carrera, anio_inicio]
print(datos_personales)

# Ejercicio 5b
from datetime import datetime
anio_actual = datetime.now().year
anios_cursados = anio_actual - anio_inicio
datos_personales.append(anios_cursados)
print(f"{nombre} {apellido} lleva {anios_cursados} años cursando")

# Ejercicio 5c
basedatos = []
while True:
    continuar = input("¿Desea cargar otra persona? (s/n): ").lower()
    if continuar != 's':
        break
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    localidad = input("Localidad: ")
    edad = int(input("Edad: "))
    dni = int(input("DNI: "))
    carrera = input("Carrera universitaria: ")
    anio_inicio = int(input("Año de inicio de la carrera: "))
    anios_cursados = datetime.now().year - anio_inicio
    datos_personales = [nombre, apellido, localidad, edad, dni, carrera, anio_inicio, anios_cursados]
    basedatos.append(datos_personales)

# Ejercicio 5d
for persona in basedatos:
    persona[5] = "TUIA"
print(basedatos) #se agregan años cursados, se automatiza para varios usuarios, y se cambia la carrera por "TUIA"

# Ejercicio 6a
# Representación con tuplas para cartas: (valor, palo)
carta = ("10", "corazones")

# Ejercicio 6b
# Verificar si una mano es poker (4 cartas del mismo valor)
mano = [("10", "corazones"), ("10", "tréboles"), ("10", "picas"), ("10", "diamantes"), ("5", "corazones")]
valores = [carta[0] for carta in mano]
print(valores.count("10") == 4)  # True si es poker

# Ejercicio 7a
# Representar tiempo como tupla (horas, minutos, segundos)
tiempo1 = (1, 45, 30)
tiempo2 = (2, 20, 50)

# Ejercicio 7b
# Sumar tiempos
def sumar_tiempos(t1, t2):
    h = t1[0] + t2[0]
    m = t1[1] + t2[1]
    s = t1[2] + t2[2]
    m += s // 60
    s %= 60
    h += m // 60
    m %= 60
    return (h, m, s)

print(sumar_tiempos(tiempo1, tiempo2))

# Ejercicio 8
# Calcular el día siguiente de una fecha (día, mes, año)
def dia_siguiente(d, m, a):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if d < dias_mes[m - 1]:
        return (d + 1, m, a)
    elif m < 12:
        return (1, m + 1, a)
    else:
        return (1, 1, a + 1)

print(dia_siguiente(31, 12, 2023))

# Ejercicio 9
# Fecha con mes como texto
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
def siguiente_fecha_texto(d, mes, a):
    i = meses.index(mes)
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if d < dias_mes[i]:
        return (d + 1, mes, a)
    elif i < 11:
        return (1, meses[i + 1], a)
    else:
        return (1, meses[0], a + 1)

print(siguiente_fecha_texto(31, "Dic", 2023))

# Ejercicio 10
# Corregir valor en tupla
valores = ("189", "1930", "187", "210", "202")
valores = list(valores)
valores[1] = "193"
valores = tuple(valores)
print(valores)

# Ejercicio 11
salarios = [(12345678, 150000), (87654321, 80000), (11111111, 40000)]
SMVM = 80000
rango1 = rango2 = rango3 = rango4 = 0
for _, ingreso in salarios:
    if ingreso < SMVM:
        rango1 += 1
    elif ingreso < SMVM * 2:
        rango2 += 1
    elif ingreso < SMVM * 4:
        rango3 += 1
    else:
        rango4 += 1
print([("<SMVM", rango1), ("[SMVM,2x]", rango2), ("[2x,4x]", rango3), (">4x", rango4)])

# Ejercicio 12
frase = "la peluca de la abuela"
conteo = {}
for palabra in frase.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)

# Ejercicio 13a y 13b
notas = [("Perez", 8), ("Gonzalez", 10), ("Fernandez", 10)]
dict_alumnos = {}
dict_notas = {}
for alumno, nota in notas:
    dict_alumnos.setdefault(alumno, []).append(nota)
    dict_notas.setdefault(nota, []).append(alumno)
print(dict_alumnos)
print(dict_notas)

# Ejercicio 14
alumnos = {"Juan": [6, 9, 8], "Manuel": [9, 10, 9], "Martin": [5, 6, 7]}
for alumno, calificaciones in alumnos.items():
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"El promedio de {alumno} es {promedio:.2f}")

# Ejercicio 15
lista = [1, 2, 3, 4, 2, 5, 3]
repetidos = {}
for num in lista:
    repetidos[num] = repetidos.get(num, 0) + 1
for k, v in repetidos.items():
    if v > 1:
        print(f"Repetido: {k}")

# Ejercicio 16
nombres = ["Ana", "Luis", "Pedro"]
edades = [20, 25, 30]
diccionario = dict(zip(nombres, edades))
print(diccionario)

# Ejercicio 17
dosis_covid = {"123": 2, "456": 3, "789": 2}
tercera_dosis = [dni for dni, cantidad in dosis_covid.items() if cantidad == 2]
print("Recordatorios para tercera dosis:", tercera_dosis)

# Ejercicio 18
morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
         'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
         '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

codigo = ['.--.', '.-.', '---', '--.', '.-.', '.- --', '.- -', '.', '.', '-.-.']  # ejemplo
mensaje = ""
for seq in codigo:
    for letra, cod in morse.items():
        if cod == seq:
            mensaje += letra
            break
print("Mensaje descifrado:", mensaje)

# Ejercicio 19
com1 = {'legajo_11': [6, 7, 8]}
com2 = {'legajo_21': [5, 6, 7]}
com3 = {'legajo_31': [8, 9, 10]}
com4 = {'legajo_41': [3, 8, 9]}
prog_1 = {}
prog_1.update(com1)
prog_1.update(com2)
prog_1.update(com3)
prog_1.update(com4)
print(prog_1)
