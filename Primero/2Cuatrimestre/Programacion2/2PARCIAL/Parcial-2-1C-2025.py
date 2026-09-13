from typing import Any
"""
1. Cuando el usuario visita una nueva pagina, la pagina actual se guarda en el historial y la nueva
pagina se conviene en la pagina actual. El avance se vacia.
2. Al hacer clic en “Atras”, recupera la ultima pagina guardada en el historial (si la hay) y se
convierte en la pagina actual. La pagina actual hasta ese momento pasa a formar parte del avance.
3. Al hacer clic en “Adelante”, recupera la ultima pagina guardada en el avance (si la hay) y se
convierte en la pagina actual. La pagina actual hasta ese momento pasa a formar parte del historial"""

class Navegador :
def __init__ ( self ):
    self.historial = Pila() # considere que el historial comienza vacio
    self.avance = Pila() # considere que el avance comienza vacio
    self.pagina_actual = None
def visitar (self , pagina : 'Pagina '): # considere que existe una clase Pagina ya definida
    self.historial.apilar(self.pagina_actual)

    self.pagina_actual=pagina
    while not self.avance.esta_vacia():
        self.avance.desapilar()
def atras ( self ):
    #pagina actual pasa a avance
    self.avance.apilar(self.pagina_actual)
    #recupera la ultima pagina del historial y es la nueva actual
    self.pagina_actual=self.historial.desapilar()
def adelante ( self ):
    #la pagina actual pasa al historial
    self.historial.apilar(self.pagina_actual)
    #la pagina en el avance es la nueva actual
    self.pagina_actual=self.avance.desapilar()
def mostrar_pagina_actual ( self ) -> None:
    '''
    Muestra en pantalla la informacion de la pagina actual
    '''
    if self.pagina_actual:
        print(self.pagina_actual)
    else:
        print('Ninguna pagina abierta')
        return

#Ejercicio 2 
"""2. Considere la clase vista en clase BinaryTree:
1. Implemente una funcion que reciba un BinaryTree y devuelva la cantidad de hojas (i.e. nodos
terminales) del  ́arbol.
2. Implemente una funcion que reciba un BinaryTree de numeros, y dos numeros l y r, devuelva
una lista con todos los numeros entre l y r inclusive que se encuentran en el arbol."""

class BinaryTree:
    def __init__(self , cargo=None , left=None , right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
def cantidad_hojas(btree:BinaryTree)->int:
    if btree is None:
        return 0
    if btree.left is None and btree.right is None: #es hoja si no tiene hijos
        return 1
    return cantidad_hojas(btree.left)+cantidad_hojas(btree.right)

def numeros_entre(btree:BinaryTree, l:int, r:int)->list|None:
    if btree is None:
        return []
    lista=[]
    if l<=btree.cargo<=r:
        lista.append(btree.cargo)
    lista_izq=numeros_entre(btree.left,l,r)
    lista_der=numeros_entre(btree.right,l,r)
    return lista + lista_izq + lista_der 

#Ejercicio 3
"""3. Considere la siguiente implementacion del TAD Grafo Dirigido:
Completa la implementaci ́on agregando los siguientes m ́etodos:
1. remove edge(x, y): Remueve la arista dirigida entre el nodo x y el nodo y (si existe).
2. remove node(x): Remueve el nodo x del grafo. Si habia aristas que salian o llegaban a este
nodo, tambi ́en deben borrar del grafo.
3. are adjacent(x, y): Devuelve True si x apunta a y, False en caso contrario.
4. get outdegree(v): Devuelve el grado de salida (outdegree) del vertice, que es el n ́umero de
aristas que salen de  ́el.
5. get indegree(v): Devuelve el grado de salida (indegree) del vertice, que es el n ́umero de aristas
que llegan a  ́el."""
from typing import Any
class GrafoDirigido:
    def __init__(self) -> None:
        self.vertices = []
        self.vecinos = {}
    def add_node(self , vertice: Any) -> None:
        self.vertices.append(vertice)
        self.vecinos[vertice] = []
    def add_edge(self , vertice1: Any , vertice2: Any) -> None:
        self.vecinos[vertice1 ]. append(vertice2)
    def get_adjacent(self , vertice: Any) -> Any:
        return self.vecinos[vertice]
    def get_nodes(self) -> list[Any]:
        return self.vertices
    

    def are_adjacent(self, x,y)->bool:
        if x in self.vertices and y in self.vertices:
            if y in self.vecinos[x]:
                return True
        return False
    def remove_edge(self,x:Any,y:Any)->None:
        if x in self.vertices and y in self.vertices:
            if self.are_adjacent(x,y):
                self.vecinos[x].remove(y)
                self.vecinos[y].remove(x)
    def remove_node(self,x:Any)->None:
        if x in self.vertices:
            self.vertices.remove(x) #saco vertice x
            for vecino in self.vecinos[x]:
                self.vecinos[vecino].remove(x) #saco vertice de lista de vecinos
            del self.vecinos[x] #borro la lista de vecinos de x
    def get_outdegree(self, v:Any)->int:
        aristas_salen=0
        for nodo in self.vertices:
            if self.are_adjacent(v, nodo): #v apunta a nodo
                aristas_salen+=1
        return aristas_salen

    def get_indegree(self, v:Any)->int:
        aristas_entran=0
        for nodo in self.vertices:
            if self.are_adjacent(nodo, v): #nodo apunta a v
                aristas_entran+=1
        return aristas_entran

#Ejercicio 4
"""Lo hice a mano
Pasos:
1) Iniciar S=v1
2) Entre v2,v3yv4 elijo v=v2. L(v2)=1. S=v1,v2
3) Entre v3,v5 elijo v=v5. L(v5)=1+3=4. S=v1,v2,v5
4) Entre v6,v7 elijo v=v7. L(v7)=1+3+1=5. S=v1,v2,v5,v7

B)Prim comenzando en v3
1)v3 a v2=1
2)v2 a v1=1
3)v1 a v4=1
4)v3 a v6=2
5)v6 a v5=1
6)v5 a v7=1
Total=1+1+1+2+1+1=7


