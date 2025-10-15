from enum import Enum, auto


class Orientacao(Enum):
    COLINEAR = auto()
    DIREITA = auto()
    ESQUERDA = auto()


class Classificacao(Enum):
    LEGAL = auto()
    ILEGAL = auto()