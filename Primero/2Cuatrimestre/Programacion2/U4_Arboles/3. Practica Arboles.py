"""Árboles Binarios
A lo largo de esta práctica trabajaremos con la siguiente estructura, observe lo similar que es a Node de
Listas Enlazadas, pero en lugar de next, posee left y right.
class Tree:
def __init__(self, cargo, left = None, right = None):
self.cargo = cargo
self.left = left
self.right = right
Ejercicio 1
Dibuje ejemplos de árboles en su hoja con las siguientes características, luego, construya sus ejemplos
en Python
1. Un árbol con únicamente su raíz.
2. Un árbol parecido a una lista de largo 3.
3. Un árbol completo de altura 1.
4. Un árbol vacío ¿Puede hacerlo?"""
from typing import Optional, Any
#Ejercicio 1
class Tree:
    def __init__(self, cargo:Any , left= None, right = None)->None:
        self.cargo = cargo
        self.left = left
        self.right = right
    def __str__(self)->str:
        return(self.cargo)

unica_raiz=Tree(1)
largo3=Tree(1,Tree(2,Tree(3))) #1->Left de 1=2->left de 2=3
altura1=Tree(1,Tree(2),Tree(3))
arbol_vacio=None

#Ejercicio 2
"""Implemente en la clase Tree los siguiente métodos:
Ayuda: pensar que cada árbol tiene a su izquierda y derecha objetos árboles como sus hijos.
•nodos: devuelve la cantidad de nodos del árbol
•menor_mayor: devuelve el menor y el mayor elemento del árbol en una tupla
•buscar: busca si un elemento está o no en el árbol
•altura: calcula la altura del árbol, la distancia desde la raíz hasta la hoja más lejana"""
class Tree:
    def __init__(self, cargo:Any , left:Optional['Tree'] = None, right:Optional['Tree'] = None)->None:
        self.cargo = cargo
        self.left = left
        self.right = right
    def __str__(self)->str:
        return(self.cargo)
    def nodos(self)->int:
        """devuelve la cantidad de nodos del arbol"""
        if self is None:
            return 0
        num=1
        if self.left is not None:
            num+=self.left.nodos()
        if self.right is not None:
            num+=self.right.nodos()
        return num
    """Solucion mas recursiva
    def nodos(self) -> int:
    if self is None:
        return 0
    return 1 + self.left.nodos() + self.right.nodos()"""

    def menor_mayor(self)->tuple:
        """devuelve el menor y el mayor elemento del árbol en una tupla"""
        menor,mayor=self.cargo, self.cargo
        if self.left is not None: 
            menor_izq, mayor_izq=self.left.menor_mayor()
            if menor_izq<menor:
                menor=menor_izq
            if mayor_izq>mayor:
                mayor=mayor_izq
        if self.right is not None:
            menor_der, mayor_der=self.right.menor_mayor()
            if menor_der<menor:
                menor=menor_der
            if mayor_der>mayor:
                mayor=mayor_der
        return menor,mayor
    def buscar(self, elemento:Any)->bool:
        """busca si un elemento está o no en el árbol"""
        if self.cargo == elemento:
            return True
        encontrado_izq=False
        if self.left is not None:
            encontrado_izq=self.left.buscar(elemento)
        if encontrado_izq:
            return True
        encontrado_der=False
        if self.right is not None:
            encontrado_der=self.right.buscar(elemento)
        if encontrado_der:
            return True
        return False
    """Solucion mas recursiva 
    def buscar(self, x) -> bool:
    if self is None:
        return False
    if self.cargo == x:
        return True
    return self.left.buscar(x) or self.right.buscar(x)"""
    def altura(self)->int:
        """calcula la altura del árbol, la distancia desde la raíz hasta la hoja más lejana"""
        altura_izq=0
        altura_der=0
        if self.left is not None:
            altura_izq=1+self.left.altura()
        if self.right is not None:
            altura_der=1+self.right.altura()
        altura=max(altura_izq,altura_der)
        return altura
