from typing import Any
#Ejercicio 1
"""Completar la implementación agregando los siguientes métodos:
•remove_node(x): Remueve el nodo x (si existe) y todas sus aristas adyacentes.
•remove_edge(x, y): Remueve la arista entre el nodo x y el nodo y (si existe).
•are_adjacent(x, y): Devuelve True si x e y son adyacentes, False en caso contrario.
•is_node(x): Devuelve True si x es un nodo del grafo, False en caso contrario.
Estime la complejidad temporal de cada una de las operaciones en función de la cantidad de vértices del grafo."""
class Grafo:
    def __init__(self) -> None:
        self.vertices:list[Any] = []
        self.aristas:dict[Any,list[Any]]= {}
    def add_node(self, vertice: Any) -> None:
    # O(1)
        if vertice not in self. vertices:
            self.vertices.append(vertice)
            self.aristas[vertice] = []
    def add_edge(self, vertice1: Any, vertice2: Any) -> None:
    # O(1)
        self.add_node(vertice1)
        self.add_node(vertice2)
        if vertice2 not in self.aristas[vertice1]:
            self.aristas[vertice1].append(vertice2)
        if vertice1 not in self.aristas[vertice2]:
            self.aristas[vertice2].append(vertice1)
    def get_adjacent(self, vertice: Any) -> list[Any]:
    # O(1)
        return self.aristas[vertice]
    def get_nodes(self) -> list[Any]:
    # O(1)
        return self.vertices
    #---- metodos a completar -----
    def is_node(self, x:Any)->bool:
        #O(1)
        return x in self.vertices
    def are_adjacent(self, x:Any, y:Any)->bool:
        #O(1)
        if self.is_node(x) and self.is_node(y):
            if (x in self.aristas[y]) and (y in self.aristas[x]):
                return True
        return False
    def remove_node(self, x:Any)->None:
        #O(n)
        if x in self.vertices:
            self.vertices.remove(x)
            for vecino in self.aristas[x]:
                self.aristas[vecino].remove(x)
            del self.aristas[x]
    def remove_edge(self, x:Any,y:Any)->None:
        #O(1)
        if self.is_node(x) and self.is_node(y):
            if self.are_adjacent(x,y):
                self.aristas[x].remove(y)
                self.aristas[y].remove(x)
#Ejercicio 2
"""Escriba una función get_edges(G) que reciba un grafo y devuelva una lista de las aristas del grafo.
Tenga cuidado de no repetir aristas."""
def get_edges(G:Grafo)->list:
    lista=[]
    for vertice in G.get_nodes():
        for arista in G.get_adjacent(vertice):
            tupla=tuple(sorted((vertice,arista))) #asi evito duplicado porque siempre va a estar ordenado
            if tupla not in lista:           
                lista.append(tupla)
    return lista
#Ejercicio 3
"""Escriba una función is_subgraph(G, H) que decida si H es subgrafo de G."""
def is_subgraph(G:Grafo, H:Grafo)->bool:
    for v in H.get_nodes():
        if not G.is_node(v):
            return False
        #ahora verifico que los vecinos esten
        for vecino in H.get_adjacent(v): #recorro la lista de vecinos
            if not G.are_adjacent(v,vecino):
                return False
    return True

#Ejercicio 4
"""Escriba una función induce(G, U) que recibe un grafo G y una lista de vértices U y devuelva el grafo
inducido en G por el conjunto U."""
def induce(G:Grafo, U:list[Any])->Grafo:
    grafo_inducido=Grafo()
    for vertice in U:
        if G.is_node(vertice):
            grafo_inducido.add_node(vertice)
        #revisa vecinos en grafo original
        vecinos=G.get_adjacent(vertice)
        for vecino in vecinos:
            if vecino in U:
                grafo_inducido.add_edge(vertice, vecino)
    return grafo_inducido

