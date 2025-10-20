import time
from src.dominio import Circulo, Ponto
from src.nuvem_pontos import gera_nuvem_pontos
from src.plot import plota_triangulacao, plota_pontos, plota_analise_complexidade
from src.triangulacao_delaunay import TriangulacaoDelaunay
from src.triangulos_por_aresta import TriangulosPorAresta

TAMANHOS = list(range(10000, 510000, 10000))


def triangula(_pontos: list[Ponto]) -> float:
    start = time.process_time()
    triangulacao_delaunay = TriangulacaoDelaunay(TriangulosPorAresta())
    _ = triangulacao_delaunay.realiza_triangulacao(_pontos)
    end = time.process_time()
    tempo_cpu = end - start

    return tempo_cpu


if __name__ == '__main__':
    tempos_cpu = []
    for tamanho in TAMANHOS:
        pontos = gera_nuvem_pontos(
            numero_pontos=tamanho,
            circulo=Circulo(
                centro=Ponto(x=0.0, y=0.0),
                raio=3
            )
        )

        print(f"Inicia triangulação com {tamanho} pontos.")
        tempo_cpu = triangula(pontos)
        print(f"Finaliza triangulação com {tamanho} pontos.")
        print(f"Tempo: {tempo_cpu}\n")

        tempos_cpu.append(tempo_cpu)

    plota_analise_complexidade(TAMANHOS, tempos_cpu)
