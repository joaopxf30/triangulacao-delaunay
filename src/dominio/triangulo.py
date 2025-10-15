from collections import defaultdict

from src.constants import Orientacao
from src.dominio import Ponto, Segmento
from src.dominio import Poligono


class Triangulo(Poligono):
    def __init__(self, vertices: list[Ponto]):
        if len(vertices) != 3:
            raise ValueError("Triângulo só admite três vértices")

        super().__init__(vertices)

    def localiza_ponto_interno(self, ponto: Ponto) -> bool:
        for aresta in self.arestas:
            if aresta.localiza_ponto(ponto) != Orientacao.ESQUERDA:
                return False

        return True

    def subdivide(self, ponto: Ponto) -> list["Triangulo"]:
        triangulo_1 = Triangulo([ponto, self.vertices[0], self.vertices[1]])
        triangulo_2 = Triangulo([ponto, self.vertices[1], self.vertices[2]])
        triangulo_3 = Triangulo([ponto, self.vertices[2], self.vertices[0]])

        return [triangulo_1, triangulo_2, triangulo_3]
