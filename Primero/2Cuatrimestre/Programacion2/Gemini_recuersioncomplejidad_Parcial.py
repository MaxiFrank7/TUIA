"""Ejercicio 1: Recursión y Potencia
Implemente una función recursiva llamada potencia_rec que reciba como parámetros dos números enteros, una base b y un exponente n (con n >= 0), 
y que calcule b^n. Para su implementación, considere las siguientes propiedades matemáticas:
    b^n=1 si n=0
    b^n=(b^n/2)^2 si n es par
    b^n=b*b^(n-1) si n es impar
Escriba, además, una función iterativa potencia_it que resuelva el mismo problema."""
def potencia_rec(b:int, n:int)->int:
    if n==0:
        return 1
    if n%2!=0:
        return b*potencia_rec(b,n-1)
    else:
        return b*potencia_rec(b,n//2)
print(potencia_rec(2,3))
print(potencia_rec(2,2))

def potencia_it(b:int, n:int)->int:
    resultado=1
    for _ in range(n):
        resultado*=b
    return resultado
print(potencia_it(2,3))
print(potencia_it(2,2))

"""1. Cálculo de Productoria
Implemente una función recursiva llamada productoria_rec que reciba como parámetro una lista de números enteros y devuelva el producto de todos sus elementos. Si la lista está vacía, debe devolver 1.

Escriba, además, una función iterativa productoria_it que sea equivalente.

Justificación de diseño: Este ejercicio evalúa la capacidad de traducir un concepto matemático simple a dos paradigmas de programación distintos, 
un desafío similar al de contar_ocurrencias en los parciales originales. La lógica se deriva directamente del concepto de caso base y caso recursivo explicado en los apuntes de recursión."""
def productoria_rec(lista:list[int])->int:
    if not lista:
        return 1
    return lista[0]*productoria_rec(lista[1:])
print(productoria_rec([1,2,3,4]))
print(productoria_rec([]))

def productoria_it(lista:list[int])->int:
    if not lista:
        return 1
    total=1
    for num in lista:
        total*=num
    return total
print(productoria_it([1,2,3,4]))
print(productoria_it([]))

"""Ejercicio 2: Complejidad Temporal
Analice el siguiente algoritmo y determine su orden de complejidad temporal (notación O grande). Explique detalladamente el razonamiento utilizado 
para llegar a esa conclusión, contando las operaciones más relevantes que realiza la función."""

def procesar_datos1(matriz: list[list[int]]) -> int:
    """
    Procesa una matriz cuadrada (n x n).
    """
    n = len(matriz)                 #1
    suma_total = 0                       #1
    # Bucle 1
    for i in range(n):                   #n
        print(f"Procesando fila {i}")    #1
        suma_total += matriz[i][i]       #2 --->Total=3n=O(n)
    # Bucle 2
    for i in range(n):                   #n
        for j in range(i, n):            #n-i
            print(f"Analizando elemento ({i}, {j})") #1
            suma_total += matriz[i][j] * 2          #3--->Total bucle= n*n-i*(4)=n*(4n-4i)=4n2-4ni
    return suma_total                   #1
#Complejidad O(n2)

"""2. Análisis de Complejidad Temporal
Indique el orden de complejidad temporal del siguiente algoritmo. Explique lo más detalladamente posible cómo obtiene esa complejidad, 
basándose en el análisis de sus bucles y operaciones."""
def procesar_datos2(datos: list[int]) -> int:
    n = len(datos)                  #1
    total = 0                            #1
    # Bucle 1
    for i in range(n):                  #n
        for j in range(n):              #n
            total += datos[i] * datos[j] #1 ---> Total bucle: n*n*1=n2 O(n2)
    # Bucle 2
    for k in range(n):                  #n
        print(f"Procesando elemento {k}") #1 ---> Total bucle=n O(n)
    # Bucle 3
    for _ in range(10):                 #10
        total -= 1                      #1 ---> Total bucle=10
    return total                        #1
#Complejidad O(n2), la mas importante la del bucle1
   
"""Ejercicio 1: Suma de Dígitos
Implemente una función recursiva llamada sumar_digitos_rec que reciba como parámetro un número entero no negativo 
y devuelva la suma de sus dígitos. Por ejemplo, sumar_digitos_rec(123) debería devolver 6 (porque 1+2+3=6).

Escriba, además, una función iterativa sumar_digitos_it que resuelva el mismo problema.
Ayuda: Para la versión recursiva, piense en un caso base (un número de un solo dígito) y en cómo reducir el problema 
en cada llamada (por ejemplo, utilizando el cociente // y el resto % de la división por 10)."""

def sumar_digitos_rec(n:int)->int:
    if 0<=n<10:
        return n
    return sumar_digitos_rec(n//10)+(n%10)
def sumar_digitos_it(n:int)->int:
    suma=0
    while n>0:
        suma+=n%10
        n=n//10
    return suma
numero = 9524
print(f"Recursivo: La suma de los dígitos de {numero} es {sumar_digitos_rec(numero)}") # Resultado: 20
print(f"Iterativo: La suma de los dígitos de {numero} es {sumar_digitos_it(numero)}")   # Resultado: 20

"""Ejercicio 2: Complejidad Temporal
Indique el orden de complejidad temporal (notación O grande) del siguiente algoritmo. Explique detalladamente su razonamiento, 
identificando las operaciones más significativas y cómo su número escala con el tamaño de la entrada n"""

def algoritmo_misterioso(n: int) -> None:
    """
    Realiza una serie de operaciones basadas en el entero n.
    """
    # Bucle 1
    for i in range(n):                  #n
        # Bucle interno con un número fijo de iteraciones
        for j in range(10):             #10
            print(f"Procesando ({i}, {j})") #1 --->Total bucle:n*10=O(n)
    # Bucle 2
    for k in range(n):                  #n
        print(f"Paso final {k}")        #1  --->Total bucle:n O(n)
 #Total O(n)


"""Ejercicio 1: Búsqueda del Máximo Elemento
Implemente una función recursiva llamada encontrar_maximo_rec que reciba como parámetro una lista de números enteros y devuelva el número más grande de la lista.
 Puede asumir que la lista no estará vacía.

Escriba, además, una función iterativa encontrar_maximo_it que resuelva el mismo problema."""

def encontrar_maximo_rec(lista:list[int])->int:
    if len(lista)==1:
        return lista[0]
    if lista[0]> encontrar_maximo_rec(lista[1:]):
        return lista[0]
    else:
        return encontrar_maximo_rec(lista[1:])

def encontrar_maximo_it(lista:list[int])->int:
    max=lista[0]
    for num in lista[1:]:
        if num>max:
            max=num
    return max
numeros = [12, 45, 8, 99, 23, 56]
print(f"Recursivo: El máximo es {encontrar_maximo_rec(numeros)}") # Resultado: 99
print(f"Iterativo: El máximo es {encontrar_maximo_it(numeros)}")   # Resultado: 99

"""Ejercicio 2: Complejidad Temporal
Determine el orden de complejidad temporal (notación O grande) del siguiente algoritmo. Justifique su respuesta explicando detalladamente cómo la 
cantidad de operaciones escala en función del tamaño de la lista de entrada, n"""

def calculo_complejo(lista: list[int]) -> int:
    """
    Realiza un cálculo sobre una lista de enteros.
    """
    n = len(lista)  #1
    resultado = 0        #1
    for i in range(n):   #n
        for j in range(i, n): #n-i  si i=0->n i=1 -> n-1  i=2 -> n-2 
            # Esta operación se considera de tiempo constante O(1)
            resultado += lista[i] * lista[j] #O(1)--> Total bucle es n*(n+1)/2=n2/2+n/2
    return resultado #1
#Total= 1+1+n2/2+n/2+1=3+n2/2+n/2->O(n2)

"""Ejercicio 1: Inversión de Cadena
Implemente una función recursiva llamada invertir_cadena_rec que reciba como parámetro una cadena de texto y devuelva la cadena invertida. 
Por ejemplo, invertir_cadena_rec("hola") debería devolver "aloh".

Escriba, además, una función iterativa invertir_cadena_it que resuelva el mismo problema.

Ayuda: Para la versión recursiva, piense que invertir una cadena es igual a tomar el último carácter y concatenarlo con la inversión del resto de la cadena. 
El caso base es una cadena vacía o de un solo carácter."""
def invertir_cadena_rec(cadena:str)->str:
    if len(cadena)==0:
        return ""
    if len(cadena)==1:
        return cadena
    return invertir_cadena_rec(cadena[1:])+cadena[0]

def invertir_cadena_it(cadena:str)->str:
    resultado=""
    for letra in cadena:
        resultado=letra+resultado
    return resultado
texto = "python"
print(f'Recursivo: Invertir "{texto}" -> "{invertir_cadena_rec(texto)}"') # Resultado: "nohtyp"
print(f'Iterativo: Invertir "{texto}" -> "{invertir_cadena_it(texto)}"')   # Resultado: "nohtyp"

"""Ejercicio 2: Complejidad Temporal
Determine el orden de complejidad temporal (notación O grande) del siguiente algoritmo. Justifique su respuesta 
explicando detalladamente cómo la cantidad de operaciones escala en función del tamaño de la entrada, n"""

def algoritmo_conteo(n: int) -> int:
    """
    Realiza un conteo basado en el entero n.
    """
    contador = 0             #1
    i = n               #1
    while i > 1:             #n/2^i
        contador += 1
        i = i // 2  # División entera
        print(f"Valor actual de i: {i}")
    return contador

"""Ejercicio 1: Verificación de Palíndromo
Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda (ej: "radar", "neuquen").

Implemente una función recursiva llamada es_palindromo_rec que reciba una cadena de texto y devuelva True si es un palíndromo y False en caso contrario.

Escriba, además, una función iterativa es_palindromo_it que resuelva el mismo problema.

Ayuda: Para la versión recursiva, una cadena es un palíndromo si su primer y último carácter son iguales, y la subcadena que queda 
en el medio también es un palíndromo. El caso base es una cadena con 0 o 1 carácter."""

def es_palindromo_rec(cadena:str)->bool:
    if len(cadena)<2:
        return True
    if cadena[0]==cadena[-1]:
        return es_palindromo_rec(cadena[1:-1])
    return False

def es_palindromo_it(cadena:str)->bool:
    inicio=0
    fin=len(cadena)-1
    while inicio<fin:
        if cadena[inicio] != cadena[fin]:
            return False
        inicio+=1
        fin-=1
    return True
        

palabra1 = "neuquen"
palabra2 = "casa"
print(f'Recursivo: "{palabra1}" es palíndromo? {es_palindromo_rec(palabra1)}') # Resultado: True
print(f'Iterativo: "{palabra1}" es palíndromo? {es_palindromo_it(palabra1)}')   # Resultado: True
print(f'Recursivo: "{palabra2}" es palíndromo? {es_palindromo_rec(palabra2)}') # Resultado: False
print(f'Iterativo: "{palabra2}" es palíndromo? {es_palindromo_it(palabra2)}')   # Resultado: False


"""Ejercicio 2: Complejidad Temporal
Determine el orden de complejidad temporal (notación O grande) del siguiente algoritmo. Justifique su respuesta explicando detalladamente 
cómo la cantidad de operaciones escala en función del tamaño de la entrada, n"""

def procesar_cubo_de_datos(n: int) -> int:
    """
    Procesa un cubo de datos imaginario de dimensiones n x n x n.
    """
    operaciones = 0                         #1
    # Bucle 1: itera sobre la altura
    for i in range(n):                      #n
        # Bucle 2: itera sobre la anchura
        for j in range(n):                  #n
            # Bucle 3: itera sobre la profundidad
            for k in range(n):              #n
                operaciones += 1 # Operación de tiempo constante #2        
    return operaciones #1
#Total 1+n*n*n*2+1=2+2n3=> O(n3)

"""Ejercicio 1: Suma de Elementos de una Lista
Implemente una función recursiva llamada suma_lista_rec que reciba como parámetro una lista de números enteros y devuelva la suma de todos sus elementos.

Escriba, además, una función iterativa suma_lista_it que resuelva el mismo problema.

Ayuda: Para la versión recursiva, considere que la suma de una lista es igual al primer elemento más la 
suma del resto de la lista. El caso base es una lista vacía"""
def suma_lista_rec(lista:list[int])->int:
    if not lista:
        return 0
    if len(lista)==1:
        return lista[0]
    return lista[0]+suma_lista_rec(lista[1:])
print(suma_lista_rec([1,3,6,8]))

def suma_lista_it(lista:list[int])->int:
    suma=0
    for elemento in lista:
        suma+=elemento
    return suma
print(suma_lista_it([1,3,6,8]))

"""Ejercicio 2: Complejidad Temporal
Determine el orden de complejidad temporal (notación O grande) del siguiente algoritmo. Justifique su respuesta explicando 
detalladamente cómo la cantidad de operaciones escala en función del tamaño de la lista de entrada, n."""
def analizar_lista(lista: list[int]) -> None:
    """
    Realiza dos recorridos separados sobre una lista.
    """
    n = len(lista)
    # Primer recorrido
    print("Iniciando primer análisis...")
    for i in range(n):
        print(f"Elemento {i}: {lista[i]}")
    # Segundo recorrido
    print("Iniciando segundo análisis...")
    for j in range(n):
        print(f"Repasando elemento {j}: {lista[j]}")


"""Ejercicio 1: Conteo de Ocurrencias
Implemente una función recursiva llamada contar_ocurrencias_rec que reciba como parámetros una lista de números enteros y un número valor, 
y que cuente cuántas veces aparece ese valor específico en la lista. 

Escriba, además, una función iterativa contar_ocurrencias_it equivalente. 

Ayuda: Para la versión recursiva, verifique si el primer elemento de la lista es igual al valor. El resultado será 1 (si es igual) o 0 
(si es diferente), más el conteo de ocurrencias en el resto de la lista. El caso base es una lista vacía."""

def contar_ocurriencias_rec(lista:list[int], valor:int)->int:
    if not lista:
        return 0
    if lista[0]==valor:
        return 1+contar_ocurriencias_rec(lista[1:],valor)
    else:
        return contar_ocurriencias_rec(lista[1:],valor)
    
def contar_ocurrencias_it(lista:list[int],valor:int)->int:
    suma=0
    for num in lista:
        if num == valor:
            


numeros = [1, 5, 2, 5, 8, 5, 3]
valor_a_buscar = 5
print(f"Recursivo: El valor {valor_a_buscar} aparece {contar_ocurriencias_rec(numeros, valor_a_buscar)} veces.") # Resultado: 3
print(f"Iterativo: El valor {valor_a_buscar} aparece {contar_ocurrencias_it(numeros, valor_a_buscar)} veces.")   # Resultado: 3
    
"""Ejercicio 1: Factorial de un NúmeroImplemente una función recursiva llamada factorial_rec que reciba como parámetro un número entero no negativo n y devuelva su factorial ($n!$). 
El factorial de un número es el producto de todos los enteros positivos desde 1 hasta ese número. Por definición, el factorial de 0 es 1 ($0! = 1$).
Escriba, además, una función iterativa factorial_it equivalente.Ayuda: Para la versión recursiva, recuerde que $n! = n \times (n-1)!$. El caso base es $0! = 1$."""
def factorial_rec(n:int)->int:
    if n<2:
        return 1
    return factorial_rec(n-1)
def factorial_it(n:int)->int:
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

numero = 5
print(f"Recursivo: El factorial de {numero} es {factorial_rec(numero)}") # Resultado: 120
print(f"Iterativo: El factorial de {numero} es {factorial_it(numero)}")  # Resultado: 120
