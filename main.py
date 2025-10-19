from src.dominio import Circulo, Ponto
from src.nuvem_pontos import gera_nuvem_pontos
from src.plot import plota_triangulacao, plota_pontos
from src.triangulacao_delaunay import TriangulacaoDelaunay
from src.triangulos_por_aresta import TriangulosPorAresta

if __name__ == '__main__':
    pontos = gera_nuvem_pontos(
        numero_pontos=2000,
        circulo=Circulo(
            centro=Ponto(x=-0.0, y=-0.0),
            raio=3
        )
    )
    plota_pontos(pontos)
    triangulacao_delaunay = TriangulacaoDelaunay(TriangulosPorAresta())
    triangulos = triangulacao_delaunay.realiza_triangulacao(pontos)
    plota_triangulacao(triangulos)
