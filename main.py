from src.dominio import Circulo, Ponto
from src.nuvem_pontos import gera_nuvem_pontos
from src.triangulacao_delaunay import TriangulacaoDelaunay
from src.triangulos_por_aresta import TriangulosPorAresta

if __name__ == '__main__':
    pontos = gera_nuvem_pontos(
        numero_pontos=20,
        circulo=Circulo(
            centro=Ponto(x=-15.0, y=-0.0),
            raio=3
        )
    )
    triangulacao_delaunay = TriangulacaoDelaunay(TriangulosPorAresta())
    triangulacao_delaunay.realiza_triangulacao(pontos)
