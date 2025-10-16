from collections import defaultdict

from src.dominio import Ponto, Triangulo, Segmento


class TriangulosPorAresta:
    def __init__(self):
        self._triangulos_por_aresta: defaultdict[frozenset[Ponto], list[Triangulo]] = defaultdict(list)

    def adiciona(self, triangulo: Triangulo):
        for aresta in triangulo.arestas:
            vertices = self._usa_par_vertices(aresta)

            self._triangulos_por_aresta[vertices].append(triangulo)

    def remove(self, triangulo: Triangulo):
        for aresta in triangulo.arestas:
            vertices = self._usa_par_vertices(aresta)

            triangulos = self._triangulos_por_aresta.get(vertices)
            triangulos.remove(triangulo)

    def obtem_triangulos(self, vertices: frozenset[Ponto]) -> list[Triangulo]:
        triangulos = self._triangulos_por_aresta.get(vertices)

        return triangulos

    def obtem_todos_triangulos(self) -> list[Triangulo]:
        todos_triangulos = []
        for triangulos in self._triangulos_por_aresta.values():
            todos_triangulos.extend(triangulos)

        return todos_triangulos

    @staticmethod
    def _usa_par_vertices(aresta: Segmento) -> frozenset[Ponto]:
        par_vertices = frozenset(
            {aresta.vertice_inicial, aresta.vertice_final}
        )

        return par_vertices