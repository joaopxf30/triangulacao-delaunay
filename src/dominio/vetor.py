import math


class Vetor:
    def __init__(self, x: float, y: float, z: float = 0):
        self.coord_x = x
        self.coord_y = y
        self.coord_z = z

    def __mul__(self, entidade: float) -> "Vetor":
        match entidade:
            case float():
                return self.__calcula_produto_escalar(entidade)

            case _:
                raise TypeError("Somente produto escalar está implementado")

    def __calcula_produto_escalar(self, escalar: float) -> "Vetor":
        if escalar <= 0:
            raise ValueError("Parâmetro deve ser maior que 0")

        coord_x = escalar * self.coord_x
        coord_y = escalar * self.coord_y

        return Vetor(coord_x, coord_y)

    def calcula_norma_euclidiana(self) -> float:
        p_norma_2 = math.sqrt(self.coord_x**2 + self.coord_y**2)

        return p_norma_2

    def calcula_produto_interno(self, vetor: "Vetor") -> float:
        produto_interno = (
            self.coord_x * vetor.coord_x +
            self.coord_y * vetor.coord_y +
            self.coord_z * vetor.coord_z
        )

        return produto_interno

    def calcula_produto_vetorial(self, vetor: "Vetor") -> "Vetor":
        coord_x = self.coord_y * vetor.coord_z - self.coord_z * vetor.coord_y
        coord_y = self.coord_z * vetor.coord_x - self.coord_x * vetor.coord_y
        coord_z = self.coord_x * vetor.coord_y - self.coord_y * vetor.coord_x

        return Vetor(coord_x, coord_y, coord_z)

    def normaliza(self) -> "Vetor":
        fator_normalizacao = 1/(self.calcula_norma_euclidiana())
        vetor_unitario = self * fator_normalizacao

        return vetor_unitario

