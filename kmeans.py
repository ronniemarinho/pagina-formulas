import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import seaborn as sns

# Função para gerar dados de exemplo
def generate_data(n_samples=300, n_features=2, n_clusters=4):
    X, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, cluster_std=0.60, random_state=0)
    return X

# Função para aplicar o algoritmo K-means
def apply_kmeans(X, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
    return kmeans

# Função para exibir os resultados no Streamlit
def show_kmeans():
    st.title("Algoritmo K-means de Agrupamento de Dados")

    # Introdução ao Algoritmo K-means
    st.header("Introdução ao Algoritmo K-means")
    st.write("""
    O **algoritmo K-means** é uma técnica de **agrupamento de dados** usada para particionar um conjunto de dados em \(k\) clusters, onde cada ponto de dados pertence ao cluster com a média mais próxima. O objetivo é minimizar a variação dentro de cada cluster.

    A ideia principal é encontrar um conjunto de \(k\) centroids (ou centros de clusters) que minimizem a soma das distâncias quadráticas entre os pontos de dados e os seus centroids correspondentes.
    """)

    # Fórmulas Utilizadas
    st.subheader("Fórmulas Utilizadas")
    st.latex(r'\text{Custo} = \sum_{i=1}^{k} \sum_{x \in C_i} \|x - \mu_i\|^2')
    st.write("""
    Onde:
    - \( C_i \) é o i-ésimo cluster.
    - \( x \) é um ponto de dados no cluster \(C_i\).
    - \( \mu_i \) é o centro do cluster \(C_i\).
    """)

    # Seção de características do algoritmo K-means
    st.header("Características do Algoritmo K-means")
    st.write("""
    O algoritmo K-means possui as seguintes características:

    - **Partição dos Dados**: Divide os dados em \(k\) clusters.
    - **Centroides**: Cada cluster é representado por um centroide.
    - **Minimização da Variância**: Objetiva minimizar a soma das distâncias quadráticas entre os pontos e os centroides.
    - **Iterativo**: O algoritmo é iterativo e continua até que os centroides não mudem mais significativamente.
    """)

    # Seção de vantagens
    st.header("Vantagens do Algoritmo K-means")
    st.write("""
    O algoritmo K-means oferece várias vantagens:

    - **Simplicidade**: Fácil de entender e implementar.
    - **Eficiência**: Relativamente rápido e eficiente para grandes conjuntos de dados.
    - **Escalabilidade**: Pode ser aplicado a grandes conjuntos de dados.
    - **Convergência**: Converge rapidamente para uma solução.
    """)

    # Seção de desvantagens
    st.header("Desvantagens do Algoritmo K-means")
    st.write("""
    No entanto, o K-means apresenta algumas desvantagens:

    - **Número de Clusters**: É necessário especificar o número de clusters \(k\) a priori, o que pode não ser trivial.
    - **Sensibilidade a Outliers**: Pode ser sensível a outliers e ruído nos dados.
    - **Início dos Centroides**: A escolha inicial dos centroides pode afetar a qualidade da solução final.
    - **Forma dos Clusters**: Supõe que os clusters têm forma esférica e tamanho similar, o que pode não ser verdadeiro para todos os dados.
    """)

    # Conclusão
    st.header("Conclusão")
    st.write("""
    O **algoritmo K-means** é uma técnica popular e eficaz para agrupamento de dados, especialmente útil quando o número de clusters é conhecido e os dados têm uma estrutura clara. Embora seja eficiente e fácil de implementar, suas limitações devem ser consideradas, e pode ser necessário usar técnicas adicionais para melhorar o desempenho e a robustez do agrupamento.
    """)

    # Exemplo prático com dados gerados
    st.header("Exemplo Prático: Agrupamento de Dados com K-means")

    # Gerar dados de exemplo
    X = generate_data()

    # Parâmetros de clusters
    n_clusters = st.slider("Número de Clusters", 1, 10, 4)

    # Aplicar K-means
    kmeans = apply_kmeans(X, n_clusters)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    # Visualizar clusters
    st.subheader("Visualização dos Clusters")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=labels, palette="Set2", s=50, alpha=0.7, edgecolor='w')
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
    plt.title("Visualização dos Clusters com K-means")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    st.pyplot(plt)

    # Exibir centros dos clusters
    st.subheader("Centros dos Clusters")
    st.write(pd.DataFrame(centers, columns=["Feature 1", "Feature 2"]))

# Execução do código no Streamlit
if __name__ == "__main__":
    show_kmeans()
