import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Função para gerar dados fuzzy de exemplo
def generate_fuzzy_data():
    x = np.linspace(0, 10, 100)
    return x

# Função para calcular a função de pertinência
def membership_function(x, a, b, c):
    # Evitar divisão por zero
    if a == b or b == c:
        return np.zeros_like(x)
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)

# Função para calcular o centroide da função fuzzy
def calculate_centroid(x, mu):
    numerator = np.sum(x * mu)
    denominator = np.sum(mu)
    return numerator / denominator if denominator != 0 else 0

# Função para exibir os resultados no Streamlit
def show_fuzzy_logic():
    st.title("Introdução à Lógica Fuzzy")

    # Introdução ao conceito de lógica fuzzy
    st.header("O que é Lógica Fuzzy?")
    st.write("""
    A **lógica fuzzy** é uma forma de lógica multivalorada que lida com conceitos vagos e imprecisos, permitindo que os valores de verdade não sejam simplesmente verdadeiros ou falsos, mas sim em algum grau entre 0 e 1. 
    Ao contrário da lógica booleana tradicional, que utiliza apenas dois valores (0 e 1), a lógica fuzzy permite valores intermediários, o que é mais próximo da forma como os humanos percebem e interpretam informações.
    """)

    # Fórmulas Utilizadas
    st.subheader("Fórmulas Utilizadas")
    st.latex(r'\text{Função de Pertinência} \, \mu(x) = \max \left( \min \left( \frac{x - a}{b - a}, \frac{c - x}{c - b} \right), 0 \right)')
    st.latex(r'\text{Centroide\_calc} = \frac{\sum_{i} x_i \cdot \mu(x_i)}{\sum_{i} \mu(x_i)}')
    st.write("""
    Onde:
    - \( a \) e \( c \) são os pontos que definem o intervalo da função de pertinência.
    - \( b \) é o ponto onde a função de pertinência atinge o seu valor máximo.
    - \( x_i \) representa os valores da variável de entrada.
    - \( \mu(x_i) \) é o grau de pertinência correspondente ao valor \( x_i \).
    """)

    # Seção de características da lógica fuzzy
    st.header("Características da Lógica Fuzzy")
    st.write("""
    A lógica fuzzy tem as seguintes características:
    - **Valores Intermediários**: Permite valores de verdade intermediários entre 0 e 1.
    - **Funções de Pertinência**: Utiliza funções para definir o grau de pertença de um elemento a um conjunto fuzzy.
    - **Regras Fuzzy**: Permite a criação de regras que lidam com a imprecisão e a incerteza dos dados.
    - **Modelagem de Incerteza**: Adequada para sistemas onde a informação é imprecisa ou incerta.
    """)

    # Seção de vantagens
    st.header("Vantagens da Lógica Fuzzy")
    st.write("""
    A lógica fuzzy oferece várias vantagens:
    - **Flexibilidade**: Capacidade de lidar com incertezas e imprecisões.
    - **Interpretação Natural**: Mais próxima da forma como os humanos interpretam informações.
    - **Desempenho**: Pode ser usada em sistemas de controle e tomada de decisão complexos.
    - **Simples de Implementar**: Conceitos e regras podem ser facilmente definidos e ajustados.
    """)

    # Seção de desvantagens
    st.header("Desvantagens da Lógica Fuzzy")
    st.write("""
    No entanto, a lógica fuzzy também apresenta algumas desvantagens:
    - **Complexidade na Definição de Regras**: Definir um grande número de regras pode ser complexo e trabalhoso.
    - **Dificuldade de Ajuste**: Pode ser difícil ajustar e validar funções de pertinência para sistemas complexos.
    - **Desempenho Computacional**: Sistemas fuzzy complexos podem exigir mais recursos computacionais.
    """)

    # Cálculo e visualização do centroide
    st.header("Cálculo Dinâmico do Centroide\_calc da Função de Pertinência")

    # Gerar dados fuzzy
    x = generate_fuzzy_data()

    # Parâmetros das funções de pertinência
    a = st.slider("Parâmetro a", 0.0, 5.0, 2.0)
    b = st.slider("Parâmetro b", 0.0, 5.0, 5.0)
    c = st.slider("Parâmetro c", 5.0, 10.0, 8.0)

    # Calcular a função de pertinência
    mu = membership_function(x, a, b, c)

    # Calcular o centroide
    centroid_calc = calculate_centroid(x, mu)

    # Mostrar cálculo do centroide
    st.subheader("Cálculo do Centroide\_calc")
    st.write(f"""
    A fórmula para calcular o centroide da função de pertinência é:
    $$ \\text{{Centroide\_calc}} = \\frac{{\\sum_i x_i \\cdot \\mu(x_i)}}{{\\sum_i \\mu(x_i)}} $$

    Onde:
    - \( x_i \) são os valores da variável de entrada.
    - \( \\mu(x_i) \) é o grau de pertinência correspondente ao valor \( x_i \).

    Para os valores atuais dos parâmetros:
    - \( a = {a} \)
    - \( b = {b} \)
    - \( c = {c} \)

    A função de pertinência é calculada como:
    $$ \\mu(x) = \\max \\left( \\min \\left( \\frac{{x - {a}}}{{{b} - {a}}}, \\frac{{{c} - x}}{{{c} - {b}}} \\right), 0 \\right) $$

    O centroide calculado é: {centroid_calc:.2f}
    """)

    # Visualizar função de pertinência
    st.subheader("Visualização da Função de Pertinência")
    plt.figure(figsize=(10, 6))
    plt.plot(x, mu, label=f'a={a}, b={b}, c={c}', color='blue')
    plt.axvline(centroid_calc, color='red', linestyle='--', label=f'Centroide\_calc = {centroid_calc:.2f}')
    plt.title("Função de Pertinência Fuzzy")
    plt.xlabel("x")
    plt.ylabel("Grau de Pertinência")
    plt.legend()
    st.pyplot(plt)

    # Exibir parâmetros e centroide
    st.subheader("Parâmetros da Função de Pertinência")
    st.write(pd.DataFrame({
        'Parâmetro': ['a', 'b', 'c', 'Centroide_calc'],
        'Valor': [a, b, c, centroid_calc]
    }))

if __name__ == "__main__":
    show_fuzzy_logic()
