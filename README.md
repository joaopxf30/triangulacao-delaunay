# Triangulação de Delaunay com algoritmo incremental com uso de DAG para localização de pontos 

Este projeto, intitulado triangulacao-delauney, implementa o algoritmo incremental com uso de DAG para localização de 
pontos  para realizar a triangulação de Delauney. 
A versão utilizada para desenvolvimento é Python 3.12.3.


---
## Ambientes virtuais

É fortemente recomendado a utilização de ambientes virtuais. Para tal, execute no terminal a partir de um path desejado o seguinte comando de acordo com o sistema operacional:

**WINDOWS**:
```
python -m venv env
```

**OS/LINUX**:
```
python3 -m venv env
```

Para ativação do ambiente virutal, execute o seguinte comando de acordo com a platafoma:

**WINDOWS**:
```
<path>\env\Scripts\Activate.ps1
```

**POSIX**:
```
source <path>/env/bin/activate
```

O ambiente virtual será criado.

## Instalando dependências

Todas as dependências do projeto se encontram no arquivo `requirements.txt`. A obtenção é feita a partir da execução do seguinte comando na raiz do projeto:

```
pip install -r requirements.txt
```

As dependências são instaladas.

## Recomendações de uso

Para acionar o código basta rodar da raiz do projeto

```
python main.py
```

O código realizará o plot da triangulação de Delauney para uma nuvem de pontos contendo `numero_pontos` elementos que é
gerada aleatoriamente a partir de uma distribuição uniforme em área de um círculo centrado em coordenada x em `Ponto.x` 
e coordenada y em `Ponto.y` com raio de tamanho `raio`.

```python
if __name__ == '__main__':
    pontos = gera_nuvem_pontos(
        numero_pontos=100,
        circulo=Circulo(
            centro=Ponto(x=0.0, y=0.0),
            raio=3
        )
    )
    triangulacao_delaunay = TriangulacaoDelaunay(TriangulosPorAresta())
    triangulos = triangulacao_delaunay.realiza_triangulacao(pontos)
    plota_triangulacao(triangulos)
```