#Ejercicio 3
"""a. Pensar y dibujar un ejemplo de árbol en papel, escribir los resultados de PreOrder, InOrder yPostOrder
b. Implementar los recorridos PreOrder, InOrder y PostOrder como funciónes recursivas, verificarsus resultados
c. Implementar los recorridos PreOrder, InOrder y PostOrder como funciónes iterativas, verificarsus resultados

Ayuda: Para las versiones iterativas, necesitará utilizar una Pila como estructura de datos adicional.
Puede importar una implementacion cualquiera de Pila que haya realizado en la Practica anterior."""
def PreOrder(arbol:Tree)->Tree|None:
    """Primero raiz, luego subarbol izq, luego subarbol der"""
    if arbol is None:
        return
    print(arbol.cargo)
    PreOrder(arbol.left)
    PreOrder(arbol.right)

def InOrder(arbol:Tree)->Tree|None:
    """Primero subarbol izq, luego raiz, luego subarbol der"""
    if arbol is None:
        return
    InOrder(arbol.left)
    print(arbol.cargo)
    InOrder(arbol.right)


def PosOrder(arbol:Tree)->Tree|None:
    """Primero subarbol izq, luego subarbol der, luego raiz"""
    if arbol is None:
        return
    PosOrder(arbol.left)
    PosOrder(arbol.right)
    print(arbol.cargo)

class Pila:
    def __init__(self)->None:
        """Crea la pila vacia"""
        self.items=[]
    def push(self, elemento:Any)->None:
        """Apila elemento sobre la lista"""
        self.items.append(elemento)
    def pop(self)->Any:
        """Desapila el ultimo elemento y lo devuelve"""
        if self.isEmpty():
            print(f'Pila vacia')
            return
        return self.items.pop()
    def isEmpty(self)->bool:
        if len(self.items)==0:
            return True
        return False
#----- Iterativos -----
def IterativaPreOrder(arbol:Tree)->None:
    if arbol is None:
        return
    pila=Pila()
    pila.push(arbol) #pone la raiz
    while not pila.isEmpty():
        nodo_actual=pila.pop()
        print(nodo_actual.cargo)
        #se recorre nodo derecho primero y dsp izquierdo para que dsp el pop saque lo ultimo arriba(nodo izq)
        if nodo_actual.right is not None:
            pila.push(nodo_actual.right)
        if nodo_actual.left is not None:
            pila.push(nodo_actual.left)
def IterativoInOrder(arbol:Tree)->None:
    pila=Pila()
    nodo_actual=arbol
    while not pila.isEmpty() or arbol is not None:
        if nodo_actual is not None: #baja hasta el nodo mas a la izquierda hasta que encuentra el ultimo nodo a la izquierda(actual is None)
            pila.push(nodo_actual)
            nodo_actual=nodo_actual.left
        else:
            #ahora saca de la raiz
            nodo_actual=pila.pop()
            print(nodo_actual.cargo)
            #ahora vamos al subarbol derecho
            nodo_actual=nodo_actual.right
def IterativoPostOrder(arbol:Tree)->None:
    """La idea es hacer un PreOrder modificado (Raíz -> Derecha -> Izquierda)
    y guardamos el resultado, luego lo invertimos."""
    pila=Pila()
    pila.push(arbol) #pone la raiz
    salida=[]
    while not pila.isEmpty():
        nodo_actual=pila.pop()
        salida.append(nodo_actual.cargo)
        #se recorre nodo izq primero y dsp derecho para que dsp el pop saque lo ultimo arriba(nodo izq)
        if nodo_actual.left is not None:
            pila.push(nodo_actual.left)
        if nodo_actual.right is not None:
            pila.push(nodo_actual.right)
    #lo imprimimos en manera inversa
    print(salida[::-1])

