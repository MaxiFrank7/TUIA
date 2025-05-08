# -*- coding: utf-8 -*-
"""
PRÁCTICA 1 - OPERADORES (RESUELTA)
Contiene todos los ejercicios de la Práctica 1 en un solo script Python.
"""

def mostrar_separador(ejercicio):
    print(f"\n{'='*50}\nEjercicio {ejercicio}\n{'='*50}")

# =============================================================================
# Ejercicio 1: Prueba de Expresiones
# =============================================================================
mostrar_separador(1)
print("1a:", 0)
print("1b:", 1.5 * 0)
print("1c:", 11 / 2)
print("1d:", 11 // 2)
print("1e:", 11.0 // 2.0)
print("1f:", 2 ** 2)
print("1g:", "a" + "b")
print("1h:", "a" * 0)

# =============================================================================
# Ejercicio 2: Predicción y Verificación
# =============================================================================
mostrar_separador(2)
# print("2a:", 1 / 0)  # Descomentar para ver el error
print("2b:", 10 / 2 // 1 ** 5)
print("2c:", "hola" + ' ' + "mundo" + '!')
print("2d:", "hola" + (' ' + "mundo") * 0)

# =============================================================================
# Ejercicio 3: Comparación con ==
# =============================================================================
mostrar_separador(3)
a, b = 3, 3.0
c = (0.1 + 0.2) * 10
d, e = 22 / 7, 22 // 7
print("3a:", a == b)
print("3b:", c == 3.0)
print("3c:", d == e)

# =============================================================================
# Ejercicio 4: Diferencias y Similitudes
# =============================================================================
mostrar_separador(4)
print("4a.1:", 10 + 5, type(10 + 5))
print("4a.2:", 10 + 5.0, type(10 + 5.0))
print("4a.3:", 10 + 5., type(10 + 5.))
print("4b.1:", 11 / 2, type(11 / 2))
print("4b.2:", 11 // 2, type(11 // 2))
print("4b.3:", 11.0 // 2, type(11.0 // 2))

# =============================================================================
# Ejercicio 5: Operadores Unarios
# =============================================================================
mostrar_separador(5)
print("5a:", +1)
print("5b:", -1)
print("5c:", +-1)
print("5d:", -1)

# =============================================================================
# Ejercicio 6: Precedencia y Paréntesis
# =============================================================================
mostrar_separador(6)
print("6a:", 3 * 5 - 7 * 4 / 14 + 3 / 1)
print("6b:", 2 ** 1 + 3 / 5 // 4)

# =============================================================================
# Ejercicio 7: Evaluación de Expresiones Booleanas
# =============================================================================
mostrar_separador(7)
print("7a:", (4 >= 40 and 8 <= 10) or (2 < 20 or 10 > 100))
print("7b:", 4 <= 10 or (2/0 == 1))  # True (short-circuit)
print("7c:", (8 >= 10 or 4 <= 8) and (3 != 10 or 10 >= 4))
print("7d:", (50 > 49 and 7 == 5) or (15 <= 14 or 10 > 100))
print("7e:", not(not(10 >= 8) and 1 > 3) or (2 != 3 and 2 < 8))
print("7f:", (4 > 2 or 7 > 6) and not(3 < 6 or 2 > 0))
print("7g:", not(0))
print("7h:", not(1))
print("7i:", not(8))
print("7j:", not('a'))
print("7k:", not([]))

# =============================================================================
# Ejercicio 8: Corrección de Código
# =============================================================================
mostrar_separador(8)
# Versión corregida del 8a
saludo = " Hola "
destino = " Mundo "
puntuacion = " ! "
print("8a:", saludo + destino + puntuacion)

# 8b (original correcto)
cateto1, cateto2 = 3, 4
hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5
del cateto1, cateto2
print("8b:", hipotenusa)

# Versión corregida del 8c
tengo_hambre = False
del tengo_hambre
tengo_hambre = True
print("8c:", tengo_hambre)

# =============================================================================
# Ejercicio 9: Slicing en URL
# =============================================================================
mostrar_separador(9)
sitio_web = "https://fceia.unr.edu.ar/noticias-fceia"
protocolo = sitio_web[:8]
dominio = sitio_web[8:25]
ruta = sitio_web[25:]
print("9 - Protocolo:", protocolo)
print("9 - Dominio:", dominio)
print("9 - Ruta:", ruta)

# =============================================================================
# Ejercicio 10: Números Pares con Slicing
# =============================================================================
mostrar_separador(10)
numeros = "0123456789"
pares = numeros[::2]
print("10:", pares)

# =============================================================================
# Ejercicio 11: Traducción a Booleanos
# =============================================================================
mostrar_separador(11)
print("11a:", len("Hola, mundo") == 14)
print("11b:", 5**2 == 625**0.5)
print("11c:", 3.25*2 > 6 and 3.25*2 < 7)
print("11d:", (22/7 > 3) and (2+2 == 5))
# print("11e:", 10 > 5 or (0/0 == 0))  # Error
# print("11f:", len("Python") == 5 and (1+"1" == 2))  # Error

# =============================================================================
# Ejercicio 12: Algoritmos
# =============================================================================
mostrar_separador(12)
# 12a - Rectángulo
base, altura = 10, 5
print("12a - Área:", base * altura)
print("12a - Perímetro:", 2*(base + altura))

# 12b - Promedio
notas = [8, 7, 9]
print("12b - Promedio:", sum(notas)/len(notas))

# 12c - Distancia
x1, y1, x2, y2 = 0, 0, 3, 4
distancia = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("12c - Distancia:", distancia)

# =============================================================================
# Ejercicio 13: Pregunta al Usuario
# =============================================================================
mostrar_separador(13)
respuesta = "soleado"  # Simulamos input para automatizar
print("13: El día está", respuesta)

# =============================================================================
# Ejercicio 14: Área y Perímetro de Círculo
# =============================================================================
mostrar_separador(14)
import math
radio = 5
print("14 - Área:", math.pi * radio**2)
print("14 - Perímetro:", 2 * math.pi * radio)

# =============================================================================
# Ejercicio 15: Precio Promedio
# =============================================================================
mostrar_separador(15)
precios = [100, 200, 300]
print("15 - Precio promedio:", sum(precios)/len(precios))

# =============================================================================
# Ejercicio 16: Conversión de Metros
# =============================================================================
mostrar_separador(16)
metros = 2
print("16 - Centímetros:", metros*100)
print("16 - Milímetros:", metros*1000)
print("16 - Pulgadas:", metros*100/2.54)

# =============================================================================
# Ejercicio 17: Tiempo a Segundos
# =============================================================================
mostrar_separador(17)
h, m, s = 2, 30, 15
print("17 - Total segundos:", h*3600 + m*60 + s)

# =============================================================================
# Ejercicio 18: Segundos a Horas:Minutos:Segundos
# =============================================================================
mostrar_separador(18)
segundos = 9015
h = segundos // 3600
resto = segundos % 3600
m = resto // 60
s = resto % 60
print("18 - Formato hh:mm:ss:", f"{h:02d}:{m:02d}:{s:02d}")

# =============================================================================
# Ejercicio 19: Consumo de Combustible
# =============================================================================
mostrar_separador(19)
litros, km = 50, 400
print("19 - Consumo:", km/litros, "km/lt")

# =============================================================================
# Ejercicio 20: Intercambio de Variables
# =============================================================================
mostrar_separador(20)
a, b = 9, 3
print("20 - Antes: a=", a, "b=", b)
a, b = b, a
print("20 - Después: a=", a, "b=", b)

# =============================================================================
# Ejercicio 21: Intercambio de Tres Variables
# =============================================================================
mostrar_separador(21)
a, b, c = 9, 3, 5
print("21 - Antes: a=", a, "b=", b, "c=", c)
a, b, c = b, c, a
print("21 - Después: a=", a, "b=", b, "c=", c)

# =============================================================================
# Ejercicio 22: Operaciones Aritméticas
# =============================================================================
mostrar_separador(22)
num1, num2 = 10, 5
print("22 - Suma:", num1 + num2)
print("22 - Resta:", num1 - num2)
print("22 - Multiplicación:", num1 * num2)
print("22 - División:", num1 / num2)

# =============================================================================
# Ejercicio 23: Porcentaje de Niños/Niñas
# =============================================================================
mostrar_separador(23)
ninos, ninas = 20, 30
total = ninos + ninas
print("23 - % Niños:", (ninos/total)*100)
print("23 - % Niñas:", (ninas/total)*100)

# =============================================================================
# Ejercicio 24: Conversión de Días
# =============================================================================
mostrar_separador(24)
dias = 2
print("24 - Horas:", dias*24)
print("24 - Minutos:", dias*24*60)
print("24 - Segundos:", dias*24*60*60)

# =============================================================================
# Ejercicio 25: Problemas Varios
# =============================================================================
mostrar_separador(25)
# 25a - Temperatura promedio
temp1, temp2 = 20.5, 22.3
print("25a - Temp promedio:", (temp1 + temp2)/2)

# 25b - Tiempo para decir nombres
personas = 10
print("25b - Tiempo total:", personas*(personas-1)*4.5, "segundos")

# 25c - Comparación de nombres
nombre1, nombre2 = "María", "María"
print("25c - Misma longitud:", len(nombre1) == len(nombre2))
print("25c - Iguales:", nombre1 == nombre2)

print("\n¡Todos los ejercicios completados! 🎉")