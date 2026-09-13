# Ejercicio 3

class ArbolBinario:
    def __init__(self, valor=None, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

    def contar_nodos(self):
        ret = 1
        if self.izquierda is not None:
            ret += self.izquierda.contar_nodos()
        if self.derecha is not None:
            ret += self.derecha.contar_nodos()
        return ret

    def sumar_valores(self):
        ret = self.valor
        if self.izquierda is not None:
            ret += self.izquierda.sumar_valores()
        if self.derecha is not None:
            ret += self.derecha.sumar_valores()
        return ret


def contar_nodos(arbol: 'ArbolBinario'):
    if arbol is None:
        return 0
    return 1 + contar_nodos(arbol.izquierda) + contar_nodos(arbol.derecha)


def sumar_valores(arbol: 'ArbolBinario'):
    if arbol is None:
        return 0
    return arbol.valor + sumar_valores(arbol.izquierda) + sumar_valores(arbol.derecha)


arbol = ArbolBinario(1,
                     ArbolBinario(2,
                                  ArbolBinario(3), ArbolBinario(4)),
                     ArbolBinario(5,
                                  ArbolBinario(6), ArbolBinario(7)),
                     )

assert (arbol.contar_nodos() == 7)
assert (arbol.sumar_valores() == 28)

assert (contar_nodos(arbol) == 7)
assert (sumar_valores(arbol) == 28)
