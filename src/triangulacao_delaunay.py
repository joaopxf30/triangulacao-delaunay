import random

from collections import defaultdict
from src.dominio import Ponto, Segmento
from src.dominio import Triangulo
from src.dominio.triangulacao_dag import TriangulacaoDAG
from src.plot import plota_triangulacao


class TriangulacaoDelaunay:
    def __init__(self):
        self._incidencia_arestas: defaultdict[frozenset[Ponto], list[Triangulo]] = defaultdict(list)

    def realiza_triangulacao(self, pontos: list[Ponto]):
        triangulo_envolvente = self._cria_triangulo_envolvente(pontos)
        random.shuffle(pontos)
        dag = TriangulacaoDAG(triangulo_envolvente)

        for ponto in pontos:
            sub_dag = self._localiza_ponto_na_dag(ponto, dag)

            triangulos = sub_dag.triangulo.subdivide(ponto)
            for triangulo in triangulos:
                self._atualiza_incidencia_arestas(triangulo)
                self._checa_arestas_legais(ponto, triangulo)

            sub_sub_dags = [TriangulacaoDAG(triangulo) for triangulo in triangulos]
            sub_dag.sub_dags = sub_sub_dags

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
        ponto_triangulo_2 = Ponto(x=centro.coord_x + 3*semi_lado, y=centro.coord_y)
        ponto_triangulo_3 = Ponto(x=centro.coord_x, y=centro.coord_y + 3*semi_lado)

        triangulo_envolvente = Triangulo([ponto_triangulo_1, ponto_triangulo_2, ponto_triangulo_3])

        return triangulo_envolvente

    def _atualiza_incidencia_arestas(self, triangulo: Triangulo):
        for aresta in triangulo.arestas:
            par_vertices = frozenset(
                {aresta.vertice_inicial, aresta.vertice_final}
            )

            self._incidencia_arestas[par_vertices].append(triangulo)

    def _localiza_ponto_na_dag(self, ponto: Ponto, dag: TriangulacaoDAG) -> TriangulacaoDAG:
        if dag.sub_dags is None:
            return dag

        for dag in dag.sub_dags:
            triangulo = dag.triangulo

            if triangulo.localiza_ponto_interno(ponto):
                if dag.sub_dags is None:
                    return dag
                else:
                    return self._localiza_ponto_na_dag(ponto, dag)

        assert False, "Ponto tem que pertencer a um triângulo da DAG!"

    def _checa_arestas_legais(self, ponto: Ponto, triangulo: Triangulo) -> bool:
        par_vertices_comum = set(triangulo.vertices) - {ponto}
        triangulo_incidente = self._incidencia_arestas.get(frozenset(par_vertices_comum))

        if len(triangulo_incidente) == 1:
            return True



        print("hi")