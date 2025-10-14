import math
import random
from src.dominio import Ponto, Circulo


def gera_nuvem_pontos(numero_pontos: int, circulo: Circulo) -> list[Ponto]:
    nuvem_pontos = []

    for i in range(numero_pontos):
        theta = random.uniform(0, 2 * math.pi)
        raio = circulo.raio * math.sqrt(random.uniform(0, 1))
        ponto = Ponto.inicializa_com_coordenadas_polares(circulo.centro, theta, raio)
        nuvem_pontos.append(ponto)

    return nuvem_pontos