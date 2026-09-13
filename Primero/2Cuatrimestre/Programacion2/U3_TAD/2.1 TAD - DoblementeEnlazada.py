#Ejercicio 6 Una desventaja de la implementación del TAD Lista que vimos es que es relativamente caro insertar al final de la lista, dado que necesitamos recorrer todos los nodos para poder 
    # lograrlo. Esto se puede solucionar utilizando la estructura conocida como ListaDoblementeEnlazada. Esta estructura funciona en esencia del mismo modo que la ListaEnlazada que ya vimos,
    #  pero incorpora un atributo más (last) y el siguiente invariante de objeto: 
    # Invariante: El atributo last es None si la lista está vacía. Si no está vacía, last apunta al último elemento de la lista. 
    # Dar una implementación del TAD Lista utilizando una ListaDoblementeEnlazada.
from typing import Any
class NodoDoble:
    def __init__(self, dato:Any=None, prox=None, prev=None)->None:
        self.dato=dato
        self.prox=prox
        self.prev=prev
    def __str__(self)->str:
        return str(self.dato)

class ListaDoblementeEnlazada:
    def __init__(self)->None:
        """Inicia lista vacia"""
        self.prim=None
        self.last=None
        self.len=0
    def __len__(self) -> int:
        """devuelve la cantidad de nodos de la lista"""
        return self.len
    def __str__(self)-> str:
        """devuelve la lista en formato string"""
        texto='['
        nodo=self.prim
        while nodo is not None:
            texto+=str(nodo.dato)
            nodo=nodo.prox #avanzo al prox nodo
            if nodo is not None:
                texto+=', '
        texto+=']'
        return texto
    
    def append(self, x:Any)->None:
        """ Agrega elemento x al final de la lista"""
        nuevo=NodoDoble(x)
        if self.len==0:
            self.prim=self.last=nuevo
        else:
            nuevo.prev=self.last #el anterior ultimo es el previo del nuevo ultimo
            self.last.prox=nuevo #el siguiente del anterior ultimo es nuevo
            self.last=nuevo #el nuevo ultimo es nuevo
        self.len+=1
    def remove(self, x:Any)->None:
        """Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, imprime un mensaje de error y retorna
        inmediatamente."""
        if self.len == 0:
            print("La lista esta vacía")
            return
        actual=self.prim
        #avanzo mientras no se encuentra ni llega al final
        while actual is not None and actual.dato != x:
            actual=actual.prox
        #si no lo encontro
        if actual is None:
            print('El valor no esta en la lista')
            return
        
        #si lo encontro hay 4 casos
        if self.len==1: #1_unico elemento en lista
            self.prim=self.last=None
        elif actual==self.prim: #2_si es el primero en la lista 
            self.prim=actual.prox
            self.prim.prev=None
        elif actual==self.last: #3_si es el ultimo elemento
            self.last=actual.prev
            self.last.prox=None
        else: #4_es un nodo intermedio
            actual.prev.prox=actual.prox #el anterior al actual apunta al proximo del actual
            actual.prox.prev=actual.prev #el proximo al actual apunta al anterior del actual
        self.len-=1
    def insert(self,i:int,x:Any)->None:
        """Inserta el elemento x en la posición i. 
        Si la posición es inválida, imprime un error y retorna inmediatamente."""
        if i < 0 or i >self.len:
            print("Posición inválida")
            return
        nuevo=NodoDoble(x)
        if i==0:
            if self.len==0:
                self.prim=self.last=nuevo
            else:
                nuevo.prox=self.prim
                self.prim.prev=nuevo
                self.prim=nuevo
            
            self.len+=1
            return
        elif i==self.len: #ultima pos
            self.append(x)
            return
        else: #nodo intermedio
            if i<self.len/2: #primera mitad se busca de adelante para atras
                anterior=self.prim
                for pos in range(i):
                    anterior=anterior.prox
            else: #esta en la segunda mitad buscamos de atras para adelante
                anterior=self.last
                for pos in range(self.len-i):
                    anterior=anterior.prev
            # Para este punto, 'anterior' es el nodo que estará ANTES del nuevo nodo
            siguiente=anterior.prox
            #conecto el nuevo con el siguiente y anterior
            nuevo.prox=siguiente
            nuevo.prev=anterior
            #conecto nodos vecinos con nuevo
            anterior.prox=nuevo
            siguiente.prev=nuevo

            self.len+=1
            return
    def pop(self, i:int|None= None)->Any:
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se muestra un mensaje de error y se retorna inmediatamente. Si no se recibe la posición, devuelve el último elemento."""
        if self.len == 0:
            print("Error: La lista está vacía")
            return
        if i < 0 or i > self.len:
            print("Posición inválida")
            return
        
        if i is None:
            i=self.len-1
        if i==0:
            dato=self.prim.dato
            self.prim=self.prim.prox
            if self.prim is not None: #lista no quedo vacia
                self.prim.prev=None
            else: #lista vacia
                self.last=None
        elif i==self.len-1:
            dato=self.last.dato
            self.last=self.last.prev
            if self.last is not None: #lista no quedo vacia
                self.last.prox=None
            else: #lista vacia
                self.prim=None
        else: #nodo intermedio
            if i<self.len/2: #primera mitad se busca de adelante para atras
                actual=self.prim
                for pos in range(i):
                    actual=actual.prox
            else: #esta en la segunda mitad buscamos de atras para adelante
                actual=self.last
                for pos in range(self.len-1-i):
                    actual=actual.prev
            #actual es el nodo a eliminar
            dato=actual.dato
            #para hacer el enganche mas legible
            siguiente=actual.prox
            anterior=actual.prev
            #enganchamos el resto de nodos
            anterior.prox = siguiente 
            siguiente.prev = anterior
        self.len-=1
        return dato