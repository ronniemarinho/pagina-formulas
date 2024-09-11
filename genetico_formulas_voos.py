import streamlit as st
import random_forest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Título e Introdução
st.title("Teoria e Aplicação do Algoritmo Genético no Problema de Horários de Voos")

# Seções Teóricas
st.header("O que é um Algoritmo Genético?")
st.write("""
Um **Algoritmo Genético** (AG) é uma técnica de busca e otimização inspirada no processo da evolução natural. 
Ele é amplamente utilizado para resolver problemas complexos de otimização, como o problema de horários de voos.

### Etapas de um Algoritmo Genético:
1. **Inicialização**: Uma população inicial de possíveis soluções é gerada.
2. **Avaliação**: Cada solução é avaliada usando uma função de fitness.
3. **Seleção**: Soluções são selecionadas para gerar uma nova geração.
4. **Crossover**: Duas soluções são combinadas para criar novos indivíduos (filhos).
5. **Mutação**: Pequenas modificações aleatórias são aplicadas às soluções.
6. **Elitismo**: A melhor solução da geração anterior é preservada.
7. **Repetição**: O processo se repete até que uma condição de parada seja atingida.
""")

st.header("Problema de Horários de Voos")
st.write("""
O problema de horários de voos envolve a alocação de voos em janelas de horário específicas, minimizando conflitos e maximizando a satisfação dos passageiros. 
A função de avaliação penaliza sobreposições de horários e recompensa a diversidade nas janelas de tempo alocadas.
Neste exemplo, vamos considerar:
- **4 voos**
- **3 horários disponíveis** (janelas de tempo)
- **6 soluções (população inicial)** e vamos evoluir por **5 gerações**.
""")

# Exemplo numérico e simulação
st.header("Simulação do Problema com Algoritmo Genético")

voos = 4
horarios = 3
populacao_size = 6
geracoes = 5

# Simulando uma população inicial aleatória (cada solução é uma lista de horários)
populacao_inicial = [random.choices(range(1, horarios + 1), k=voos) for _ in range(populacao_size)]
st.subheader("População Inicial")
st.write(pd.DataFrame(populacao_inicial, columns=[f'Voo {i + 1}' for i in range(voos)]))


# Função de avaliação (satisfação - conflitos)
def avaliacao(solucao):
    return len(set(solucao)) - len([sol for sol in solucao if sol != 0]) * 0.5


# Avaliando a população inicial
fitness = [avaliacao(sol) for sol in populacao_inicial]
tabela_fitness = pd.DataFrame({'Solução': populacao_inicial, 'Fitness': fitness})
st.subheader("Tabela de Avaliação (Fitness) - População Inicial")
st.write(tabela_fitness)


# Função de crossover
def crossover(pai1, pai2):
    ponto_corte = random.randint(1, voos - 1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2


# Seleção dos pais por torneio
def selecao_torneio(populacao, fitness):
    indices = random.sample(range(len(populacao)), 2)
    if fitness[indices[0]] > fitness[indices[1]]:
        return populacao[indices[0]]
    else:
        return populacao[indices[1]]


# Mutação (alterando um horário aleatoriamente)
def mutacao(solucao, taxa_mutacao=0.1):
    if random.random() < taxa_mutacao:
        idx = random.randint(0, voos - 1)
        solucao[idx] = random.randint(1, horarios)
    return solucao


# Elitismo (preserva a melhor solução)
def elitismo(populacao, fitness):
    melhor_idx = np.argmax(fitness)
    return populacao[melhor_idx]


# Simulação de 5 gerações
nova_populacao = populacao_inicial[:]
for geracao in range(geracoes):
    nova_populacao_avaliada = [avaliacao(sol) for sol in nova_populacao]

    nova_geracao = []
    while len(nova_geracao) < populacao_size:
        pai1 = selecao_torneio(nova_populacao, nova_populacao_avaliada)
        pai2 = selecao_torneio(nova_populacao, nova_populacao_avaliada)

        filho1, filho2 = crossover(pai1, pai2)
        filho1 = mutacao(filho1)
        filho2 = mutacao(filho2)

        nova_geracao.extend([filho1, filho2])

    # Elitismo: preserva o melhor da geração anterior
    melhor_solucao = elitismo(nova_populacao, nova_populacao_avaliada)
    nova_geracao[0] = melhor_solucao  # Substitui um dos filhos pela melhor solução

    # Atualiza a população
    nova_populacao = nova_geracao[:populacao_size]
    st.write(f"Geração {geracao + 1}:")
    st.write(pd.DataFrame(nova_populacao, columns=[f'Voo {i + 1}' for i in range(voos)]))

# Tabela final de fitness
fitness_final = [avaliacao(sol) for sol in nova_populacao]
tabela_fitness_final = pd.DataFrame({'Solução': nova_populacao, 'Fitness': fitness_final})
st.subheader("Tabela Final de Avaliação (Fitness)")
st.write(tabela_fitness_final)

# Teoria e Simulação de Crossover, Mutação e Elitismo
st.header("Crossover, Mutação e Elitismo")

st.subheader("Crossover Simulado")
st.write("""
O **crossover** ocorre entre duas soluções (pais) e troca partes dessas soluções para gerar novos indivíduos (filhos).
No exemplo, a cada iteração do AG, dois pais são selecionados e uma nova geração é criada por crossover.
""")
st.latex(r'\text{Filho 1} = \text{Pai 1}[:ponto\_corte] + \text{Pai 2}[ponto\_corte:]')
st.latex(r'\text{Filho 2} = \text{Pai 2}[:ponto\_corte] + \text{Pai 1}[ponto\_corte:]')

st.subheader("Mutação Simulada")
st.write("""
A **mutação** altera aleatoriamente um dos horários de voo de um indivíduo, garantindo que novas soluções sejam exploradas.
No exemplo, a taxa de mutação é de 10%, ou seja, cada indivíduo tem 10% de chance de sofrer mutação.
""")

st.subheader("Elitismo Simulado")
st.write("""
O **elitismo** garante que a melhor solução de uma geração seja preservada para a próxima geração. 
No exemplo, o melhor indivíduo de cada geração é copiado diretamente para a próxima geração, evitando que a solução de maior fitness seja perdida.
""")

# Fluxograma colorido do Algoritmo Genético
st.header("Fluxograma do Algoritmo Genético")

# Criar o fluxograma usando NetworkX
G = nx.DiGraph()

# Adicionar nós (passos do algoritmo)
G.add_node("Inicialização")
G.add_node("Avaliação")
G.add_node("Seleção")
G.add_node("Crossover")
G.add_node("Mutação")
G.add_node("Nova População")
G.add_node("Condição de Parada")

# Adicionar arestas (fluxo entre os passos)
G.add_edges_from([
    ("Inicialização", "Avaliação"),
    ("Avaliação", "Seleção"),
    ("Seleção", "Crossover"),
    ("Crossover", "Mutação"),
    ("Mutação", "Nova População"),
    ("Nova População", "Avaliação"),
    ("Avaliação", "Condição de Parada")
])

# Definir a posição dos nós para um layout circular
pos = nx.spring_layout(G)

# Definir as cores para os nós e arestas
node_colors = ['#ff6666', '#ffcc66', '#66ff66', '#66ccff', '#ff99cc', '#ccccff', '#ffcc99']
edge_colors = ['#999999'] * len(G.edges)

# Desenhar o grafo
fig, ax = plt.subplots(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=3000, font_size=10,
        font_color='black', font_weight='bold', ax=ax)

# Exibir o fluxograma
st.pyplot(fig)
