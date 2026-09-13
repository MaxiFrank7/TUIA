# Ejercicio 3

from typing import Any


class GrafoDirigido:
    def __init__(self) -> None:
        self.vertices = []
        self.vecinos = {}

    def add_node(self, vertice: Any) -> None:
        self.vertices.append(vertice)
        self.vecinos[vertice] = []

    def add_edge(self, vertice1: Any, vertice2: Any) -> None:
        if vertice1 not in self.vertices:
            print(f"ERROR: no existe vertice {vertice1}")
            return

        if vertice2 not in self.vertices:
            print(f"ERROR: no existe vertice {vertice2}")
            return

        self.vecinos[vertice1].append(vertice2)

    def get_adjacent(self, vertice: Any) -> Any:
        if vertice not in self.vertices:
            print(f"ERROR: no existe vertice {vertice}")
            return

        return self.vecinos[vertice]

    def get_nodes(self) -> list[Any]:
        return self.vertices

    def remove_edge(self, x, y):
        """
        Remueve la arista dirigida entre el nodo x y el nodo y (si existe).
        """
        if x not in self.vertices:
            print(f"ERROR: no existe vertice {x}")
            return

        if y not in self.vertices:
            print(f"ERROR: no existe vertice {y}")
            return

        if y not in self.vecinos[x]:
            print(f"ERROR: no existe arista {(x, y)}")
            return

        self.vecinos[x].remove(y)

    def remove_node(self, x):
        """
        Remueve el nodo x del grafo. Si había aristas que salían o llegaban a
        este nodo, también deben borrar del grafo.
        """
        if x not in self.vertices:
            print("ERROR: no existe vertice {x}")
            return

        for i in self.vertices:
            if x in self.vecinos[i]:
                self.vecinos[i].remove(x)

        self.vertices.remove(x)
        self.vecinos.pop(x)

    def are_adjacent(self, x, y) -> bool:
        """
        Devuelve True si x apunta a y, False en caso contrario.
        """
        if x not in self.vertices:
            print(f"ERROR: no existe vertice {x}")
            return

        if y not in self.vertices:
            print(f"ERROR: no existe vertice {y}")
            return

        return y in self.vecinos[x]

    def get_outdegree(self, v) -> int:
        """
        Devuelve el grado de salida(outdegree) del vértice, que es el número de
        aristas que salen de él.
        """
        if v not in self.vertices:
            print(f"ERROR: no existe vertice {v}")
            return -1

        return len(self.vecinos[v])

    def get_indegree(self, v) -> int:
        """
        Devuelve el grado de salida(indegree) del vértice, que es el número de
        aristas que llegan a él.
        """
        if v not in self.vertices:
            print(f"ERROR: no existe vertice {v}")
            return -1

        ret = 0
        for i in self.vertices:
            ret += self.vecinos[i].count(v)
        return ret


# Ejemplo de uso
grafo = GrafoDirigido()

grafo.add_node("A")
grafo.add_node("B")
grafo.add_node("C")

grafo.add_edge("A", "B")
grafo.add_edge("A", "C")
grafo.add_edge("B", "C")

assert (grafo.get_nodes() == ["A", "B", "C"])
assert (grafo.get_adjacent("A") == ["B", "C"])
assert (grafo.get_adjacent("B") == ["C"])
assert (grafo.get_adjacent("C") == [])

grafo.remove_edge("D", "A")
grafo.remove_edge("C", "A")
grafo.remove_edge("A", "C")

assert (grafo.get_nodes() == ["A", "B", "C"])
assert (grafo.get_adjacent("A") == ["B"])
assert (grafo.get_adjacent("B") == ["C"])
assert (grafo.get_adjacent("C") == [])

grafo.remove_node("B")

assert (grafo.get_nodes() == ["A", "C"])
assert (grafo.get_adjacent("A") == [])
assert (grafo.get_adjacent("C") == [])

grafo.add_node("D")
grafo.add_node("E")
grafo.add_node("F")

grafo.add_edge("D", "A")
grafo.add_edge("D", "C")
grafo.add_edge("D", "E")
grafo.add_edge("D", "F")

assert (grafo.get_nodes() == ["A", "C", "D", "E", "F"])
assert (grafo.get_adjacent("A") == [])
assert (grafo.get_adjacent("C") == [])
assert (grafo.get_adjacent("D") == ["A", "C", "E", "F"])
assert (grafo.get_adjacent("E") == [])
assert (grafo.get_adjacent("F") == [])

assert (grafo.are_adjacent("D", "A"))
assert (not grafo.are_adjacent("A", "D"))
assert (grafo.are_adjacent("D", "C"))
assert (not grafo.are_adjacent("C", "D"))

assert (grafo.get_indegree("A") == 1)
assert (grafo.get_indegree("D") == 0)
assert (grafo.get_outdegree("A") == 0)
assert (grafo.get_outdegree("D") == 4)