#Ejercicio 5
"""Implemente el método __eq__ para grafos para permitir comparar por igualdad. Dos grafos son iguales si tienen el mismo conjunto de vértices y la misma colección de aristas"""
class Grafo:
    def __init__(self) -> None:
        self.vertices:list[Any] = []
        self.aristas:dict[Any,list[Any]]= {}
    def add_node(self, vertice: Any) -> None:
    # O(1)
        if vertice not in self. vertices:
            self.vertices.append(vertice)
            self.aristas[vertice] = []
    def add_edge(self, vertice1: Any, vertice2: Any) -> None:
    # O(1)
        self.add_node(vertice1)
        self.add_node(vertice2)
        if vertice2 not in self.aristas[vertice1]:
            self.aristas[vertice1].append(vertice2)
        if vertice1 not in self.aristas[vertice2]:
            self.aristas[vertice2].append(vertice1)
    def get_adjacent(self, vertice: Any) -> list[Any]:
    # O(1)
        return self.aristas[vertice]
    def get_nodes(self) -> list[Any]:
    # O(1)
        return self.vertices
    #---- metodos a completar -----
    def is_node(self, x:Any)->bool:
        #O(1)
        return x in self.vertices
    def are_adjacent(self, x:Any, y:Any)->bool:
        #O(1)
        if not self.is_node(x):
            return False
        return y in self.aristas[x]
    def remove_node(self, x:Any)->None:
        #O(n)
        if x in self.vertices:
            self.vertices.remove(x)
            for vecino in self.aristas[x]:
                self.aristas[vecino].remove(x)
            del self.aristas[x]
    def remove_edge(self, x:Any,y:Any)->None:
        #O(1)
        if self.is_node(x) and self.is_node(y):
            if self.are_adjacent(x,y):
                self.aristas[x].remove(y)
                self.aristas[y].remove(x)
    def __eq__(self, other:Grafo)->bool:
        if not isinstance(other,Grafo):
            return NotImplemented
        #compara vertices
        if sorted(self.get_nodes()) != sorted(other.get_nodes()):
            return False
        #compara aristas        
        if sorted(get_edges(self)) != sorted(get_edges(other)):
            return False
        return True

#Ejercicio 6
"""Escriba una función is_induced_subgraph(G, H) que decida si H es subgrafo inducido de G, para
algún conjunto de vértices."""
def is_induced_subgraph(G:Grafo, H:Grafo)->bool:
    if not is_subgraph(G,H):
        return False
    #verifica los vertices
    for vertice in H.get_nodes():
        for vecino_en_G in G.get_adjacent(vertice): #para cada vecino en G del vertice
            if H.is_node(vecino_en_G): #tiene que ser vertice en H
                if not H.are_adjacent(vertice, vecino_en_G): #y ser adyacente tambien en H
                    return False
    return True

#Ejercicio 7
"""Escriba una función is_complete(G) que decida si G es el grafo completo."""
def is_complete(G: Grafo) -> bool:
    n = len(G.get_nodes())
    for vertice in G.get_nodes():
        # Cada vértice debe tener exactamente n-1 vecinos
        if len(G.get_adjacent(vertice))!=n-1:
            return False
    return True

"""
def is_complete(G:Grafo)->bool:
    #Lo que hay que saber es que la cantidad de aristas se saca de la formula (vertices*(vertices-1))/2
    vertices=len(G.get_nodes())
    aristas=get_edges(G)
    if (vertices*(vertices-1)/2)!=len(aristas):
        return False
    return True
"""

#Ejercicio 9
"""El complemento de un grafo G=(V,E) es un grafo G'=(V,E') que contiene exactamente los mismos
vértices y los vértices v y w estan conectados si y solo si no lo están en V.
Defina una función complement(G) que dado un grafo G, devuelva el grafo complementario a G. La
función debe ser pura, es decir, no debe modificar el grafo original."""
def complento(G:Grafo)->Grafo:
    complentario=Grafo()
    nodos=G.get_nodes()
    for vertice in nodos:
        complentario.add_node(vertice)
    
    for vertice1 in nodos:
        for vertice2 in nodos:
            if vertice1 != vertice2: #no conectar vertice consigo mismo
                if not G.are_adjacent(vertice1, vertice2):
                    complentario.add_edge(vertice1, vertice2)
    
    return complentario

#Ejercicio 8
"""Dado un grafo G=(V,E), un clique es un subconjunto de vértices C ⊆ E tal que todos los vértices de
C son adyacentes entre sí. En otras palabras, un clique es un subgrafo en el que cada vértice está
conectado a todos los demás vértices del subgrafo. Esto equivale a decir que el subgrafo de G inducido
por C es un grafo completo.
El tamaño de un clique es el número de vértices que contiene.
Dar una función has_clique(G, k) que decida si un grafo G tiene un clique de al menos k elementos.
Ayuda: Defina primero una función subsets_of_size_k que, dada una lista y un entero positivo k,
devuelva una lista con todas las posibles listas de tamaño k"""
pass #esperan demasiado de mi