import streamlit as st
import numpy as np


def show_random_forest():
    st.title("Algoritmo Random Forest")

    # Introdução ao Random Forest
    st.header("Introdução ao Random Forest")
    st.write("""
    O Random Forest é um algoritmo de aprendizado supervisionado que pode ser usado tanto para classificação quanto para regressão. 
    Ele constrói várias árvores de decisão e as combina para melhorar a precisão e evitar overfitting. A ideia principal é treinar diversas árvores em subconjuntos aleatórios dos dados e fazer a média das previsões (no caso de regressão) ou votação (no caso de classificação).
    """)

    # Processo de Criação do Random Forest
    st.header("Processo de Criação do Random Forest")
    st.write("""
    O Random Forest segue o seguinte processo:
    1. **Bootstrapping**: São gerados vários subconjuntos aleatórios de dados de treinamento, com substituição (amostragem com reposição).
    2. **Treinamento das Árvores**: Cada árvore de decisão é treinada em um desses subconjuntos.
    3. **Predição Agregada**: Para classificação, a previsão final é baseada na votação majoritária das árvores. Para regressão, é calculada a média das previsões das árvores.
    """)

    # Explicação de Bootstrapping e Randomização de Atributos
    st.header("Bootstrapping e Randomização de Atributos")
    st.write("""
    O **bootstrapping** ajuda a reduzir o overfitting ao fornecer conjuntos de dados ligeiramente diferentes para cada árvore. Além disso, em cada divisão da árvore, o Random Forest seleciona um subconjunto aleatório de características, o que reduz a correlação entre as árvores e melhora a generalização do modelo.
    """)

    # Fórmula do Ganho de Informação e do Índice de Gini
    st.subheader("Ganho de Informação e Índice de Gini")
    st.write("""
    Assim como em árvores de decisão, cada árvore no Random Forest pode usar métricas como o **Ganho de Informação** ou o **Índice de Gini** para fazer suas divisões.
    """)

    st.subheader("Índice de Gini")
    st.latex(r'Gini(S) = 1 - \sum_{i=1}^{c} p_i^2')
    st.write("""
    O índice de Gini é uma métrica utilizada para avaliar a impureza dos nós em árvores de decisão. Quanto menor o valor de Gini, mais puro é o nó resultante da divisão.
    """)

    # Vantagens e Desvantagens do Random Forest
    st.header("Vantagens e Desvantagens do Random Forest")

    st.subheader("Vantagens")
    st.write("""
    1. **Redução de Overfitting**: O uso de múltiplas árvores e a aleatorização reduzem o risco de overfitting em relação a uma única árvore de decisão.
    2. **Alta Precisão**: O Random Forest geralmente resulta em uma alta precisão, devido à agregação de previsões.
    3. **Robusto a Outliers**: Como a decisão final é baseada em um conjunto de árvores, outliers em um subconjunto de dados têm pouco impacto na decisão final.
    4. **Lida com Dados Faltantes**: Random Forest pode lidar com valores ausentes por meio da substituição das médias ou moda dos dados.
    """)

    st.subheader("Desvantagens")
    st.write("""
    1. **Maior Complexidade**: Um modelo de Random Forest pode ser difícil de interpretar, devido à combinação de várias árvores.
    2. **Custo Computacional**: Treinar múltiplas árvores pode ser computacionalmente caro, tanto em termos de tempo quanto de memória, especialmente para grandes conjuntos de dados.
    3. **Predições Lentas**: A inferência pode ser mais lenta em comparação com uma única árvore de decisão, já que envolve a consulta de múltiplas árvores.
    """)

    # Comparação entre Random Forest e Árvores de Decisão
    st.header("Comparação com Árvores de Decisão")
    st.write("""
    Enquanto uma árvore de decisão única pode ser altamente suscetível ao overfitting, o Random Forest reduz esse problema ao combinar várias árvores e realizar votações. 
    Isso resulta em um modelo mais robusto e generalizável.
    """)

    # Aplicações de Random Forest
    st.header("Aplicações do Random Forest")
    st.write("""
    O Random Forest é amplamente utilizado em diversas áreas, como:

    - **Detecção de Fraude**: Usado para identificar transações fraudulentas em sistemas financeiros.
    - **Diagnóstico Médico**: Para prever a probabilidade de doenças com base em sintomas.
    - **Sistemas de Recomendação**: Para prever as preferências dos usuários com base em seu comportamento anterior.
    - **Análise de Crédito**: Para determinar a elegibilidade de crédito de um solicitante.
    """)

    # Principais Características do Random Forest
    st.header("Principais Características do Random Forest")
    st.write("""
    - **Ensemble de Árvores**: Combina o resultado de múltiplas árvores para melhorar a precisão.
    - **Aleatorização**: Usa amostragem aleatória de dados e de características para construir cada árvore, reduzindo a correlação entre elas.
    - **Robusto a Overfitting**: Mesmo se algumas árvores overfitarem, a agregação final tende a suavizar os efeitos, resultando em um modelo mais generalizável.
    - **Escalabilidade**: Funciona bem com grandes conjuntos de dados e com um grande número de características.
    """)

    # Conclusão
    st.header("Conclusão")
    st.write("""
    O Random Forest é um algoritmo poderoso e versátil, adequado tanto para classificação quanto para regressão. 
    Sua capacidade de reduzir o overfitting e lidar com grandes volumes de dados faz dele uma escolha popular em muitas aplicações práticas.
    """)


# Exibir no Streamlit
if __name__ == '__main__':
    show_random_forest()
