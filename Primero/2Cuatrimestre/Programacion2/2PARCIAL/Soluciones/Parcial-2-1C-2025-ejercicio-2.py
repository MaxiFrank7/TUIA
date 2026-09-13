# Ejercicio 2

class BinaryTree:
    def __init__(self, cargo=None, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right


def cantidad_hojas(btree: BinaryTree) -> int:
    if btree.left is None and btree.right is None:
        return 1

    ret = 0
    if btree.left is not None:
        ret += cantidad_hojas(btree.left)
    if btree.right is not None:
        ret += cantidad_hojas(btree.right)

    return ret


def numeros_entre(btree, l, r):
    ret = []

    if l <= btree.cargo and btree.cargo <= r:
        ret += [btree.cargo]

    if btree.left is not None:
        ret += numeros_entre(btree.left, l, r)
    if btree.right is not None:
        ret += numeros_entre(btree.right, l, r)

    return ret


arbol = BinaryTree(1)
assert (cantidad_hojas(arbol) == 1)
assert (numeros_entre(arbol, 3, 6) == [])
assert (numeros_entre(arbol, 0, 1) == [1])


arbol = BinaryTree(1,
                   BinaryTree(2,
                              BinaryTree(3), BinaryTree(4)),
                   BinaryTree(5,
                              BinaryTree(6), BinaryTree(7)),
                   )

assert (cantidad_hojas(arbol) == 4)
assert (numeros_entre(arbol, 3, 6) == [3, 4, 5, 6])
assert (numeros_entre(arbol, 0, 1) == [1])

arbol = BinaryTree(1,
                   BinaryTree(2,
                              BinaryTree(3), BinaryTree(4)),
                   BinaryTree(5)
                   )

assert (cantidad_hojas(arbol) == 3)
assert (numeros_entre(arbol, 3, 6) == [3, 4, 5])
assert (numeros_entre(arbol, 0, 1) == [1])
