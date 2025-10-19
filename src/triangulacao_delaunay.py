import random

from src.dominio import Ponto, Circulo
from src.dominio import Triangulo
from src.plot import plota_triangulacao, plota_triangulacao_2
from src.triangulacao_dag import TriangulacaoDAG
from src.triangulos_por_aresta import TriangulosPorAresta


class TriangulacaoDelaunay:
    def __init__(self, estrutura_dados: TriangulosPorAresta):
        self._estrutura_dados = estrutura_dados

    def realiza_triangulacao(self, pontos: list[Ponto]):
        triangulo_envolvente = self._cria_triangulo_envolvente(pontos)
        self._estrutura_dados.adiciona(triangulo_envolvente)
        dag = TriangulacaoDAG(triangulo_envolvente)
        random.shuffle(pontos)

        for ponto in pontos:
            sub_dag = dag.localiza_ponto(ponto)

            triangulo_envolvente = sub_dag.triangulo

            plota_triangulacao_2([ponto], self._estrutura_dados.obtem_todos_triangulos(), triangulo_envolvente)

            self._estrutura_dados.remove(triangulo_envolvente)
            triangulos = triangulo_envolvente.subdivide(ponto)

            sub_sub_dags = []
            for triangulo in triangulos:
                sub_sub_dag = TriangulacaoDAG(triangulo)
                sub_sub_dags.append(sub_sub_dag)
                dag.atualiza_mapeamento(triangulo, sub_sub_dag.sub_dags)
                self._estrutura_dados.adiciona(triangulo)

            sub_dag.sub_dags = sub_sub_dags
            dag.atualiza_mapeamento(triangulo_envolvente, sub_sub_dags)

            plota_triangulacao([ponto], self._estrutura_dados.obtem_todos_triangulos())

            self._realiza_triangulacao(triangulos, ponto, dag)

    def _realiza_triangulacao(self, triangulos: list[Triangulo], ponto: Ponto, dag: TriangulacaoDAG):
        for triangulo in triangulos:
            vertices = self._retorna_vertices_complementares(triangulo, ponto)
            triangulos_adjacentes = self._estrutura_dados.obtem_triangulos(vertices)

            plota_triangulacao_2([ponto], self._estrutura_dados.obtem_todos_triangulos(), triangulo)

            if ponto_comparacao := self._obtem_ponto_comparacao(triangulos_adjacentes, triangulo, vertices):
                if not self._checa_legalidade_aresta(ponto_comparacao, triangulo):
                    triangulo_adjacente_1 = triangulos_adjacentes[0]
                    triangulo_adjacente_2 = triangulos_adjacentes[1]
                    sub_dags = self._vira_aresta(
                        triangulo_adjacente_1,
                        triangulo_adjacente_2,
                        vertices
                    )
                    # plota_triangulacao_2([ponto], self._estrutura_dados.obtem_todos_triangulos(), triangulo_adjacente_1)
                    # plota_triangulacao_2([ponto], self._estrutura_dados.obtem_todos_triangulos(), triangulo_adjacente_2)
                    # plota_triangulacao([ponto], self._estrutura_dados.obtem_todos_triangulos())
                    dag.atualiza_mapeamento(sub_dags[0].triangulo, sub_dags[0].sub_dags)
                    dag.atualiza_mapeamento(sub_dags[1].triangulo, sub_dags[1].sub_dags)
                    dag.atualiza_mapeamento(triangulo_adjacente_1, sub_dags)
                    dag.atualiza_mapeamento(triangulo_adjacente_2, sub_dags)

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

        ponto_inicial = Ponto(x=centro.coord_x - 3*semi_lado, y=centro.coord_y - 3*semi_lado)
        ponto_itermediario = Ponto(x=centro.coord_x + 3*semi_lado, y=centro.coord_y)
        ponto_final = Ponto(x=centro.coord_x, y=centro.coord_y + 3*semi_lado)

        triangulo_envolvente = Triangulo([ponto_inicial, ponto_itermediario, ponto_final])

        return triangulo_envolvente

    @staticmethod
    def _retorna_vertices_complementares(triangulo: Triangulo, ponto: Ponto) -> frozenset[Ponto]:
        vertices = frozenset(triangulo.vertices) - {ponto}

        return vertices

    @staticmethod
    def _obtem_ponto_comparacao(
        triangulos_candidatos: list[Triangulo],
        triangulo_exclusao: Triangulo,
        vertices_exclusao: frozenset[Ponto],
    ) -> Ponto | None:
        triangulo_interesse = next(
            (triangulo for triangulo in triangulos_candidatos if triangulo != triangulo_exclusao),
            None
        )

        if triangulo_interesse is None:
            return None
        else:
            ponto = set(triangulo_interesse.vertices) - vertices_exclusao
            return ponto.pop()

    @staticmethod
    def _checa_legalidade_aresta(ponto: Ponto, triangulo: Triangulo) -> bool:
        vertices = triangulo.vertices
        circulo_circunscrito = Circulo.inicializa_por_tres_pontos(vertices[0], vertices[1], vertices[2])
        vetor = ponto - circulo_circunscrito.centro
        distancia = vetor.calcula_norma_euclidiana()

        return distancia > circulo_circunscrito.raio

    def _vira_aresta(
        self,
        triangulo_adjacente_1: Triangulo,
        triangulo_adjacente_2: Triangulo,
        vertices: frozenset[Ponto]
    ) -> list[TriangulacaoDAG]:
        self._estrutura_dados.remove(triangulo_adjacente_1)
        self._estrutura_dados.remove(triangulo_adjacente_2)

        triangulo_1 = self._constroi_novo_triangulo(
            triangulo_adjacente_1,
            triangulo_adjacente_2,
            vertices
        )
        triangulo_2 = self._constroi_novo_triangulo(
            triangulo_adjacente_2,
            triangulo_adjacente_1,
            vertices
        )

        self._estrutura_dados.adiciona(triangulo_1)
        self._estrutura_dados.adiciona(triangulo_2)

        return [TriangulacaoDAG(triangulo_1), TriangulacaoDAG(triangulo_2)]

    @staticmethod
    def _constroi_novo_triangulo(
        triangulo_referencia_1: Triangulo,
        triangulo_referencia_2: Triangulo,
        vertices: frozenset[Ponto],
    ) -> Triangulo:
        vertice_inicio = (set(triangulo_referencia_1.vertices) - vertices).pop()
        vertice_final = (set(triangulo_referencia_2.vertices) - vertices).pop()

        for aresta in triangulo_referencia_1.arestas:
            if aresta.vertice_inicial == vertice_inicio:
                vertice_intermediario = aresta.vertice_final
                break
        else:
            assert False, "Deve ser garantido que o vértice seja encontrado"

        return Triangulo([vertice_inicio, vertice_intermediario, vertice_final])