#Ejercicio 4
"""Escriba una función copiar que reciba un árbol y devuelva un nuevo árbol idéntico al original."""
def copiar(arbol:Tree)->Tree|None:
    if arbol is None:
        return None
    #copiar el nodo actual
    nuevo_arbol=Tree(arbol.cargo)
    #recursivamente
    nuevo_arbol.left=copiar(arbol.left)
    nuevo_arbol.right=copiar(arbol.right)
    return nuevo_arbol

"""Solucion mas recursiva
def copiar(arbol: Tree) -> Tree:
    if arbol is None:
        return None
    return Tree(arbol.cargo, copiar(arbol.left), copiar(arbol.right))"""

#Ejercicio 5
"""Escriba una función invertir que reciba un árbol binario e intercambie los hijos derechos por los izquierdos de todos los nodos."""
def invertir(arbol:Tree)->Tree|None:
    if arbol is None:
        return None
    #copiar nodo actual
    nuevo_arbol=Tree(arbol.cargo)
    nuevo_arbol.left=invertir(arbol.right)
    nuevo_arbol.right=invertir(arbol.left)
    return nuevo_arbol

"""Solucion mas recursiva
def invertir(arbol:Tree)->Tree:
    if arbol is None:
        return None
    return Tree(arbol.cargo, invertir(arbol.right), invertir(arbol.left))"""

#Ejercicio 6
"""Escriba una función sumatoria que reciba un árbol binario que contiene números en sus nodos y devuelva la suma de todos los nodos"""
def sumatoria(arbol:Tree)->float:
    if arbol is None:
        return 0
    suma=arbol.cargo
    if arbol.left is not None:
        suma+=sumatoria(arbol.left)
    if arbol.right is not None:
        suma+=sumatoria(arbol.right)
    return suma
"""Solucion mas recursiva
def sumatoria(arbol:Tree)->int:
    if arbol is None:
        return 0
    return arbol.cargo+sumatoria(arbol.left)+sumatoria(arbol.right)"""

#Ejercicio 7
"""Escriba una función que reciba un árbol binario A cuyos nodos contienen números y que dado un
entero M, una clave inicial inicio y una clave final final, calcula la suma de todos los números de los árboles que se encuentren entre inicio y final y a lo sumo en el nivel M."""
def suma_hasta_nivel(arbol:Tree, M:int, inicio:int, final:int)->int:
    if arbol is None:
        return 0
    if M<0: #se resto tanto que nos pasamos y estamos en un nivel mayor al permitido
        return 0
    suma=0
    if inicio<=arbol.cargo<=final:
        suma+=arbol.cargo
    return suma + suma_hasta_nivel(arbol.left, M-1, inicio, final) + suma_hasta_nivel(arbol.right, M-1, inicio, final)

#Arboles Binarios de Busqueda BST
#Ejercicio 9
"""Utilizando la misma clase Tree de la sección anterior, implemente otra clase llamada BSTree que herede
de esta, reimplemente los métodos menor_mayor, buscar e implemente un nuevo método llamado insertar que inserte un elemento.
Ayuda: puede optar por definir métodos menor y mayor internamente por separado para hacer la
implementación más sencilla, pero no es estrictamente necesario."""
class BSTree(Tree):
    def __init__(self,cargo:Any, left=None,right=None)->None:
        super.__init__(cargo,left,right)

    def insertar(self, new_data:Any)->None:
        """Inserta nuevo dato en el arbol"""
        if new_data<self.cargo:
            if self.left is None:          
                self.left=BSTree(new_data)#crea nodo
            else:
                self.left.insertar(new_data)#sigue buscando recursivamente
        elif new_data>self.cargo:
            if self.right is None:          
                self.right=BSTree(new_data)#crea nodo
            else:
                self.right.insertar(new_data)#sigue buscando recursivamente
    def buscar(self, elemento:Any)->bool:
        if elemento<self.cargo:
            if self.left is None:
                return False
            else:
                return self.left.buscar(elemento)
        elif elemento>self.cargo:
            if self.right is None:
                return False
            else:
                return self.right.buscar(elemento)
        else:
            return True

    def menor_mayor(self)->tuple:
        menor_actual=self.left
        while menor_actual.left is not None:
            menor_actual=menor_actual.left #avanzo hasta llegar al nodo mas a la izquierda
        menor=menor_actual.cargo
        mayor_actual=self.right
        while mayor_actual.right is not None:
            mayor_actual=mayor_actual.right #avanzo hasta llegar al nodo mas a la derecha
        mayor=mayor_actual.cargo
        return menor,mayor
    

