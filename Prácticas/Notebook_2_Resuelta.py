# -*- coding: utf-8 -*-
"""
Práctica 2 - Estructuras de Control (Resuelta)
Tecnicatura Universitaria en Inteligencia Artificial
"""

def ejercicio_1():
    """Mayoría de edad"""
    print("\n--- Ejercicio 1 ---")
    edad = int(input("Ingrese su edad: "))
    print("Mayor de edad" if edad >= 18 else "Menor de edad")

def ejercicio_2():
    """Verificación de contraseña"""
    print("\n--- Ejercicio 2 ---")
    contraseña_correcta = 'pepito'
    contraseña = input("Ingrese la contraseña: ").lower()
    print("Acceso concedido" if contraseña == contraseña_correcta else "Acceso denegado")

def ejercicio_3():
    """Seguridad de contraseña"""
    print("\n--- Ejercicio 3 ---")
    contraseña = input("Ingrese una contraseña: ")
    especiales = '!@#$%^&*_.?'
    numeros = '0123456789'
    
    cumple_longitud = 8 < len(contraseña) < 16
    tiene_especial = any(c in contraseña for c in especiales)
    tiene_numero = any(c in contraseña for c in numeros)
    
    if cumple_longitud and tiene_especial and tiene_numero:
        print("✔ Contraseña segura")
    else:
        print("✖ Contraseña no cumple los requisitos")

def ejercicio_4():
    """Precio de entrada"""
    print("\n--- Ejercicio 4 ---")
    edad = int(input("Ingrese la edad del cliente: "))
    if edad < 4:
        precio = 0
    elif 4 <= edad <= 18:
        precio = 500
    else:
        precio = 800
    print(f"Precio de entrada: ${precio}")

def ejercicio_5():
    """Tipo de triángulo"""
    print("\n--- Ejercicio 5 ---")
    a = float(input("Ingrese lado 1: "))
    b = float(input("Ingrese lado 2: "))
    c = float(input("Ingrese lado 3: "))
    
    if a + b > c and a + c > b and b + c > a:  # Validación de triángulo
        if a == b == c:
            print("Equilátero")
        elif a == b or a == c or b == c:
            print("Isósceles")
        else:
            print("Escaleno")
    else:
        print("No es un triángulo válido")

def ejercicio_6():
    """Evaluación de notas"""
    print("\n--- Ejercicio 6 ---")
    nota = float(input("Ingrese la nota: "))
    if nota < 0 or nota > 10:
        print("Nota inválida")
    elif nota < 6:
        print("Desaprobado")
    else:
        print("Aprobado")

def ejercicio_7():
    """Descuentos por sede"""
    print("\n--- Ejercicio 7 ---")
    item = input("Item (Zapatillas/Remeras/Pantalones): ").capitalize()
    sede = input("Sede (Rosario/Funes/Roldan): ").capitalize()
    
    descuentos = {
        'Zapatillas': {'Rosario': 30, 'Funes': 40, 'Roldan': 25},
        'Remeras': {'Rosario': 20, 'Funes': 30, 'Roldan': 15},
        'Pantalones': {'Rosario': 10, 'Funes': 5, 'Roldan': 20}
    }
    
    if item in descuentos and sede in descuentos[item]:
        print(f"Descuento aplicado: {descuentos[item][sede]}%")
    else:
        print("Combinación item/sede no válida")

def ejercicio_8():
    """Descuentos acumulables"""
    print("\n--- Ejercicio 8 ---")
    item = input("Item: ").capitalize()
    sede = input("Sede: ").capitalize()
    dia = input("Día (Lunes/Miércoles/Jueves): ").capitalize()
    
    descuento_base = {
        'Zapatillas': {'Rosario': 30, 'Funes': 40, 'Roldan': 25},
        'Remeras': {'Rosario': 20, 'Funes': 30, 'Roldan': 15},
        'Pantalones': {'Rosario': 10, 'Funes': 5, 'Roldan': 20}
    }
    
    descuento_dia = {'Lunes': 10, 'Miércoles': 8, 'Jueves': 5}
    
    base = descuento_base.get(item, {}).get(sede, 0)
    adicional = descuento_dia.get(dia, 0)
    
    print(f"Descuento total: {base + adicional}%")

def main():
    """Menú principal"""
    print("PRÁCTICA 2 - ESTRUCTURAS DE CONTROL\n")
    ejercicios = {
        1: ejercicio_1,
        2: ejercicio_2,
        3: ejercicio_3,
        4: ejercicio_4,
        5: ejercicio_5,
        6: ejercicio_6,
        7: ejercicio_7,
        8: ejercicio_8
    }
    
    while True:
        print("\nSeleccione un ejercicio (1-8) o 0 para salir:")
        try:
            opcion = int(input("Opción: "))
            if opcion == 0:
                print("Saliendo...")
                break
            elif 1 <= opcion <= 8:
                ejercicios[opcion]()
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()