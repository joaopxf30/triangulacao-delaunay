import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from src.dominio import Triangulo, Ponto


def plota_triangulacao(triangulacao: set[Triangulo]):
    fig, ax = plt.subplots()

    vertices_triangulos = []
    for vertices_triangulo in triangulacao:
        vertices = []
        for vertice_poligono in vertices_triangulo.vertices:
            vertices.append((vertice_poligono.coord_x, vertice_poligono.coord_y))

        vertices_triangulos.append(vertices)

    for vertices_triangulo in vertices_triangulos:
        triangulo_plot = Polygon(vertices_triangulo, closed=True, edgecolor="black", facecolor="lightcoral")
        ax.add_patch(triangulo_plot)

    ax.plot([], [], ".", color="black")

    ax.set_xlabel(r"$x$", fontsize=12)
    ax.set_ylabel(r"$y$", fontsize=12)

    ax.set_aspect("equal")

    plt.show()


def plota_pontos(pontos: list[Ponto]):
    fig, ax = plt.subplots()

    coords_x = [ponto.coord_x for ponto in pontos]
    coords_y = [ponto.coord_y for ponto in pontos]

    ax.plot(coords_x, coords_y, "o", color="black", markersize=2)

    ax.set_xlabel(r"$x$", fontsize=12)
    ax.set_ylabel(r"$y$", fontsize=12)

    ax.set_aspect("equal")

    plt.show()


def plota_analise_complexidade(tamanhos, tempos):
    plt.plot(tamanhos, tempos, marker='o', linestyle='-', color='blue')
    plt.title(r"Análise do limite superior assintótico", fontsize=14)

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    plt.xlabel("$n$", fontsize=14)
    plt.ylabel(r"Tempo de CPU ($s$)", fontsize=14)

    plt.grid(True)

    plt.savefig("analise_complexidade.pdf", format="pdf")

    plt.show()
