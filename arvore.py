import streamlit as st
import numpy as np


def show_decision_tree():
    st.title("Algoritmo de Árvore de Decisão")

    # Introdução à Árvore de Decisão
    st.header("Introdução à Árvore de Decisão")
    st.write("""
    O algoritmo de árvore de decisão é um dos mais populares para classificação e regressão. 
    Ele constrói um modelo em forma de árvore que divide repetidamente os dados em subconjuntos baseados em atributos.
    Cada nó da árvore representa uma decisão ou teste, e cada ramo representa o resultado desse teste, até que uma folha seja atingida, indicando a previsão final.
    """)

    # Explicação do Processo de Divisão
    st.header("Processo de Divisão")
    st.write("""
    A árvore de decisão usa métricas como a **Entropia** e o **Ganho de Informação** (ou **Índice de Gini**) para decidir como dividir os dados. 
    O objetivo é maximizar a "pureza" de cada divisão, de forma que os dados em cada subconjunto resultante sejam o mais homogêneos possível.
    """)

    st.subheader("Entropia")
    st.latex(r'H(S) = -\sum_{i=1}^{c} p_i \log_2(p_i)')
    st.write("""
    A entropia é uma medida de incerteza. Para um conjunto \( S \), com \( c \) classes, \( p_i \) é a proporção de exemplos da classe \( i \) no conjunto \( S \).
    O objetivo é reduzir a entropia em cada divisão, criando subconjuntos que sejam mais homogêneos.
    """)

    st.subheader("Ganho de Informação")
    st.latex(r'IG(S, A) = H(S) - \sum_{v \in \text{Valores}(A)} \frac{|S_v|}{|S|} H(S_v)')
    st.write("""
    O ganho de informação mede a redução da entropia após dividir o conjunto de dados \( S \) com base em um atributo \( A \). 
    Quanto maior o ganho de informação, melhor o atributo para fazer a divisão.
    """)

    st.subheader("Índice de Gini")
    st.latex(r'Gini(S) = 1 - \sum_{i=1}^{c} p_i^2')
    st.write("""
    O índice de Gini mede a impureza de um conjunto. Ele é utilizado para avaliar a qualidade das divisões. 
    Quanto menor o índice de Gini, mais puro é o conjunto resultante.
    """)

    # Tipos de Árvore de Decisão
    st.header("Tipos de Árvores de Decisão")

    st.subheader("Árvore de Classificação")
    st.write("""
    Usada quando o objetivo é prever uma classe (valor discreto). Cada folha da árvore representa uma classe e cada divisão maximiza a homogeneidade das classes resultantes.
    """)

    st.subheader("Árvore de Regressão")
    st.write("""
    Usada quando o objetivo é prever um valor contínuo. As divisões são feitas para minimizar o erro de previsão, como o erro quadrático médio (MSE).
    """)

    # Vantagens e Desvantagens
    st.header("Vantagens e Desvantagens")

    st.subheader("Vantagens")
    st.write("""
    1. **Fácil de Interpretar**: Representa o processo de decisão de forma visual e compreensível.
    2. **Versátil**: Pode ser usada tanto para problemas de classificação quanto de regressão.
    3. **Sem Necessidade de Normalização**: As árvores de decisão não são afetadas por diferentes escalas dos dados.
    4. **Lida Bem com Dados Categóricos e Numéricos**: Pode lidar com ambos os tipos de dados sem precisar de pré-processamento especial.
    """)

    st.subheader("Desvantagens")
    st.write("""
    1. **Propenso a Overfitting**: Árvores profundas podem se ajustar demais ao conjunto de treinamento, perdendo a capacidade de generalizar.
    2. **Instabilidade**: Pequenas alterações nos dados podem resultar em uma estrutura de árvore completamente diferente.
    3. **Maior Complexidade em Dados Grandes**: Árvores complexas podem ser difíceis de interpretar quando aplicadas a conjuntos de dados grandes.
    """)

    # Aplicações de Árvores de Decisão
    st.header("Aplicações de Árvores de Decisão")
    st.write("""
    Árvores de decisão são amplamente usadas em:

    - **Diagnósticos Médicos**: Para auxiliar na tomada de decisões de diagnóstico e prognóstico.
    - **Classificação de Crédito**: Para determinar se um solicitante de empréstimo é de baixo ou alto risco.
    - **Marketing**: Para segmentar clientes com base em características demográficas e comportamentais.
    """)

    # Principais Características das Árvores de Decisão
    st.header("Principais Características das Árvores de Decisão")
    st.write("""
    - **Baseadas em Regras**: As decisões são tomadas em cada nó da árvore com base em uma condição.
    - **Estrutura Hierárquica**: O processo de decisão segue uma hierarquia de testes.
    - **Não Paramétrico**: Não faz suposições sobre a distribuição dos dados.
    """)

    # Conclusão
    st.header("Conclusão")
    st.write("""
    Árvores de decisão são ferramentas poderosas para classificação e regressão. 
    Sua simplicidade e capacidade de interpretação fazem delas uma escolha popular, embora possam ser sensíveis ao overfitting. 
    Técnicas como poda e o uso de florestas aleatórias podem ajudar a mitigar esses problemas.
    """)


# Exibir no Streamlit
if __name__ == '__main__':
    show_decision_tree()
