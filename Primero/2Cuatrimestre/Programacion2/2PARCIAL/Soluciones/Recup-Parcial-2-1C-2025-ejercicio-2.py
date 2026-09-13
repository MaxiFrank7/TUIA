# Ejercicio 2

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

    def cima(self):
        return self.items[-1] if not self.esta_vacia() else None

    def tamanio(self):
        """
        1. tamanio: Devuelve la cantidad de elementos en la pila.
        """
        return len(self.items)

    def limpia(self):
        """
        2. limpia: Elimina todos los elementos de la pila.
        """
        self.items = []

    def copiar(self):
        """
        3. copiar: Devuelve una nueva pila que es una copia de la pila actual.
        """
        ret = Pila()
        for item in self.items:
            ret.apilar(item)
        return ret


pila = Pila()

for i in range(10):
    pila.apilar(i)

assert (pila.tamanio() == 10)

pila.limpia()
assert (pila.esta_vacia())

copia = pila.copiar()
assert (copia.esta_vacia())

for i in range(10):
    pila.apilar(i)

copia = pila.copiar()
assert (copia.tamanio() == 10)
