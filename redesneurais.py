import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def show_single_layer_perceptron():
    st.title("Rede Neural de Uma Camada (Perceptron Simples)")

    # Introdução ao Perceptron Simples
    st.header("Introdução ao Perceptron Simples")
    st.write("""
    O **Perceptron Simples** é uma rede neural básica com uma única camada de saída. Ele é usado para resolver problemas de classificação linearmente separáveis. O Perceptron pode ser visto como um classificador linear que ajusta os pesos com base nos erros cometidos durante o treinamento.
    """)

    # Fórmula da Função Linear
    st.subheader("Fórmula da Função Linear do Perceptron Simples")
    st.latex(r'y = \sigma(w \cdot x + b)')
    st.write("""
    Onde:
    - \( y \) é a saída do neurônio.
    - \( w \) é o vetor de pesos que define a importância de cada entrada.
    - \( x \) é o vetor de entradas.
    - \( b \) é o viés (bias) adicionado ao modelo para ajustar o valor da saída.
    - \( \sigma \) é a função de ativação.
    """)

    # Funções de Ativação
    st.subheader("Funções de Ativação")
    st.write("""
    Funções de ativação são usadas para introduzir não-linearidade nos modelos. As funções mais comuns são:

    - **Sigmoid**: Mapeia o valor de saída entre 0 e 1.
    - **ReLU (Rectified Linear Unit)**: Define a saída como o máximo entre 0 e o valor de entrada.
    - **Degrau**: Retorna 1 se a entrada for maior que um limiar e 0 caso contrário.
    """)

    st.subheader("Função Sigmoid")
    st.latex(r'\sigma(x) = \frac{1}{1 + e^{-x}}')
    st.write("A função sigmoid é usada frequentemente em problemas de classificação binária.")

    st.subheader("Função ReLU")
    st.latex(r'\text{ReLU}(x) = \max(0, x)')
    st.write("A função ReLU é popular em redes neurais profundas devido à sua simplicidade e eficácia.")

    st.subheader("Função Degrau")
    st.latex(r'\text{Degrau}(x) = \begin{cases} '
             '1 & \text{se } x > 0 \\ '
             '0 & \text{caso contrário} '
             '\end{cases}')
    st.write(
        "A função degrau é uma das funções de ativação mais simples e é usada em problemas onde a saída precisa ser binária.")


    # Cálculo do Erro
    st.header("Cálculo do Erro")
    st.write("""
    A função de custo para o Perceptron Simples pode ser calculada usando as seguintes fórmulas:

    - **Erro Quadrático Médio (MSE)**:
    """)
    st.latex(r'\text{MSE} = \frac{1}{m} \sum_{i=1}^{m} (h(x^{(i)}) - y^{(i)})^2')
    st.write("""
    Onde:
    - \( h(x^{(i)}) \) é a previsão do Perceptron para a amostra \( i \).
    - \( y^{(i)} \) é o valor verdadeiro da amostra \( i \).
    - \( m \) é o número total de amostras.

    - **Entropia Cruzada (Cross-Entropy)**:
    """)
    st.latex(
        r'\text{CE} = - \frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(h(x^{(i)})) + (1 - y^{(i)}) \log(1 - h(x^{(i)})) \right]')
    st.write("""
    Onde:
    - \( h(x^{(i)}) \) é a previsão do Perceptron para a amostra \( i \).
    - \( y^{(i)}) \) é o valor verdadeiro da amostra \( i \).
    - \( m \) é o número total de amostras.
    """)

    # Vantagens e Desvantagens
    st.header("Vantagens e Desvantagens do Perceptron Simples")

    st.subheader("Vantagens")
    st.write("""
    1. **Simplicidade**: O Perceptron Simples é fácil de implementar e entender.
    2. **Rápido Treinamento**: O treinamento é geralmente rápido devido à simplicidade do modelo.
    3. **Base para Redes Neurais**: Serve como uma base para entender conceitos de redes neurais mais complexas.
    """)

    st.subheader("Desvantagens")
    st.write("""
    1. **Classificação Linear**: Só é capaz de resolver problemas linearmente separáveis.
    2. **Limitação de Representação**: Não é capaz de capturar padrões complexos e não-lineares.
    3. **Problemas com Dados Não Linearmente Separáveis**: Não pode resolver problemas que não sejam linearmente separáveis, como o problema XOR.
    """)

    # Aplicações do Perceptron Simples
    st.header("Aplicações do Perceptron Simples")
    st.write("""
    O Perceptron Simples é utilizado em problemas onde os dados podem ser separados por uma linha reta. Exemplos incluem:

    - **Classificação Binária Simples**: Identificação de padrões básicos que podem ser separados linearmente.
    - **Teste de Conceitos de Redes Neurais**: Usado como um modelo inicial para entender redes neurais antes de avançar para modelos mais complexos.
    """)

    # Conclusão
    st.header("Conclusão")
    st.write("""
    O Perceptron Simples é uma rede neural básica que pode ser eficaz para problemas simples de classificação linear. No entanto, suas limitações em lidar com padrões complexos tornam necessário o uso de redes neurais multicamadas para problemas mais desafiadores.
    """)


# Exibir no Streamlit
if __name__ == '__main__':
    show_single_layer_perceptron()
