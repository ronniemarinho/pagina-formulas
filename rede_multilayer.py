import streamlit as st
import numpy as np


# Funções de ativação e suas derivadas
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


# Função para calcular o erro quadrático médio (MSE)
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


# Implementação do algoritmo Backpropagation
def backpropagation(X, y, learning_rate, epochs, hidden_neurons):
    input_neurons = X.shape[1]  # Número de neurônios de entrada
    output_neurons = y.shape[1]  # Número de neurônios de saída

    # Inicialização aleatória dos pesos e vieses
    weights_input_hidden = np.random.rand(input_neurons, hidden_neurons)
    weights_hidden_output = np.random.rand(hidden_neurons, output_neurons)
    bias_hidden = np.random.rand(1, hidden_neurons)
    bias_output = np.random.rand(1, output_neurons)

    # Armazenar os erros ao longo do tempo
    mse_history = []

    for epoch in range(epochs):
        # Forward Pass
        hidden_input = np.dot(X, weights_input_hidden) + bias_hidden
        hidden_output = sigmoid(hidden_input)

        final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
        final_output = sigmoid(final_input)

        # Cálculo do erro
        error = y - final_output
        mse_history.append(mse(y, final_output))

        # Backward Pass (Backpropagation)
        d_output = error * sigmoid_derivative(final_output)
        d_hidden = d_output.dot(weights_hidden_output.T) * sigmoid_derivative(hidden_output)

        # Atualização dos pesos e vieses
        weights_hidden_output += hidden_output.T.dot(d_output) * learning_rate
        weights_input_hidden += X.T.dot(d_hidden) * learning_rate
        bias_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate
        bias_hidden += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

    return weights_input_hidden, weights_hidden_output, bias_hidden, bias_output, mse_history


# Função principal para exibir o conteúdo no Streamlit
def show_multilayer_perceptron():
    st.title("Algoritmo Backpropagation em Redes Neurais Multicamadas")

    # Introdução ao Backpropagation
    st.header("Introdução ao Algoritmo Backpropagation")
    st.write("""
    O algoritmo de **Backpropagation** é utilizado para ajustar os pesos de uma rede neural, minimizando o erro da saída em relação ao valor esperado. Ele consiste em dois passos principais:

    1. **Forward Pass**: O cálculo da saída da rede neural.
    2. **Backward Pass**: O cálculo dos gradientes e a atualização dos pesos utilizando a regra da cadeia.
    """)

    # Fórmulas do Forward Pass e Backward Pass
    st.subheader("Fórmulas do Forward Pass")
    st.latex(r'h^{(1)} = \sigma(W^{(1)} \cdot x + b^{(1)})')
    st.latex(r'h^{(2)} = \sigma(W^{(2)} \cdot h^{(1)} + b^{(2)})')
    st.write("""
    Onde:
    - \( x \) é a entrada da rede.
    - \( h^{(1)} \) é a saída da primeira camada oculta.
    - \( h^{(2)} \) é a saída final da rede.
    - \( W^{(1)} \) e \( W^{(2)} \) são os pesos da camada oculta e da camada de saída, respectivamente.
    - \( b^{(1)} \) e \( b^{(2)} \) são os vieses das camadas.
    - \( \sigma \) é a função de ativação (neste caso, Sigmoid).
    """)

    st.subheader("Fórmulas do Backward Pass (Cálculo dos Gradientes)")
    st.latex(r'\delta^{(2)} = (h^{(2)} - y) \cdot \sigma^{\prime}(z^{(2)})')
    st.latex(r'\delta^{(1)} = \delta^{(2)} \cdot W^{(2)} \cdot \sigma^{\prime}(z^{(1)})')
    st.write("""
    Onde:
    - \( \delta^{(2)} \) é o erro da camada de saída.
    - \( \delta^{(1)} \) é o erro da camada oculta.
    - \( \sigma^{\prime}(z) \) é a derivada da função de ativação Sigmoid.
    """)

    st.subheader("Atualização dos Pesos")
    st.latex(r'W^{(2)} = W^{(2)} - \eta \cdot \delta^{(2)} \cdot h^{(1)T}')
    st.latex(r'W^{(1)} = W^{(1)} - \eta \cdot \delta^{(1)} \cdot x^{T}')
    st.write("""
    Onde:
    - \( \eta \) é a taxa de aprendizado.
    - \( W^{(2)} \) e \( W^{(1)} \) são os pesos a serem atualizados.
    """)

    # Exemplo prático
    st.header("Exemplo Prático: Treinamento com Backpropagation")

    # Entradas do exemplo (XOR)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Parâmetros do treinamento
    learning_rate = st.slider("Taxa de Aprendizado", 0.01, 1.0, 0.1)
    hidden_neurons = st.slider("Número de Neurônios na Camada Oculta", 1, 10, 2)
    epochs = st.slider("Número de Épocas", 100, 10000, 1000)

    # Treinar a rede neural com Backpropagation
    weights_input_hidden, weights_hidden_output, bias_hidden, bias_output, mse_history = backpropagation(X, y,
                                                                                                         learning_rate,
                                                                                                         epochs,
                                                                                                         hidden_neurons)

    # Exibir os pesos finais
    st.subheader("Pesos Finais Após o Treinamento")
    st.write("Pesos da Camada de Entrada para Camada Oculta:")
    st.write(weights_input_hidden)
    st.write("Pesos da Camada Oculta para a Camada de Saída:")
    st.write(weights_hidden_output)

    # Exibir o gráfico do erro ao longo das épocas
    st.subheader("Erro (MSE) ao Longo das Épocas")
    st.line_chart(mse_history)


# Execução do código no Streamlit
if __name__ == "__main__":
    show_backpropagation()
