"""Listas
Ejercicio 1
Complete la implementación del TAD Lista utilizando nodos enlazados. Falta implementar los métodos
index, append, __len__ y __str__. Escriba código de prueba hasta convencerse de que esta clase
funciona de manera análoga a las listas de Python."""
from typing import Any

class _Nodo:
    def __init__(self, dato: Any = None, prox=None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return str(self.dato)

def ver_lista(nodo: _Nodo | None) -> None:
    """Recorre todos los nodos a través de sus enlaces, mostrando sus contenidos."""
    while nodo is not None:
        print(nodo)
        nodo = nodo.prox

class ListaEnlazada:
    """Modela una lista enlazada."""
    def __init__(self) -> None:
        """Crea una lista enlazada vacía."""
        # Referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # Cantidad de elementos de la lista
        self.len = 0

    def insert(self, i: int, x: Any) -> None:
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, imprime un error y retorna inmediatamente.
        """
        if i < 0 or i > self.len:
            print("Posición inválida")
            return
        nuevo = _Nodo(x)
        if i == 0:
            # Caso particular : insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox
            # Intercalar el nuevo nodo
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        self.len += 1

    def pop(self, i: int | None = None) -> Any:
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se muestra un mensaje de error y se
        retorna inmediatamente. Si no se recibe la posición, devuelve el
        último elemento.
        """
        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            print(" Posición inválida ")
            return
        if i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i -1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
            # Guardar el dato y descartar el nodo
            dato = n_act.dato
            n_ant.prox = n_act.prox
            self.len -= 1
        return dato

    def remove(self, x: Any) -> None:
        """Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, imprime un mensaje de error y retorna
        inmediatamente.
        """
        if self.len == 0:
            print("La lista esta vacía")
            return
        if self.prim.dato == x:
            # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
            # Buscar el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox
            if n_act is None:
                print("El valor no está en la lista.")
                return
            # Descartar el nodo
            n_ant.prox = n_act.prox
            self.len -= 1
    ######### Metodos a completar ##############
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
        nuevo=_Nodo(x)
        if self.len==0:
            self.prim=nuevo
        else:
            actual=self.prim
            while actual.prox is not None: #se ejecuta hasta pararse en el ultimo nodo(el que apunta a None)
                actual=actual.prox
            actual.prox=nuevo #ahora el ultimo nodo es el nuevo
        self.len+=1
    
    def index(self, x:Any)->int|str:
        """Devuelve la posicion de la primera aparicion de x en la lista, si no encuentra ERROR y sale"""
        if self.len==0:
            return f'Error! Lista esta vacia!'
        actual=self.prim
        cont=0
        while actual is not None: #avanza a todos los nodos mientras actual no sea None
            if actual.dato==x:
                return cont 
            actual=actual.prox
            cont+=1
        return f'Error! No se encontro el valor en la lista'
    
    #Ejercicio 2 
    """ Agregue a ListaEnlazada un método extend que reciba una ListaEnlazada y agregue a la lista actual los elementos que se encuentran en la lista recibida. 
    ¿Puede estimar la complejidad de este método?"""
    def extend(self, lista:'ListaEnlazada')->None:
        if len(lista)==0:
            return
        if self.len==0:
            self.prim=lista.prim
        else:
            actual=self.prim
            while actual.prox is not None:
                actual=actual.prox
            actual.prox=lista.prim
        self.len+=lista.len
    #Ejercicio 3 
    """Implemente el método remover_todos(elemento) de ListaEnlazada, que recibe un elemento y remueve de la lista todas las apariciones del mismo, devolviendo la cantidad de elementos removidos. 
    La lista debe ser recorrida una sola vez."""
    def remover_todos(self,elemento:Any)->int:
        """recibe un elemento y remueve de la lista todas las apariciones del mismo, devolviendo la cantidad de elementos removidos"""
        if self.len == 0:
            print("La lista esta vacía")
            return 0
        
        cont=0
        while self.prim is not None and self.prim.dato == elemento: #si el elemento a remover esta en la cabecera
            self.prim = self.prim.prox
            cont+=1
            self.len-=1
        
        if self.len==0: #verifica que la lista no haya quedado vacia
            return cont
        
        #recorre resto de la lista
        n_ant = self.prim
        n_act = n_ant.prox
        while n_act is not None:
            if n_act.dato == elemento:
                n_ant.prox = n_act.prox #remueve el nodo
                cont+=1
                self.len-=1
                n_act=n_ant.prox #n_ant no se mueve, n_act avanza al siguiente por si hay 2 elementos a remover seguidos en la lista 
            else:                 
                n_ant = n_act
                n_act = n_ant.prox
        return cont
    
    #Ejercicio 4 
    """ Implemente el método duplicar(elemento) de ListaEnlazada, que recibe un elemento y duplica todas las apariciones del mismo. Ejemplo:
    L = 1 -> 5 -> 8 -> 8 -> 2 -> 8
    L.duplicar(8) = L = 1 -> 5 -> 8 -> 8 -> 8 -> 8 -> 2 -> 8 -> 8 """
    def duplicar(self, elemento:Any)->None:
        """recibe un elemento y duplica todas las apariciones del mismo"""
        if self.len==0:
            print(f'Lista vacia no encuentra elemento')
            return
        act=self.prim
        while act is not None:
            if act.dato==elemento:
                nuevo=_Nodo(elemento)
                nuevo.prox=act.prox
                act.prox=nuevo
                self.len+=1
                act=nuevo.prox #avanza
            else:
                act=act.prox #avanza

    #Ejercicio 5 
    """Escriba un método de la clase ListaEnlazada que invierta el orden de la lista (es decir, el primer elemento queda como último y viceversa)"""
    def invertir(self)->None:
        if self.len==0:
            print(f'Lista vacia')
            return
        invertida=ListaEnlazada()
        act=self.prim
        while act is not None:
            invertida.insert(0,act.dato)
            act=act.prox
        self.prim=invertida.prim
        self.len=invertida.len
    #Ejercicio 7
    """Implemente el método filtrar_primos() en la clase ListaEnlazada, que devuelve una nueva lista enlazada con los elementos que sean números primos. 
    La nueva lista debe ser construida recorriendo los nodos una sola vez (es decir, no se puede llamar a append!). Ejemplo:
    L = 1 -> 5 -> 8 -> 8 -> 2 -> 8
    L.filtrar_primos() -> L2 = 5 -> 2
    Ayuda: Conviene definir primero una función es_primo(n) que reciba un número entero y decida si es primo o no."""
    def es_primo(n)->bool:
        if n<=1:
            return False
        for i in range(2, int(n**0.5)+1):
            if (n%i)==0:
                return False
        return True
    
    def filtrar_primos(self)->'ListaEnlazada':
        lista_primos=ListaEnlazada()
        actual=self.prim
        ultimo_primo=None #variable solo para apuntar al ultimo primo
        while actual is not None:
            if self.es_primo(actual.dato) is True:
                nuevo=_Nodo(actual.dato)
                if lista_primos.prim is None: #no hay primos
                    lista_primos.prim=nuevo
                else: #recorrer lista_primos hasta el final porque no uso lista_primos.append(nuevo.dato)
                    actual_primos=lista_primos.prim
                    while actual_primos.prox is not None:
                        actual_primos=actual_primos.prox
                    actual_primos.prox=nuevo
                lista_primos.len+=1
            
            actual=actual.prox #avanzo nodo de la ListaEnlazada
        return lista_primos
    
    #Ejercicio 8
    """Se tiene una lista enlazada L de palabras, y se quiere insertar la palabra “mundo” despues de todas las apariciones de la palabra “hola”. 
    Defina una función insertar_palabra_despues(lista, palabra_objetivo, palabra_insertar) que dada una lista, una palabra objetivo (hola) y una palabra
    a insertar (mundo) devuelva una nueva lista enlazada donde se agrega la nueva palabra cada vez que se encuentra la palabra objetivo.
    Por ejemplo:
    L = “Planificacion” -> “Hola” -> “de” -> “Trece”
    insertar_palabra_despues(L, “Hola”, “Mundo”) -> L2 = “Planificacion” -> “Hola” -> “Mundo” -> “de” -> “Trece" """
    def insertar_palabra_despues(lista:'ListaEnlazada', palabra_objetivo:str, palabra_insertar:str)->'ListaEnlazada':
        lista_final=ListaEnlazada()
        actual=lista.prim
        ultimo_nodo=None
        while actual is not None:
            #copiar nodo viejos
            copia=_Nodo(actual.dato)
            if lista_final.prim is None:
                lista_final.prim=copia
                ultimo_nodo=copia
            else:
                ultimo_nodo.prox=copia
                ultimo_nodo=copia
            lista_final.len+=1
            #insertar coincidencia
            if actual.dato == palabra_objetivo:
                insertar=_Nodo(palabra_insertar)
                ultimo_nodo.prox=insertar
                ultimo_nodo=insertar
                lista_final.len+=1
            #pasa al nodo sigueinte
            actual=actual.prox
    
        return lista_final
    #Ejercicio 9 
    """ Se tiene una lista enlazada L de palabras, y se desea eliminar todas las palabras que contengan una
    ñ. Defina una función eliminar_palabras_con(lista, carácter) que dada una lista y un carácter, devuelva una nueva lista enlazada donde se eliminaron las apariciones 
    de palabras conteniendo dicho carácter.
    Por ejemplo:
    L = “Ocho” -> “Veinte” -> “Veinticuatro” -> “Hoy”
    eliminar_palabras_con(L, “V”) -> L2 = “Ocho” -> “Hoy” """
    def eliminar_palabras_con(lista:'ListaEnlazada', caracter:str)->'ListaEnlazada':
        lista_final=ListaEnlazada()
        actual=lista.prim
        ultimo_nodo=None
        while actual is not None:
            #copiar nodo viejos si no tineen el caracter
            if caracter not in actual.dato:
                copia=_Nodo(actual.dato)
                if lista_final.prim is None:
                    lista_final.prim=copia
                    ultimo_nodo=copia
                else:
                    ultimo_nodo.prox=copia
                    ultimo_nodo=copia
                lista_final.len+=1
            #pasa nodo siguiente
            actual=actual.prox
        return lista_final