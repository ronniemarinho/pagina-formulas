import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import TomekLinks
import seaborn as sns

# Função para gerar dados de exemplo
def generate_data(n_samples=1000, n_features=20, n_classes=2, weights=[0.1, 0.9]):
    X, y = make_classification(n_samples=n_samples, n_features=n_features, n_classes=n_classes,
                               weights=weights, flip_y=0.1, random_state=0)
    return X, y

# Função para aplicar SMOTE
def apply_smote(X, y):
    smote = SMOTE(random_state=0)
    X_res, y_res = smote.fit_resample(X, y)
    return X_res, y_res

# Função para aplicar Tomek Links
def apply_tomek_links(X, y):
    tomek = TomekLinks()
    X_res, y_res = tomek.fit_resample(X, y)
    return X_res, y_res

# Função para exibir os resultados no Streamlit
def show_data_processing():
    st.title("Tratamento de Dados: SMOTE e Tomek Links")

    # Introdução aos Métodos de Tratamento de Dados
    st.header("Introdução aos Métodos de Tratamento de Dados")
    st.write("""
    Neste tutorial, exploraremos duas técnicas de tratamento de dados para melhorar a qualidade dos dados e o desempenho dos modelos de aprendizado de máquina:

    - **SMOTE (Synthetic Minority Over-sampling Technique)**: Gera amostras sintéticas de minorias para balancear a distribuição das classes em um conjunto de dados desbalanceado.
    - **Tomek Links**: Remove amostras de sobreposição entre classes para limpar dados e melhorar a qualidade do conjunto de dados.
    """)

    # Seção de SMOTE
    st.header("SMOTE (Synthetic Minority Over-sampling Technique)")
    st.write("""
    O SMOTE é uma técnica de sobremuestreamento que cria novas instâncias da classe minoritária ao interpolar entre pontos existentes. Isso ajuda a balancear a distribuição das classes e melhora o desempenho do modelo.

    **Fórmula Utilizada**:
    Para gerar uma amostra sintética, o SMOTE utiliza a seguinte fórmula:
    \[
    x_{new} = x_{i} + \lambda \cdot (x_{i} - x_{nn})
    \]
    Onde:
    - \( x_{new} \) é a nova amostra sintética.
    - \( x_{i} \) é uma amostra existente.
    - \( x_{nn} \) é o vizinho mais próximo da amostra.
    - \( \lambda \) é um valor aleatório entre 0 e 1.
    """)

    # Seção de Tomek Links
    st.header("Tomek Links")
    st.write("""
    Tomek Links é uma técnica de subamostragem que identifica e remove pares de amostras em que uma amostra de uma classe é mais próxima de uma amostra de outra classe do que de qualquer outra amostra da mesma classe. Isso ajuda a limpar a sobreposição entre classes.

    **Fórmula Utilizada**:
    Tomek Links identifica pares de amostras \( (x_i, x_j) \) tais que:
    \[
    \text{dist}(x_i, x_j) < \text{dist}(x_i, x_k) \text{ e } \text{dist}(x_j, x_k)
    \]
    Onde:
    - \(x_i\) e \(x_j\) são amostras de classes diferentes.
    - \(x_k\) é uma amostra de mesma classe de \(x_i\) ou \(x_j\).
    - \(\text{dist}(x_i, x_j)\) é a distância entre \(x_i\) e \(x_j\).
    """)

    # Gerar dados de exemplo
    X, y = generate_data()

    # Normalizar dados
    X_scaled = StandardScaler().fit_transform(X)

    # Aplicar SMOTE
    st.subheader("Aplicar SMOTE")
    X_smote, y_smote = apply_smote(X_scaled, y)

    # Visualizar dados antes e depois do SMOTE
    st.write("Dados antes e depois do SMOTE")
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Visualização antes do SMOTE
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, ax=axs[0], palette="Set2")
    axs[0].set_title("Dados Originais")

    # Visualização depois do SMOTE
    sns.scatterplot(x=X_smote[:, 0], y=X_smote[:, 1], hue=y_smote, ax=axs[1], palette="Set2")
    axs[1].set_title("Dados Após SMOTE")

    st.pyplot(fig)

    # Aplicar Tomek Links
    st.subheader("Aplicar Tomek Links")
    X_tomek, y_tomek = apply_tomek_links(X_scaled, y)

    # Visualizar dados antes e depois do Tomek Links
    st.write("Dados antes e depois do Tomek Links")
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Visualização antes do Tomek Links
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, ax=axs[0], palette="Set2")
    axs[0].set_title("Dados Originais")

    # Visualização depois do Tomek Links
    sns.scatterplot(x=X_tomek[:, 0], y=X_tomek[:, 1], hue=y_tomek, ax=axs[1], palette="Set2")
    axs[1].set_title("Dados Após Tomek Links")

    st.pyplot(fig)

# Execução do código no Streamlit
if __name__ == "__main__":
    show_data_processing()
