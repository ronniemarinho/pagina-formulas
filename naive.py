import streamlit as st
import numpy as np


def show_naive_bayes():
    st.title("Algoritmo Naive Bayes")

    # Introdução ao Naive Bayes
    st.header("Introdução ao Naive Bayes")
    st.write("""
    O Naive Bayes é uma família de algoritmos de classificação baseados no teorema de Bayes, com a suposição de que as características são condicionalmente independentes umas das outras. 
    Apesar dessa suposição simplificadora, o Naive Bayes pode ser muito eficaz, especialmente em problemas de texto e classificação de documentos.
    """)

    # Fórmula do Teorema de Bayes
    st.header("Teorema de Bayes")
    st.latex(r'P(A|B) = \frac{P(B|A)P(A)}{P(B)}')
    st.write("""
    O teorema de Bayes descreve a probabilidade de um evento \( A \), dado que outro evento \( B \) já ocorreu. Para o Naive Bayes:
    - \( P(A|B) \) é a probabilidade da classe \( A \) dado os dados \( B \).
    - \( P(B|A) \) é a probabilidade dos dados \( B \) dado a classe \( A \).
    - \( P(A) \) é a probabilidade da classe \( A \) sem qualquer informação adicional.
    - \( P(B) \) é a probabilidade dos dados \( B \) sem qualquer restrição.
    """)

    # Assunção de Independência Condicional
    st.header("Assunção de Independência Condicional")
    st.write("""
    O Naive Bayes assume que todas as características (atributos) são independentes umas das outras, dado a classe. Embora essa suposição raramente seja verdadeira no mundo real, 
    ela simplifica bastante os cálculos e muitas vezes ainda leva a bons resultados em diversas aplicações.
    """)

    # Tipos de Naive Bayes
    st.header("Principais Tipos de Naive Bayes")

    st.subheader("Gaussian Naive Bayes")
    st.write("""
    Usado quando os atributos seguem uma distribuição normal (gaussiana). A probabilidade condicional é calculada utilizando a função densidade de probabilidade da normal.
    """)

    st.subheader("Multinomial Naive Bayes")
    st.write("""
    Frequentemente usado para classificação de documentos, onde os atributos são contagens inteiras de eventos, como a frequência de palavras em um texto.
    """)

    st.subheader("Bernoulli Naive Bayes")
    st.write("""
    Adequado para dados binários, onde cada atributo é representado por 0 ou 1, indicando a presença ou ausência de uma característica.
    """)

    # Vantagens e Desvantagens do Naive Bayes
    st.header("Vantagens e Desvantagens do Naive Bayes")

    st.subheader("Vantagens")
    st.write("""
    1. **Simples e Rápido**: É fácil de implementar e requer pouco tempo de treinamento, mesmo em grandes conjuntos de dados.
    2. **Eficiência com Dados de Texto**: Funciona bem em problemas de classificação de texto, como análise de sentimentos e categorização de e-mails.
    3. **Baixa Complexidade Computacional**: Exige menos memória e poder de processamento, sendo adequado para grandes volumes de dados.
    """)

    st.subheader("Desvantagens")
    st.write("""
    1. **Supondo Independência entre Características**: A suposição de que todas as características são independentes é frequentemente irrealista e pode prejudicar a precisão do modelo.
    2. **Pode Ser Pobre com Dados Correlacionados**: Quando os atributos têm correlação significativa, a performance do Naive Bayes tende a diminuir.
    3. **Sensível a Dados Escassos**: Em alguns casos, se um atributo não aparecer no conjunto de treinamento para uma determinada classe, o Naive Bayes atribui uma probabilidade zero, o que pode ser problemático. Isso pode ser corrigido com suavização de Laplace.
    """)

    # Aplicações do Naive Bayes
    st.header("Aplicações do Naive Bayes")
    st.write("""
    O Naive Bayes é amplamente utilizado em várias áreas, como:

    - **Classificação de Texto**: Análise de sentimentos, categorização de documentos e filtragem de spam.
    - **Sistemas de Recomendação**: Para sugerir itens baseados nas preferências anteriores dos usuários.
    - **Diagnósticos Médicos**: Para prever a probabilidade de doenças com base em sintomas.
    """)

    # Principais Características do Naive Bayes
    st.header("Principais Características do Naive Bayes")
    st.write("""
    - **Probabilístico**: Baseado na probabilidade e nas regras do teorema de Bayes.
    - **Rápido**: Extremamente eficiente em tempo de treinamento e inferência, ideal para problemas em tempo real.
    - **Não Paramétrico**: Não faz suposições complexas sobre a distribuição dos dados.
    - **Classificação Multiclasse**: Naturalmente suporta múltiplas classes sem precisar de ajustes especiais.
    """)

    # Conclusão
    st.header("Conclusão")
    st.write("""
    O algoritmo Naive Bayes é uma ferramenta poderosa e simples para classificação, especialmente quando lidamos com dados de texto e grandes volumes de dados. 
    Apesar de suas suposições fortes, muitas vezes oferece uma precisão satisfatória, tornando-o um ponto de partida comum para problemas de aprendizado supervisionado.
    """)


# Exibir no Streamlit
if __name__ == '__main__':
    show_naive_bayes()
