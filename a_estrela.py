import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


# Função de heurística (distância estimada entre cidades)
def heuristic(city, goal):
    heuristic_values = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 0
    }
    return heuristic_values.get(city, 0)


# Função para desenhar o grafo
def draw_graph():
    # Criando o grafo
    G = nx.Graph()

    # Adicionando nós (cidades)
    cities = ['A', 'B', 'C', 'D']
    G.add_nodes_from(cities)

    # Adicionando arestas (estradas com distâncias)
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1)
    ]
    G.add_weighted_edges_from(edges)

    # Definindo as posições dos nós manualmente para melhor visualização
    pos = {
        'A': (0, 0),
        'B': (1, 1),
        'C': (1, -1),
        'D': (2, 0)
    }

    # Desenhando o grafo
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=16, font_weight="bold",
            edge_color="gray")
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d} km' for u, v, d in edges}, font_size=12)

    # Exibindo o grafo no Streamlit
    st.pyplot(plt)


# Função para exibir os resultados no Streamlit
def show_astar():
    st.title("Algoritmo de Busca A*")

    # Introdução ao Algoritmo A*
    st.header("Introdução ao Algoritmo A*")
    st.write("""
    O **A*** é um algoritmo de busca heurística utilizado para encontrar o caminho mais curto entre dois pontos em um grafo. Ele combina as melhores características de busca em largura e profundidade, usando uma função heurística para guiar a exploração de caminhos mais promissores.

    No exemplo abaixo, utilizamos cidades conectadas por estradas e uma estimativa de distância até a cidade objetivo como a função heurística.
    """)

    # Desenho do grafo das cidades
    st.header("Grafo de Cidades")
    draw_graph()

    # Características do Algoritmo A*
    st.header("Características do Algoritmo A*")
    st.write("""
    O algoritmo A* possui as seguintes características principais:

    - **Ótimo e Completo**: Se existir um caminho para o objetivo, A* garantirá encontrar o caminho mais curto.
    - **Heurística**: Usa uma função heurística \( h(n) \) para guiar a busca, estimando a distância do nó atual ao objetivo.
    - **Função Custo**: Combina o custo real percorrido \( g(n) \) e a estimativa do custo futuro \( h(n) \) para avaliar os nós.
    - **Exploração Inteligente**: Busca os caminhos mais promissores primeiro, otimizando a exploração.
    """)

    # Vantagens do Algoritmo A*
    st.header("Vantagens do Algoritmo A*")
    st.write("""
    As principais vantagens do A* são:

    - **Ótimo**: Encontra o caminho mais curto para o objetivo.
    - **Flexível**: Funciona com uma variedade de heurísticas, podendo ser ajustado para diferentes problemas.
    - **Heurística Informada**: O uso de uma heurística permite uma exploração mais eficiente do espaço de busca.
    - **Adaptável**: Pode ser utilizado em diferentes contextos, como rotas de GPS, jogos, entre outros.
    """)

    # Desvantagens do Algoritmo A*
    st.header("Desvantagens do Algoritmo A*")
    st.write("""
    O algoritmo A* também apresenta algumas desvantagens:

    - **Custo Computacional**: Em problemas de larga escala, A* pode consumir muita memória e tempo de processamento.
    - **Qualidade da Heurística**: A eficácia do algoritmo depende muito da qualidade da função heurística utilizada.
    - **Grande Quantidade de Nós**: Para grafos muito grandes ou complexos, a quantidade de nós abertos pode ser muito alta.
    """)

    # Fórmulas Utilizadas
    st.subheader("Fórmulas Utilizadas")
    st.latex(r'f(n) = g(n) + h(n)')
    st.write("""
    Onde:
    - \( f(n) \) é o custo estimado total de um nó \( n \) (custo real + custo estimado).
    - \( g(n) \) é o custo real do caminho do nó inicial até o nó \( n \).
    - \( h(n) \) é a função heurística que estima o custo do nó \( n \) até o nó objetivo.
    """)

    # Exemplo com cidades
    st.subheader("Exemplo: Busca de Caminho entre Cidades")
    st.write("""
    Vamos usar um exemplo com quatro cidades: **A**, **B**, **C** e **D**. A meta é encontrar o caminho mais curto da cidade **A** para a cidade **D**.

    As distâncias reais entre as cidades são representadas da seguinte forma:
    - A para B: 1 km
    - A para C: 4 km
    - B para C: 2 km
    - B para D: 5 km
    - C para D: 1 km

    Além disso, a **heurística** (estimativa de distância até o objetivo) entre as cidades e a cidade **D** é:
    - A: 7 km
    - B: 6 km
    - C: 2 km
    - D: 0 km (objetivo)
    """)

    # Explicação passo a passo
    st.subheader("Passo a Passo da Busca A*")
    st.write("""
    1. Começamos na cidade **A**.
    - \( g(A) = 0 \), pois estamos na cidade inicial.
    - \( h(A) = 7 \) (estimativa de distância de A até D).
    - \( f(A) = g(A) + h(A) = 0 + 7 = 7 \).

    2. Entre as cidades conectadas a **A**, temos **B** e **C**:
    - Para **B**: \( g(B) = g(A) + \text{distância de A a B} = 0 + 1 = 1 \).
    - \( h(B) = 6 \) (estimativa de distância de B até D).
    - \( f(B) = g(B) + h(B) = 1 + 6 = 7 \).

    - Para **C**: \( g(C) = g(A) + \text{distância de A a C} = 0 + 4 = 4 \).
    - \( h(C) = 2 \) (estimativa de distância de C até D).
    - \( f(C) = g(C) + h(C) = 4 + 2 = 6 \).

    3. Escolhemos a cidade **C** (menor \( f(n) \)).
    - De **C** para **D**: \( g(D) = g(C) + \text{distância de C a D} = 4 + 1 = 5 \).
    - \( h(D) = 0 \), pois chegamos ao destino.
    - \( f(D) = g(D) + h(D) = 5 + 0 = 5 \).

    4. O caminho mais curto encontrado é **A → C → D**, com um custo total de 5 km.
    """)

    # Conclusão
    st.subheader("Conclusão")
    st.write("""
    O algoritmo A* encontra o caminho mais curto ao combinar o custo real percorrido \( g(n) \) e a estimativa de custo futuro \( h(n) \). No exemplo das cidades, o caminho mais eficiente entre **A** e **D** é **A → C → D** com um custo total de 5 km.
    """)


if __name__ == "__main__":
    show_astar()
