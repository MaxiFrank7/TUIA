# Ejercicio 1

class Nodo:
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.sig = siguiente
        self.ant = anterior

    def __str__(self):
        return f"{self.dato}"


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.largo = 0

    def __str__(self):
        ret = ""
        nodo = self.cabeza
        while nodo is not None:
            ret += f"{nodo} "
            nodo = nodo.sig
        return ret.strip()

    def agregar_al_principio(self, dato):
        """
        1. agregar al principio: Agrega un nodo con el dato al principio de la lista.
        """
        nodo = Nodo(dato)
        if self.largo == 0:
            self.cabeza = nodo
            self.ultimo = nodo
        else:
            self.cabeza.ant = nodo
            nodo.sig = self.cabeza
            self.cabeza = nodo
        self.largo += 1

    def agregar_al_final(self, dato):
        """
        2. agregar al final: Agrega un nodo con el dato al final de la lista.
        """
        nodo = Nodo(dato)
        if self.largo == 0:
            self.cabeza = nodo
            self.ultimo = nodo
        else:
            self.ultimo.sig = nodo
            nodo.ant = self.ultimo
            self.ultimo = nodo
        self.largo += 1

    def eliminar_al_principio(self):
        """
        3. eliminar al principio: elimina el nodo al principio de la lista.
        """
        if self.largo == 0:
            return
        self.cabeza = self.cabeza.sig
        if self.cabeza is None:
            self.ultimo = None
        else:
            self.cabeza.ant = None
        self.largo -= 1

    def eliminar_al_final(self):
        """
        4. eliminar al final: elimina el nodo al final de la lista.
        """
        if self.largo == 0:
            return
        self.ultimo = self.ultimo.ant
        if self.ultimo is None:
            self.cabeza = None
        else:
            self.ultimo.sig = None
        self.largo -= 1

    def eliminar_dato(self, dato):
        """
        5. eliminar dato: elimina el primer nodo que encuentra con el dato
        buscado, arrancando desde el principio, si lo encuentra.
        """
        nodo = self.cabeza
        while nodo is not None:
            if nodo.dato == dato:
                if nodo.ant is None:
                    self.cabeza = nodo.sig
                else:
                    nodo.ant.sig = nodo.sig
                if nodo.sig is None:
                    self.ultimo = nodo.ant
                else:
                    nodo.sig.ant = nodo.ant
                self.largo -= 1
                return
            nodo = nodo.sig

    def longitud(self):
        """
        6. longitud: Devuelve la cantidad de datos guardados en la lista.
        """
        return self.largo


lista = ListaDoblementeEnlazada()

assert (str(lista) == "")
assert (lista.longitud() == 0)

for i in range(5):
    lista.agregar_al_principio(i)

assert (str(lista) == "4 3 2 1 0")
assert (lista.longitud() == 5)

for i in range(5):
    lista.agregar_al_final(i)

assert (str(lista) == "4 3 2 1 0 0 1 2 3 4")
assert (lista.longitud() == 10)

for i in range(3):
    lista.eliminar_al_principio()

assert (str(lista) == "1 0 0 1 2 3 4")
assert (lista.longitud() == 7)

for i in range(3):
    lista.eliminar_al_final()

assert (str(lista) == "1 0 0 1")
assert (lista.longitud() == 4)

lista.eliminar_dato(2)
assert (str(lista) == "1 0 0 1")
assert (lista.longitud() == 4)

lista.eliminar_dato(0)
assert (str(lista) == "1 0 1")
assert (lista.longitud() == 3)

lista.eliminar_dato(1)
assert (str(lista) == "0 1")
assert (lista.longitud() == 2)

lista.eliminar_dato(1)
assert (str(lista) == "0")
assert (lista.longitud() == 1)

lista.eliminar_dato(0)
assert (str(lista) == "")
assert (lista.longitud() == 0)
