# Ejercicio 1

class Pila:
    def __init__(self):
        pass

    def apilar(self):
        pass

    def desapilar(self):
        pass

    def esta_vacia(self):
        pass


class Cola:
    def __init__(self):
        pass

    def encolar(self):
        pass

    def desencolar(self):
        pass

    def esta_vacia(self):
        pass


class Pagina:
    def __init__(self):
        pass

    def __str__(self):
        pass


class Navegador:
    def __init__(self):
        self.historial = Pila()
        self.avance = Pila()
        self.pagina_actual = None

    def visitar(self, pagina: Pagina):
        self.historial.apilar(self.pagina_actual)
        self.pagina_actual = pagina
        while not self.avance.esta_vacia():
            self.avance.desapilar()

    def atras(self):
        if self.historial.esta_vacia():
            print("ERROR: El historial está vacío")
            return
        self.avance.apilar(self.pagina_actual)
        self.pagina_actual = self.historial.desapilar()

    def adelante(self):
        if self.avance.esta_vacia():
            print("ERROR: El avance está vacío")
            return
        self.historial.apilar(self.pagina_actual)
        self.pagina_actual = self.avance.desapilar()

    def mostrar_pagina_actual(self) -> None:
        if self.pagina_actual is None:
            print("No hay página actual")
            return
        print(self.pagina_actual)
