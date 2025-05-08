# Ejercicio 1: Imprimir los primeros 20 números naturales
print("Ejercicio 1:")
for i in range(1, 21):
    print(i, end=' ')
print("\n")

# Ejercicio 2: Tabla de multiplicar del 5
print("Ejercicio 2:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print()

# Ejercicio 3: Números de -10 a -1
print("Ejercicio 3:")
for i in range(-10, 0):
    print(i, end=' ')
print("\n")

# Ejercicio 4: Números divisibles por 5 y menores a 150
print("Ejercicio 4:")
numeros = [12, 75, 150, 180, 145, 525, 50]
for num in numeros:
    if num % 5 == 0 and num < 150:
        print(num, end=' ')
print("\n")

# Ejercicio 5: Primeros 10 números de Fibonacci
print("Ejercicio 5:")
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print("\n")

# Ejercicio 6: Factorial de 5
print("Ejercicio 6:")
factorial = 1
for i in range(1, 6):
    factorial *= i
print(factorial)
print()

# Ejercicio 7: Explicación de programas
print("Ejercicio 7:")
print("a. No imprime nada porque la lista está vacía")
print("b. Imprime 1, 2, 3 (valores de la lista) y luego 3 (último valor de i)")
print()

# Ejercicio 8a: Cuadrado primeros 10 números
print("Ejercicio 8a:")
for i in range(1, 11):
    print(f"{i}^2 = {i**2}")
print()

# Ejercicio 8b: Suma 0-100
print("Ejercicio 8b:")
suma = sum(range(101))
print(f"Suma: {suma}")
print()

# Ejercicio 8c: Suma y conteo de pares <100
print("Ejercicio 8c:")
suma_pares = sum(range(0, 100, 2))
count_pares = len(range(0, 100, 2))
print(f"Suma pares: {suma_pares}, Cantidad: {count_pares}")
print()

# Ejercicio 8d: Suma y conteo de impares <100
print("Ejercicio 8d:")
suma_impares = sum(range(1, 100, 2))
count_impares = len(range(1, 100, 2))
print(f"Suma impares: {suma_impares}, Cantidad: {count_impares}")
print()

# Ejercicio 9: Problema bucle infinito
print("Ejercicio 9:")
print("El problema es que x nunca cambia, por lo que x < 5 siempre es True")
print()

# Ejercicio 10: Suma hasta umbral
print("Ejercicio 10:")
def suma_hasta_umbral(umbral, valores):
    suma = 0
    for num in valores:
        suma += num
        if suma >= umbral:
            break
    return suma

valores = [3, 5, 4, 4, 5, 5, 3, 5, 2, 7]
print(f"Umbral 21: {suma_hasta_umbral(21, valores)}")
print(f"Umbral 34: {suma_hasta_umbral(34, valores)}")
print(f"Umbral 100: {suma_hasta_umbral(100, valores)}")
print()

# Ejercicio 11: Suma de pares con while y continue
print("Ejercicio 11:")
def suma_pares(valores):
    suma = 0
    i = 0
    while i < len(valores):
        if valores[i] % 2 != 0:
            i += 1
            continue
        suma += valores[i]
        i += 1
    return suma

valores1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores2 = [1, 4, 7, 10]
print(f"Suma 1: {suma_pares(valores1)}")
print(f"Suma 2: {suma_pares(valores2)}")
print()

# Ejercicio 12: Suma interactiva
print("Ejercicio 12:")
def suma_interactiva():
    while True:
        entrada = input("Ingrese un número o 'salir' para terminar: ")
        if entrada.lower() == 'salir':
            break
        try:
            n = int(entrada)
            suma = sum(range(n))
            print(f"La suma es {suma}")
        except ValueError:
            print("Entrada no válida")

# Descomentar para probar
# suma_interactiva()
print("(Función definida, descomentar para probar interactivamente)")
print()

# Ejercicio 13: Billetes y monumento
print("Ejercicio 13:")
def dias_para_sobrepasar():
    billete_grosor = 0.11 * 0.001
    altura_monumento = 70
    billetes_n = 1
    dia = 1
    
    while True:
        altura_pila = billetes_n * billete_grosor
        if altura_pila > altura_monumento:
            break
        billetes_n *= 2
        dia += 1
    
    return dia

print(f"Días necesarios: {dias_para_sobrepasar()}")
print()

# Ejercicio 14: Múltiplos
print("Ejercicio 14:")
def contar_multiplos_for(a, b):
    count = 0
    for i in range(a, b):
        if i % a == 0:
            count += 1
    return count

def contar_multiplos_while(a, b):
    count = 0
    multiplo = a
    while multiplo < b:
        count += 1
        multiplo += a
    return count

a, b = 3, 20
print(f"Con for: {contar_multiplos_for(a, b)}")
print(f"Con while: {contar_multiplos_while(a, b)}")
print("La versión while es más eficiente y clara")
print()

# Ejercicio 15: Verificación de contraseña
print("Ejercicio 15:")
def verificar_contraseña():
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == "Toto123":
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")

# Descomentar para probar
# verificar_contraseña()
print("(Función definida, descomentar para probar interactivamente)")
print()

# Ejercicio 15.1: Verificación con reintento
print("Ejercicio 15.1:")
def verificar_con_reintento():
    while True:
        contraseña = input("Ingrese la contraseña: ")
        if contraseña == "Toto123":
            print("Contraseña correcta")
            break
        print("Contraseña incorrecta, intente nuevamente")

# Descomentar para probar
# verificar_con_reintento()
print("(Función definida, descomentar para probar interactivamente)")
print()

# Ejercicio 15.2: Verificación con límite de intentos
print("Ejercicio 15.2:")
def verificar_con_intentos():
    intentos = 3
    while intentos > 0:
        contraseña = input("Ingrese la contraseña: ")
        if contraseña == "Toto123":
            print("Contraseña correcta")
            break
        intentos -= 1
        print(f"Contraseña incorrecta. Intentos restantes: {intentos}")
    
    if intentos == 0:
        print("Cuenta bloqueada")

# Descomentar para probar
# verificar_con_intentos()
print("(Función definida, descomentar para probar interactivamente)")