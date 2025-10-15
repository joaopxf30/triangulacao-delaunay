from src.dominio import Triangulo


class TriangulacaoDAG:
    def __init__(
        self,
        triangulo: Triangulo,
        sub_dags: list["TriangulacaoDAG"] = None
    ):
        self.triangulo = triangulo
        self.sub_dags = sub_dags
