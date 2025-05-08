# -*- coding: utf-8 -*-
"""
Práctica 4 - Funciones y estructuras de datos
Contiene las soluciones a los 9 ejercicios propuestos.
"""

import math
import random
from typing import Union, Tuple, List

# --- Ejercicio 1 ---
def determinar_signo_zodiacal(fecha: str) -> str:
    """
    Determina el signo zodiacal basado en la fecha de nacimiento (DD/MM/YYYY).
    """
    dia, mes, _ = map(int, fecha.split('/'))

    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    else:
        return "Capricornio"

# --- Ejercicio 2 ---
def ordenar_cadena(cadena: str) -> Tuple[str, str]:
    """
    Ordena una cadena de caracteres de forma ascendente y descendente.
    Devuelve una tupla con (ascendente, descendente).
    """
    ascendente = ''.join(sorted(cadena))
    descendente = ''.join(sorted(cadena, reverse=True))
    return (ascendente, descendente)

# --- Ejercicio 3 ---
def potencia_max_min(a: float, b: float, c: float) -> float:
    """
    Calcula la potencia del número más grande elevado al más pequeño.
    """
    maximo = max(a, b, c)
    minimo = min(a, b, c)
    return math.pow(maximo, minimo)

# --- Ejercicio 4 ---
def juego_adivinanza():
    """
    Juego de adivinanza donde el usuario debe adivinar un número aleatorio entre 1 y 10.
    """
    numero_secreto = random.randint(1, 10)
    intentos = 0
    adivinado = False

    while not adivinado:
        intento = int(input("Adivina el número (entre 1 y 10): "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Ganaste! El número era {numero_secreto}. Intentos: {intentos}")
            adivinado = True
        else:
            print("Intenta de nuevo.")

# --- Ejercicio 5 ---
def suma(a: float, b: float) -> float:
    """Calcula la suma de dos números."""
    return a + b

def resta(a: float, b: float) -> float:
    """Calcula la resta de dos números."""
    return a - b

# --- Ejercicio 6 ---
def longitud_cadena(cadena: str) -> int:
    """
    Calcula la longitud de una cadena sin usar la función len.
    """
    contador = 0
    for _ in cadena:
        contador += 1
    return contador

# --- Ejercicio 7 ---
def contar_letra(frase: str, letra: str) -> int:
    """
    Cuenta cuántas veces aparece una letra en una frase.
    """
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    return contador

# --- Ejercicio 8 ---
def es_primo(numero: int) -> bool:
    """
    Determina si un número es primo.
    """
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos_menores_que_n(n: int) -> List[int]:
    """
    Devuelve una lista con todos los números primos menores que n.
    """
    primos = []
    for numero in range(2, n):
        if es_primo(numero):
            primos.append(numero)
    return primos

# --- Ejercicio 9 ---
def division(a: float, b: float) -> Union[float, str]:
    """Realiza la división a/b con manejo de división por cero."""
    if b == 0:
        return "Error: División por cero."
    return a / b

def multiplicacion(a: float, b: float) -> float:
    """Realiza la multiplicación a*b."""
    return a * b

def factorial(num: int) -> Union[int, str]:
    """Calcula el factorial de un número."""
    if num < 0:
        return "Error: Factorial de un número negativo no existe."
    elif num == 0:
        return 1
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

def calculadora():
    """
    Menú de calculadora con las operaciones básicas y factorial.
    """
    while True:
        print("\nMenú Calculadora:")
        print("1. Suma")
        print("2. Resta")
        print("3. División")
        print("4. Multiplicación")
        print("5. Factorial")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo de la calculadora...")
            break
        elif opcion == "5":
            num = int(input("Ingrese un número para calcular su factorial: "))
            print(f"Factorial de {num}: {factorial(num)}")
        elif opcion in ["1", "2", "3", "4"]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            if opcion == "1":
                print(f"Resultado: {suma(num1, num2)}")
            elif opcion == "2":
                print(f"Resultado: {resta(num1, num2)}")
            elif opcion == "3":
                print(f"Resultado: {division(num1, num2)}")
            elif opcion == "4":
                print(f"Resultado: {multiplicacion(num1, num2)}")
        else:
            print("Opción no válida. Intente de nuevo.")

# --- Función principal para ejecutar los ejercicios ---
def main():
    print("PRÁCTICA 4 - FUNCIONES Y ESTRUCTURAS DE DATOS")
    
    while True:
        print("\nSeleccione un ejercicio (1-9) o 0 para salir:")
        print("1. Signo zodiacal")
        print("2. Ordenar cadena")
        print("3. Potencia del máximo al mínimo")
        print("4. Juego de adivinanza")
        print("5. Suma de dos números")
        print("6. Longitud de cadena")
        print("7. Contar letra en frase")
        print("8. Números primos")
        print("9. Calculadora")
        print("0. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "0":
            print("¡Hasta luego!")
            break
            
        elif opcion == "1":
            fecha = input("Ingrese su fecha de nacimiento (DD/MM/YYYY): ")
            print(f"Su signo zodiacal es: {determinar_signo_zodiacal(fecha)}")
            
        elif opcion == "2":
            cadena = input("Ingrese una cadena de caracteres: ")
            asc, desc = ordenar_cadena(cadena)
            print(f"Cadena ordenada ascendente: {asc}")
            print(f"Cadena ordenada descendente: {desc}")
            
        elif opcion == "3":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            c = float(input("Ingrese el tercer número: "))
            print(f"Resultado: {potencia_max_min(a, b, c)}")
            
        elif opcion == "4":
            juego_adivinanza()
            
        elif opcion == "5":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"La suma es: {suma(a, b)}")
            
        elif opcion == "6":
            cadena = input("Ingrese una cadena de texto: ")
            print(f"La longitud de la cadena es: {longitud_cadena(cadena)}")
            
        elif opcion == "7":
            frase = input("Ingrese una frase: ")
            letra = input("Ingrese la letra a buscar: ")
            print(f"La letra '{letra}' aparece {contar_letra(frase, letra)} veces.")
            
        elif opcion == "8":
            print("a. Verificar si un número es primo")
            print("b. Mostrar primos menores que n")
            subopcion = input("Elija una opción (a/b): ")
            
            if subopcion.lower() == "a":
                num = int(input("Ingrese un número: "))
                if es_primo(num):
                    print(f"{num} es un número primo.")
                else:
                    print(f"{num} no es un número primo.")
                    
            elif subopcion.lower() == "b":
                n = int(input("Ingrese un número: "))
                print(f"Números primos menores que {n}:")
                print(primos_menores_que_n(n))
                
        elif opcion == "9":
            calculadora()
            
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()