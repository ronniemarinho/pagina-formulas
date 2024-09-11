import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_circles, make_moons
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# Função para gerar dados de exemplo
def generate_data(n_samples=300, noise=0.1):
    # Gera dados com duas formas complexas: círculos e luas
    X1, _ = make_circles(n_samples=n_samples//2, factor=0.5, noise=noise)
    X2, _ = make_moons(n_samples=n_samples//2, noise=noise)
    X = np.vstack((X1, X2))
    return X

# Função para aplicar o algoritmo DBSCAN
def apply_dbscan(X, eps, min_samples):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(X)
    return labels, dbscan

# Função para exibir os resultados no Streamlit
def show_dbscan():
    st.title("Algoritmo DBSCAN de Agrupamento de Dados")

    # Introdução ao Algoritmo DBSCAN
    st.header("Introdução ao Algoritmo DBSCAN")
    st.write("""
    O **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** é um algoritmo de **agrupamento baseado em densidade** que identifica clusters de alta densidade e rotula pontos em áreas de baixa densidade como ruído. O DBSCAN é útil para detectar clusters de forma arbitrária e é robusto a ruídos e outliers.

    Os principais parâmetros do DBSCAN são:

    - **Eps**: Distância máxima entre dois pontos para que um ponto seja considerado como vizinho.
    - **Min_samples**: Número mínimo de pontos em uma vizinhança para que um ponto seja considerado como núcleo de um cluster.
    """)

    # Fórmulas Utilizadas
    st.subheader("Fórmulas Utilizadas")
    st.latex(r'\text{Eps}: \text{Distância máxima para que dois pontos sejam considerados vizinhos}')
    st.latex(r'\text{Min\_samples}: \text{Número mínimo de pontos necessários em uma vizinhança para formar um cluster}')

    st.write("""
    O DBSCAN utiliza os parâmetros Eps e Min_samples para determinar a densidade dos pontos e identificar clusters:

    - **Eps**: Define a distância máxima para considerar dois pontos como vizinhos.
    - **Min_samples**: Define o número mínimo de pontos necessários para formar um cluster.
    """)

    # Seção de características do algoritmo DBSCAN
    st.header("Características do Algoritmo DBSCAN")
    st.write("""
    O DBSCAN possui as seguintes características:

    - **Baseado em Densidade**: Identifica clusters de alta densidade e rotula pontos de baixa densidade como ruído.
    - **Sem Necessidade de Número de Clusters**: Não requer a especificação do número de clusters a priori.
    - **Robusto a Outliers**: Capaz de lidar com ruído e outliers.
    - **Clusters de Forma Arbitrária**: Pode identificar clusters de formas e tamanhos variados.
    """)

    # Seção de vantagens
    st.header("Vantagens do Algoritmo DBSCAN")
    st.write("""
    O algoritmo DBSCAN oferece várias vantagens:

    - **Robustez a Ruído**: Eficaz para identificar clusters em dados com ruído e outliers.
    - **Não Necessita de Número de Clusters**: Não requer a definição do número de clusters a priori.
    - **Clusters Arbitrários**: Capaz de encontrar clusters de formas e tamanhos variados.
    """)

    # Seção de desvantagens
    st.header("Desvantagens do Algoritmo DBSCAN")
    st.write("""
    No entanto, o DBSCAN apresenta algumas desvantagens:

    - **Escolha de Parâmetros**: A escolha dos parâmetros Eps e Min_samples pode ser difícil e sensível aos dados.
    - **Escalabilidade**: Pode ser menos eficiente em conjuntos de dados muito grandes.
    - **Desempenho em Dados de Alta Dimensionalidade**: Pode enfrentar dificuldades com dados de alta dimensionalidade.
    """)

    # Conclusão
    st.header("Conclusão")
    st.write("""
    O **algoritmo DBSCAN** é uma poderosa técnica de agrupamento baseada em densidade, ideal para detectar clusters em dados com forma arbitrária e robusto a ruído. Embora apresente desafios na escolha de parâmetros e em dados de alta dimensionalidade, suas vantagens o tornam uma escolha popular para muitos problemas de agrupamento.
    """)

    # Exemplo prático com dados gerados
    st.header("Exemplo Prático: Agrupamento de Dados com DBSCAN")

    # Gerar dados de exemplo
    X = generate_data()

    # Normalizar dados
    X_scaled = StandardScaler().fit_transform(X)

    # Parâmetros do DBSCAN
    eps = st.slider("Distância Máxima (Eps)", 0.1, 1.5, 0.3)
    min_samples = st.slider("Número Mínimo de Pontos (Min_samples)", 1, 20, 5)

    # Aplicar DBSCAN
    labels, dbscan = apply_dbscan(X_scaled, eps, min_samples)

    # Adicionar rótulos aos dados
    data = pd.DataFrame(X, columns=["Feature 1", "Feature 2"])
    data['Cluster'] = labels

    # Visualizar clusters
    st.subheader("Visualização dos Clusters")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data["Feature 1"], y=data["Feature 2"], hue=labels, palette="Set2", s=50, alpha=0.7, edgecolor='w')
    plt.title("Visualização dos Clusters com DBSCAN")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    st.pyplot(plt)

    # Exibir número de clusters encontrados
    st.subheader("Número de Clusters Encontrados")
    num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    st.write(f"Total de clusters encontrados: {num_clusters+1}")

    # Exibir dados agrupados
    st.subheader("Dados Agrupados")
    st.write(data)

# Execução do código no Streamlit
if __name__ == "__main__":
    show_dbscan()
