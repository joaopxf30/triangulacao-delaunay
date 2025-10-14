from src.dominio import Circulo, Ponto
from src.nuvem_pontos import gera_nuvem_pontos
from src.triangulacao_delaunay import TriangulacaoDelaunay

if __name__ == '__main__':
    pontos = gera_nuvem_pontos(
        numero_pontos=50,
        circulo=Circulo(
            centro=Ponto(x=-15.0, y=-0.0),
            raio=3
        )
    )
    triangulacao_delaunay = TriangulacaoDelaunay()
    triangulacao_delaunay.realiza_triangulacao(pontos)

print(pontos)