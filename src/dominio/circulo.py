import numpy as np
from src.dominio.ponto import Ponto


class Circulo:
    def __init__(self, centro: Ponto, raio: float):
        self.centro = centro
        self.raio = raio

    def __str__(self):
        return f"Centro: {(self.centro.coord_x,self.centro.coord_y)}, Raio: {self.raio}"

    @staticmethod
    def inicializa_por_dois_pontos(ponto_1: Ponto, ponto_2: Ponto) -> "Circulo":
        centro = ponto_1.busca_ponto_medio(ponto_2)
        raio = (ponto_1 - ponto_2).calcula_norma_euclidiana() / 2

        return Circulo(centro, raio)

    @staticmethod
    def inicializa_por_tres_pontos(ponto_1: Ponto, ponto_2: Ponto, ponto_3: Ponto) -> "Circulo":
        """ Gera um circuncírculo formado pelos três pontos informados. A determinação
        do centro do círculo é feito resolvendo o sistema de equações formado a partir
        do fato de que a distância entre qualquer um dos três pontos para o centro é
        constante, já que o centro desse círculo é o circuncentro do triângulo formado
        pelos três pontos. O raio é a distância entre o circucnentro é qualquer um dos
        vértices.
        """
        def _calcula_coeficiente_equacao(_ponto_1: Ponto, _ponto_2: Ponto) -> list[float]:
            coficente_equacoes = [_ponto_1.coord_x - _ponto_2.coord_x, _ponto_1.coord_y - _ponto_2.coord_y]

            return coficente_equacoes

        def _calcula_termo_independente(_ponto_1: Ponto, _ponto_2: Ponto) -> float:
            termo_independente = (
                (_ponto_1.coord_x**2 + _ponto_1.coord_y**2 -
                _ponto_2.coord_x**2 - _ponto_2.coord_y**2)/2
            )

            return termo_independente

        coeficientes_equacao_1 = _calcula_coeficiente_equacao(ponto_1, ponto_2)
        coeficientes_equacao_2 = _calcula_coeficiente_equacao(ponto_2, ponto_3)
        coeficientes = np.array([coeficientes_equacao_1, coeficientes_equacao_2])

        termo_independente_equacao_1 = _calcula_termo_independente(ponto_1, ponto_2)
        termo_independente_equacao_2 = _calcula_termo_independente(ponto_2, ponto_3)
        termos_independentes = np.array([termo_independente_equacao_1, termo_independente_equacao_2])

        coordendas_centro = np.linalg.solve(coeficientes, termos_independentes)
        centro = Ponto(float(coordendas_centro[0]), float(coordendas_centro[1]))
        raio = (ponto_1 - centro).calcula_norma_euclidiana()

        return Circulo(centro, raio)
