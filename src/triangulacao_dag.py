from src.dominio import Triangulo, Ponto, Segmento


class TriangulacaoDAG:
    def __init__(
        self,
        triangulo: Triangulo,
        sub_dags: list["TriangulacaoDAG"] = None
    ):
        self.triangulo = triangulo
        self.sub_dags = sub_dags
        self.mapeamento = {}

    def localiza_ponto(self, ponto: Ponto) -> "TriangulacaoDAG":
        if self.sub_dags is None:
            return self

        for sub_triangulo in self.sub_dags:
            triangulo = sub_triangulo.triangulo

            if triangulo.localiza_ponto_interno(ponto):
                if sub_triangulo.sub_dags is None:
                    return sub_triangulo
                else:
                    return sub_triangulo.localiza_ponto(ponto)

        assert False, "Ponto tem que pertencer a um triângulo da DAG!"

    def atualiza_mapeamento(
        self,
        triangulo: Triangulo,
        sub_dags: list["TriangulacaoDAG"]
    ):
        self.mapeamento[triangulo] = sub_dags

        return self