#Ejercicio 10
"""Escriba una función combinar que combine dos árboles binarios de búsqueda en uno solo. El resultado tambien debe ser un árbol binario de búsqueda.
Ayuda: quizás resulte conveniente implementar una función de copia pero para BSTree."""
def copiarBST(arbol:BSTree)->BSTree|None:
    if arbol is None:
        return None
    #copiar el nodo actual
    return BSTree(arbol.cargo, copiarBST(arbol.left), copiarBST(arbol.right))


def obtener_elementos(arbol:BSTree)->list:
    valores = []

    valores.append(arbol.cargo)
    
    if arbol.left:
        valores += obtener_elementos(arbol.left)
    if arbol.right:
        valores +=  obtener_elementos(arbol.right)
    return valores



def combinarBST(arbol1: BSTree, arbol2: BSTree) -> BSTree | None:
    if arbol1 is None and arbol2 is None:
        return None
    #si falta el arbol1 devolvemos COPIA del 2
    elif arbol1 is None:
        return copiarBST(arbol2)
    #si falta el arbol2 devolvemos COPIA del 1
    elif arbol2 is None:
        return copiarBST(arbol1)
    else: #ambos existen
        arbol_combinado = copiarBST(arbol1)
        arbol2_elementos=obtener_elementos(arbol2)
        for elemento in arbol2_elementos:
            arbol_combinado.insertar(elemento)
        return arbol_combinado

#Ejercicio 11
"""Escriba una función borrar_raiz. Dado un árbol binario de búsqueda, esta función deberia devolver
un nuevo árbol binario de búsqueda que contenga los mismos datos, a excepcion de la raiz."""
def obtener_minimo(arbol:BSTree)->Any:
    menor_actual=arbol
    while menor_actual.left is not None:
        menor_actual=menor_actual.left #avanzo hasta llegar al nodo mas a la izquierda
    menor=menor_actual.cargo
    return menor

def borrar_minimo(arbol: BSTree) -> BSTree | None:
    if arbol.left is None:
        # Caso base: Encontramos el menor, lo saltamos devolviendo su derecha
        return arbol.right
    # Caso recursivo: Seguimos bajando por la izquierda
    arbol.left = borrar_minimo(arbol.left)
    return arbol

def borrar_raiz(arbol:BSTree)->BSTree|None:
    if arbol is None:
        return None
    elif arbol.left is None and arbol.right is None:
        return None
    elif arbol.left is None: #caso sin hijos izq
        return arbol.right
    elif arbol.right is None: #caso sin hijos der
        return arbol.left
    #caso hijos der y el izq, busco nueva raiz que es el mayor del subarbol izq o el menor del subarbol derecho
    menor_derecha=obtener_minimo(arbol.right) #va a ser la nueva raiz
    arbol.cargo=menor_derecha #reemplazo el valor de la raiz actual
    arbol.right=borrar_minimo(arbol.right) #borramos el nodo duplicado del lado derecho
    return arbol
#Ejercicio 12
"""Escriba una función borrar_valor que dado un árbol binario de búsqueda y un valor, devuelva un
árbol binario de búsqueda sin ese valor."""
def borrar_valor(arbol:BSTree, valor:Any)->BSTree:
    if arbol is None:
        return None
    if valor<arbol.cargo:
        arbol.left=borrar_valor(arbol.left, valor)
        return arbol
    if valor>arbol.cargo:
        arbol.right=borrar_valor(arbol.right, valor)
        return arbol
    else:
        return borrar_raiz(arbol)