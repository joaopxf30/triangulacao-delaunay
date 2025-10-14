from itertools import pairwise
from src.dominio.ponto import Ponto
from src.dominio.segmento import Segmento


class Poligono:
    def __init__(self, vertices: list[Ponto]):
        self.vertices = vertices
        self.arestas: list[Segmento] = self._determina_arestas()

    def _determina_arestas(self) -> list[Segmento]:
        ciclo_vertices = [*self.vertices, self.vertices[0]]
        arestas = []

        for vertice_anterior, vertice_posteior in pairwise(ciclo_vertices):
            aresta = Segmento(vertice_anterior, vertice_posteior)
            arestas.append(aresta)

        return arestas
