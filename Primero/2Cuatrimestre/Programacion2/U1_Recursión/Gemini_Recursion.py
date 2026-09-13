"""Ejercicio 1: Suma de Pares en una Lista
Escribe una función recursiva suma_pares(lista) que reciba una lista de números enteros 
y devuelva la suma de solo aquellos números que son pares."""
def suma_pares(lista:list)->int:
    if len(lista)==0:
        return 0
    if lista[0]%2==0:
        return lista[0]+suma_pares(lista[1:])
    else:
        return suma_pares(lista[1:])
    
# --- Pruebas ---
print(f"Suma de [1, 2, 3, 4, 5, 6]: {suma_pares([1, 2, 3, 4, 5, 6])}")
print(f"Suma de [10, 1, 1, 1, 10]: {suma_pares([10, 1, 1, 1, 10])}")
print(f"Suma de []: {suma_pares([])}")

"""Ejercicio 2: Conversión de Decimal a Binario
Escribe una función recursiva decimal_a_binario(n) que reciba un número entero n (mayor o igual a 0) 
y devuelva una cadena de texto (str) con su representación en formato binario."""
def decimal_a_binario(n:int)->str:
    if n<0:
        return f'Ingrese un valor mayor a 0'
    if n<2:
        return str(n)
    return decimal_a_binario(n//2)+str(n%2)

# --- Pruebas ---
print(f"Binario de 13: {decimal_a_binario(13)}")
print(f"Binario de 0: {decimal_a_binario(0)}")
print(f"Binario de 25: {decimal_a_binario(25)}")

"""Ejercicio 3: Aplanar una Lista Anidada
Escribe una función recursiva aplanar_lista(lista_anidada) que reciba una lista que puede contener tanto números enteros como otras listas, 
y devuelva una única lista "plana" con todos los números."""
def aplanar_lista(lista:list)->list[int]:
    if len(lista)==0:
        return []
    if isinstance(lista[0], list):
        return aplanar_lista(lista[0])+aplanar_lista(lista[1:])
    if isinstance(lista[0], int):
        return [lista[0]]+aplanar_lista(lista[1:])
    
# --- Pruebas ---
print(f"Aplanar [1, [2, 3], 4, [5, [6]]]: {aplanar_lista([1, [2, 3], 4, [5, [6]]])}")
print(f"Aplanar [[1, 1], [1, 1]]: {aplanar_lista([[1, 1], [1, 1]])}")
print(f"Aplanar [10, 20, 30]: {aplanar_lista([10, 20, 30])}")

"""Ejercicio 4: Comprobar si una lista está ordenada
Escribe una función recursiva esta_ordenada(lista) que reciba una lista de números y devuelva True si los elementos están ordenados 
de menor a mayor, y False en caso contrario. Una lista vacía o con un solo elemento se considera ordenada."""

def esta_ordenada(lista:list)->bool:
    if not lista or len(lista)==1:
        return True
    if lista[0]<=lista[1] and esta_ordenada(lista[1:]):
        return True
    return False

# --- Pruebas ---
print(esta_ordenada([1, 2, 3, 4, 5]))
print(esta_ordenada([1, 3, 2, 5]))
print(esta_ordenada([10]))
print(esta_ordenada([]))

"""Ejercicio 6: Eliminar Ocurrencias
Escribe una función recursiva eliminar_ocurrencias(lista, elemento) que reciba una lista y un elemento, 
y devuelva una nueva lista que sea igual a la original pero sin ninguna aparición del elemento especificado."""
def eliminar_ocurrencias(lista:list, elemento:int)->list:
    if not lista:
        return []
    if lista[0]==elemento:
        return eliminar_ocurrencias(lista[1:], elemento)
    else:
        return [lista[0]]+ eliminar_ocurrencias(lista[1:], elemento)
    
print(eliminar_ocurrencias([1, 5, 2, 5, 3, 5], 5))
#[1, 2, 3]
print(eliminar_ocurrencias(['a', 'b', 'c', 'a'], 'a'))
#['b', 'c']
print(eliminar_ocurrencias([1, 2, 3], 4))
#[1, 2, 3]

"""Ejercicio 7: Suma de Dígitos
Escribe una función suma_digitos(n) que reciba un número entero no negativo y devuelva la suma de todos sus dígitos."""
def suma_digitos(n:int)->int:
    if 0<=n<=9:
        return n
    return n%10+suma_digitos(n//10)
print(suma_digitos(123))

"""Ejercicio 8: Palíndromo
Escribe una función es_palindromo(texto) que determine si una cadena de texto es un palíndromo 
(se lee igual de izquierda a derecha que de derecha a izquierda). La función debe ignorar mayúsculas y minúsculas."""
def es_palindromo(texto:str)->bool:
    texto=texto.lower()
    if len(texto)==0 or len(texto)==1:
        return True
    if texto[0]==texto[-1]:
        return es_palindromo(texto[1:-1])
    else:
        return False
print(es_palindromo('neuquen'))
print(es_palindromo('zapatilla'))
print(es_palindromo('a'))

"""Ejercicio 9: Máximo Común Divisor (MCD)
Escribe una función mcd(a, b) que calcule el Máximo Común Divisor de dos números enteros a y b utilizando el Algoritmo de Euclides.

El MCD(a, 0) es a.

De lo contrario, el MCD(a, b) es el MCD(b, a % b)."""
def mcd(a:int,b:int)->int:
    if b==0:
        return a
    else:
        return mcd(b,a%b)
print(mcd(48, 18))
#6
print(mcd(101, 103))
#1
print(mcd(50, 0))
#50
        