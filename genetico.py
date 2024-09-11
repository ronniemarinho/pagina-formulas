import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


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


# Função para criar uma população inicial
def create_population(size, cities):
    return [np.random.permutation(cities) for _ in range(size)]


# Função para calcular o custo de um caminho
def calculate_cost(path, distances):
    cost = 0
    for i in range(len(path) - 1):
        cost += distances[path[i], path[i + 1]]
    return cost


# Função para criar a matriz de distâncias
def create_distance_matrix(edges, cities):
    dist_matrix = np.zeros((len(cities), len(cities)))
    for u, v, d in edges:
        dist_matrix[cities.index(u), cities.index(v)] = d
        dist_matrix[cities.index(v), cities.index(u)] = d
    return dist_matrix


# Função para executar o Algoritmo Genético
def genetic_algorithm(cities, edges, population_size=10, generations=10):
    distance_matrix = create_distance_matrix(edges, cities)
    population = create_population(population_size, cities)

    for generation in range(generations):
        population.sort(key=lambda x: calculate_cost(x, distance_matrix))
        new_population = population[:2]  # Seleção dos melhores

        # Cruzamento
        for _ in range(population_size - 2):
            parent1, parent2 = np.random.choice(population[:5], 2, replace=False)
            crossover_point = np.random.randint(len(cities))
            child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            new_population.append(child)

        population = new_population

    best_path = min(population, key=lambda x: calculate_cost(x, distance_matrix))
    best_cost = calculate_cost(best_path, distance_matrix)

    return best_path, best_cost


# Função para exibir os resultados no Streamlit
def show_genetic_algorithm():
    st.title("Algoritmo Genético")

    # Introdução ao Algoritmo Genético
    st.header("Introdução ao Algoritmo Genético")
    st.write("""
    O **Algoritmo Genético** é uma técnica de otimização inspirada na seleção natural e nos processos de evolução biológica. Ele é utilizado para encontrar soluções aproximadas para problemas complexos, combinando mecanismos de seleção, cruzamento e mutação.

    No exemplo abaixo, utilizamos cidades conectadas por estradas para demonstrar como o algoritmo pode encontrar a rota mais curta entre todas as cidades.
    """)

    # Desenho do grafo das cidades
    st.header("Grafo de Cidades")
    draw_graph()

    # Características do Algoritmo Genético
    st.header("Características do Algoritmo Genético")
    st.write("""
    O algoritmo genético possui as seguintes características principais:

    - **Seleção**: Escolhe os melhores indivíduos da população para a próxima geração.
    - **Cruzamento**: Combina partes dos pais para criar novos indivíduos (filhos).
    - **Mutação**: Introduz aleatoriedade nos indivíduos para manter a diversidade genética.
    - **Iteração**: Executa por várias gerações para convergir para uma solução ótima ou aproximada.
    """)

    # Vantagens do Algoritmo Genético
    st.header("Vantagens do Algoritmo Genético")
    st.write("""
    As principais vantagens do algoritmo genético são:

    - **Flexível**: Pode ser aplicado a uma ampla gama de problemas de otimização.
    - **Robustez**: Capaz de encontrar boas soluções em problemas complexos.
    - **Exploração Global**: Mantém a diversidade da população, evitando a convergência prematura para ótimos locais.
    """)

    # Desvantagens do Algoritmo Genético
    st.header("Desvantagens do Algoritmo Genético")
    st.write("""
    O algoritmo genético também apresenta algumas desvantagens:

    - **Custo Computacional**: Pode exigir muitos recursos computacionais, especialmente em problemas grandes.
    - **Parâmetros**: A eficácia depende da escolha de parâmetros como taxa de cruzamento e mutação.
    - **Convergência**: Pode convergir para soluções subótimas se não for bem configurado.
    """)

    # Exemplo com cidades
    st.subheader("Exemplo: Encontrando o Caminho Mais Curto entre Cidades")
    st.write("""
    Vamos usar um exemplo com quatro cidades: **A**, **B**, **C** e **D**. O objetivo é encontrar o caminho mais curto que passa por todas as cidades.

    As distâncias reais entre as cidades são representadas da seguinte forma:
    - A para B: 1 km
    - A para C: 4 km
    - B para C: 2 km
    - B para D: 5 km
    - C para D: 1 km
    """)

    # Executando o algoritmo genético
    cities = ['A', 'B', 'C', 'D']
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1)
    ]

    best_path, best_cost = genetic_algorithm(cities, edges)

    st.subheader("Resultado do Algoritmo Genético")
    st.write(f"O melhor caminho encontrado é: {' → '.join(best_path)}")
    st.write(f"O custo total do caminho é: {best_cost} km")

    # Conclusão
    st.subheader("Conclusão")
    st.write("""
    O algoritmo genético demonstrado aqui encontrou o caminho mais curto para visitar todas as cidades. Essa abordagem é eficaz para problemas de otimização complexos e pode ser adaptada para diferentes contextos e tamanhos de problema.
    """)


if __name__ == "__main__":
    show_genetic_algorithm()
