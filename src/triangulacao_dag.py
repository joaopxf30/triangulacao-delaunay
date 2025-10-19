from src.dominio import Triangulo, Ponto


class TriangulacaoDAG:
    def __init__(
        self,
        triangulo: Triangulo,
        sub_dags: list["TriangulacaoDAG"] = None
    ):
        self.mapeamento = {}
        self.triangulo = triangulo
        self.sub_dags = self.__criacao_subdags(sub_dags)
        self.atualiza_mapeamento(triangulo, self.sub_dags)

    @staticmethod
    def __criacao_subdags(subdags: list["TriangulacaoDAG"] | None):
        if subdags is None:
            return []

        return subdags

    def localiza_ponto(self, ponto: Ponto) -> "TriangulacaoDAG":
        if not self.sub_dags:
            return self

        for sub_triangulo in self.sub_dags:
            triangulo = sub_triangulo.triangulo

            if triangulo.localiza_ponto_interno(ponto):
                if not sub_triangulo.sub_dags:
                    return sub_triangulo
                else:
                    return sub_triangulo.localiza_ponto(ponto)

        assert False, "Ponto tem que pertencer a um triângulo da DAG!"

    def atualiza_mapeamento(
        self,
        triangulo: Triangulo,
        sub_dags: list["TriangulacaoDAG"]
    ):
        sub_dags_existentes = self.mapeamento.get(triangulo)

        if sub_dags_existentes is None:
            self.mapeamento[triangulo] = sub_dags
        else:
            sub_dags_existentes.clear()
            sub_dags_existentes.extend(sub_dags)
