#Ejercicio 1
"""1. Considere la siguiente clase Nodo:
    Utilicela para implementar una lista doblemente enlazada:

Implemente los metodos especificados:
1. agregar al principio: Agrega un nodo con el dato al principio de la lista.
2. agregar al final: Agrega un nodo con el dato al final de la lista.
3. eliminar al principio: elimina el nodo al principio de la lista.
4. eliminar al final: elimina el nodo al final de la lista.
5. eliminar dato: elimina el primer nodo que encuentra con el dato buscado, arrancando desde
el principio, si lo encuentra.
6. longitud: Devuelve la cantidad de datos guardados en la lista.
    
    """
from typing import Any
class Nodo:
    def __init__(self , dato = None , siguiente = None , anterior = None):
        self.dato = dato
        self.sig = siguiente
        self.ant = anterior
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.largo = 0
    def agregar_al_principio(self , dato:Any)->None:
        nuevo=Nodo(dato)
        if self.largo==0:
            self.cabeza=self.ultimo=nuevo
        else:
            nuevo.sig=self.cabeza
            self.cabeza.ant=nuevo
            self.cabeza=nuevo
        self.largo+=1
    def agregar_al_final(self , dato)->None:
        nuevo=Nodo(dato)
        if self.largo==0:
            self.cabeza=self.ultimo=nuevo
        else:
            nuevo.ant=self.ultimo
            self.ultimo.sig=nuevo
            self.ultimo=nuevo
        self.largo+=1
    def eliminar_al_principio(self)->None:
        dato=self.cabeza.dato
        if self.largo==1:
            self.cabeza=self.ultimo=None
        else:
            self.cabeza=self.cabeza.sig
            self.cabeza.ant=None
        self.largo-=1
        #return dato
    def eliminar_al_final(self)->None:
        dato=self.ultimo.dato
        if self.largo==1:
            self.cabeza=self.ultimo=None
        else:
            self.ultimo=self.ultimo.ant
            self.ultimo.sig=None
        self.largo-=1
        #return dato

    def eliminar_dato(self , dato:Any)->None:
        actual=self.cabeza
        while actual is not None and actual.dato!=dato:
            actual=actual.sig
        
        if actual is None:
            print(f'No se encontro dato')
            return
        
        if actual==self.cabeza:
            self.eliminar_al_principio()
        elif actual==self.ultimo:
            self.eliminar_al_final()
        else: #nodo intermedio
            actual.sig.ant=actual.ant
            actual.ant.sig=actual.sig
            self.largo-=1
        
    def longitud (self) ->int:
        return self.largo

#Ejercicio 2
"""2. Considere la siguiente implementacion del TAD Pila:
Agregue los siguientes m ́etodos a la clase Pila:
1. tamanio: Devuelve la cantidad de elementos en la pila.
2. limpia: Elimina todos los elementos de la pila.
3. copiar: Devuelve una nueva pila que es una copia de la pila actual"""
class Pila:
    def __init__(self):
        self.items = []
    def apilar(self , item):
        self.items.append(item)
    def desapilar(self):
        return self.items.pop() if not self.esta_vacia () else None
    def esta_vacia(self):
        return len(self.items) == 0
    def cima(self):
        return self.items[-1] if not self.esta_vacia () else None

    def tamanio(self)->int:
        """Devuelve la cantidad de elementos en la pila."""
        return len(self.items)
    def limpia(self)->None:
        """Elimina todos los elementos de la pila."""
        while not self.esta_vacia():
            self.desapilar()
    def copiar(self)->'Pila':
        """Devuelve una nueva pila que es una copia de la pila actual"""
        copia=Pila()
        for elemento in self.items:
            copia.apilar(elemento)
        return copia

#Ejercicio 3
"""3. Considere la siguiente clase ArbolBinario:
Implemente los metodos especificadas:
1. contar nodos: Devuelve la cantidad de nodos en el arbol.
2. sumar valores: Devuelve la suma de todos los valores en el arbol
"""
class ArbolBinario :
    def __init__ (self , valor =None , izquierda =None , derecha = None ):
        self . valor = valor
        self . izquierda = izquierda
        self . derecha = derecha
def contar_nodos ( arbol : 'ArbolBinario' )->int:
    if arbol is None:
        return 0
    return 1+contar_nodos(arbol.izquierda)+contar_nodos(arbol.derecha)
def sumar_valores ( arbol : 'ArbolBinario' )->int:
    if arbol is None:
        return 0
    return arbol.valor+sumar_valores(arbol.izquierda)+sumar_valores(arbol.derecha)

#Ejercicio 4
"""Lo hice a mano
Pasos:
1) Iniciar S=A
2) Entre ByE elijo v=B. L(B)=5. S=A,B
3) Entre C,DyE elijo v=D. L(D)=5+6=11. S=A,B,D
4) Si elegia A,B,C,D daba L(D)=5+3+4=12
