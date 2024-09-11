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


# Função para exibir o grafo das cidades no Streamlit
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
def show_greedy_search():
    st.title("Algoritmo de Busca Gulosa com Grafo")

    # Introdução ao Algoritmo de Busca Gulosa
    st.header("Introdução ao Algoritmo de Busca Gulosa")
    st.write("""
    A **Busca Gulosa** é um algoritmo de busca heurística que escolhe o próximo nó baseado unicamente na função heurística, sem considerar o custo acumulado do caminho até o momento. O objetivo é chegar o mais rapidamente possível ao destino, sempre escolhendo o caminho que parece ser o mais promissor com base na heurística.
    """)

    # Desenho do grafo das cidades
    st.header("Grafo de Cidades")
    draw_graph()

    # Características do Algoritmo de Busca Gulosa
    st.header("Características do Algoritmo de Busca Gulosa")
    st.write("""
    O algoritmo de busca gulosa possui as seguintes características principais:

    - **Heurística**: Usa apenas a função heurística \( h(n) \) para escolher o próximo nó, sem levar em consideração o custo total do caminho percorrido.
    - **Rápido e Simples**: Devido à sua natureza gulosa, é rápido em decidir qual nó explorar em cada etapa.
    - **Não Ótimo**: Não garante encontrar o caminho mais curto, apenas o que parece ser o mais promissor naquele momento.
    """)

    # Vantagens do Algoritmo de Busca Gulosa
    st.header("Vantagens do Algoritmo de Busca Gulosa")
    st.write("""
    As principais vantagens da busca gulosa são:

    - **Simplicidade**: Fácil de implementar e entender, com menos complexidade que algoritmos como A*.
    - **Rápida Tomada de Decisão**: Como usa apenas a heurística, o algoritmo toma decisões rapidamente.
    - **Baixo Custo Computacional**: Para problemas menores, a busca gulosa pode ser eficiente em termos de uso de recursos.
    """)

    # Desvantagens do Algoritmo de Busca Gulosa
    st.header("Desvantagens do Algoritmo de Busca Gulosa")
    st.write("""
    O algoritmo de busca gulosa apresenta algumas desvantagens:

    - **Não Ótimo**: Pode escolher um caminho que parece promissor no início, mas não é o melhor em termos de custo total.
    - **Falta de Consciência do Custo Total**: Ignora o custo acumulado para chegar a um nó, podendo resultar em um caminho mais longo.
    - **Depende Fortemente da Heurística**: Se a heurística não for bem escolhida, o desempenho pode ser muito ruim.
    """)

    # Fórmulas Utilizadas
    st.subheader("Fórmulas Utilizadas")
    st.latex(r'f(n) = h(n)')
    st.write("""
    Onde:
    - \( f(n) \) é o valor da função de avaliação do nó \( n \), baseado apenas na função heurística \( h(n) \).
    - \( h(n) \) é a estimativa do custo do nó \( n \) até o nó objetivo.
    """)

    # Exemplo com cidades
    st.subheader("Exemplo: Busca de Caminho entre Cidades")
    st.write("""
    Vamos usar um exemplo com quatro cidades: **A**, **B**, **C** e **D**. O objetivo é encontrar o caminho da cidade **A** para a cidade **D** usando busca gulosa, apenas considerando a heurística (distância estimada até o objetivo).

    As distâncias reais entre as cidades são representadas da seguinte forma:
    - A para B: 1 km
    - A para C: 4 km
    - B para C: 2 km
    - B para D: 5 km
    - C para D: 1 km

    A **heurística** (estimativa de distância até a cidade **D**) é:
    - A: 7 km
    - B: 6 km
    - C: 2 km
    - D: 0 km (objetivo)
    """)

    # Explicação passo a passo
    st.subheader("Passo a Passo da Busca Gulosa")
    st.write("""
    1. Começamos na cidade **A**.
    - \( h(A) = 7 \).

    2. Entre as cidades conectadas a **A**, temos **B** e **C**:
    - Para **B**: \( h(B) = 6 \) (estimativa de distância de B até D).
    - Para **C**: \( h(C) = 2 \) (estimativa de distância de C até D).

    3. Escolhemos a cidade **C** (menor heurística).

    4. Da cidade **C**, vamos para **D**:
    - De **C** para **D**: \( h(D) = 0 \), chegamos ao destino.

    5. O caminho encontrado pela busca gulosa é **A → C → D**, com base unicamente na estimativa de distância.
    """)

    # Conclusão
    st.subheader("Conclusão")
    st.write("""
    O algoritmo de busca gulosa encontra caminhos rápidos e promissores, mas não necessariamente os mais curtos. No exemplo das cidades, o caminho encontrado foi **A → C → D**, pois a cidade **C** parecia a mais próxima do objetivo com base na heurística, mesmo que o custo real entre as cidades não tenha sido levado em consideração.
    """)


if __name__ == "__main__":
    show_greedy_search()
