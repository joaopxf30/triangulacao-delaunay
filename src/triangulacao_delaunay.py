import random

from src.dominio import Ponto
from src.dominio import Triangulo
from src.plot import plota_triangulacao


class TriangulacaoDelaunay:

    def realiza_triangulacao(self, pontos: list[Ponto]):
        triangulo_envolvente = self._cria_triangulo_envolvente(pontos)
        random.shuffle(pontos)
        self._localiza_pontos(pontos, triangulo_envolvente)


    @staticmethod
    def _cria_triangulo_envolvente(pontos: list[Ponto]) -> Triangulo:
        coords_x = [ponto.coord_x for ponto in pontos]
        coords_y = [ponto.coord_y for ponto in pontos]

        coord_x_min = min(coords_x)
        coord_x_max = max(coords_x)
        coord_y_min = min(coords_y)
        coord_y_max = max(coords_y)

        centro = Ponto(
            x=(coord_x_min + coord_x_max) / 2,
            y=(coord_y_min + coord_y_max) / 2,
        )

        semi_lado = max(coord_x_max - coord_x_min, coord_y_max - coord_y_min) / 2

        ponto_triangulo_1 = Ponto(x=centro.coord_x - 3*semi_lado, y=centro.coord_y - 3*semi_lado)
        ponto_triangulo_2 = Ponto(x=centro.coord_x, y=centro.coord_y + 3*semi_lado)
        ponto_triangulo_3 = Ponto(x=centro.coord_x + 3*semi_lado, y=centro.coord_y)

        triangulo_envolvente = Triangulo([ponto_triangulo_1, ponto_triangulo_2, ponto_triangulo_3])

        return triangulo_envolvente

    @staticmethod
    def _localiza_pontos(pontos: list[Ponto], triangulo_envolvente: Triangulo):
        for ponto in pontos:
            if ponto in
