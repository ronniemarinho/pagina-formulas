import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_circles, make_moons
from sklearn.preprocessing import StandardScaler
import scipy.cluster.hierarchy as sch

# Função para gerar dados de exemplo
def generate_data(n_samples=300, noise=0.1):
    # Gera dados com duas formas complexas: círculos e luas
    X1, _ = make_circles(n_samples=n_samples//2, factor=0.5, noise=noise)
    X2, _ = make_moons(n_samples=n_samples//2, noise=noise)
    X = np.vstack((X1, X2))
    return X

# Função para aplicar o algoritmo de agrupamento hierárquico
def apply_hierarchical(X, n_clusters, linkage):
    model = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    labels = model.fit_predict(X)
    return labels

# Função para exibir os resultados no Streamlit
def show_hierarchical():
    st.title("Algoritmo de Agrupamento Hierárquico")

    # Introdução ao Algoritmo de Agrupamento Hierárquico
    st.header("Introdução ao Algoritmo de Agrupamento Hierárquico")
    st.write("""
    O **algoritmo de agrupamento hierárquico** é uma técnica que busca construir uma hierarquia de clusters. Existem duas abordagens principais para o agrupamento hierárquico:

    - **Aglomerativo**: Começa com cada ponto como um cluster separado e, a cada passo, une os clusters mais próximos até que todos os pontos estejam em um único cluster ou o número desejado de clusters seja atingido.
    - **Divisivo**: Começa com todos os pontos em um único cluster e, a cada passo, divide o cluster em subclusters até que cada ponto esteja em seu próprio cluster.

    O algoritmo pode ser visualizado através de um **dendrograma**, que ilustra a fusão ou divisão dos clusters em cada etapa.
    """)

    # Fórmulas Utilizadas
    st.subheader("Fórmulas Utilizadas")
    st.write("""
    O algoritmo de agrupamento hierárquico aglomerativo utiliza diferentes métodos de ligação para calcular a distância entre clusters:

    - **Ligação Simples**: Distância mínima entre pontos em diferentes clusters.
    - **Ligação Completa**: Distância máxima entre pontos em diferentes clusters.
    - **Ligação Média**: Distância média entre todos os pares de pontos em diferentes clusters.
    - **Ligação de Centroide**: Distância entre os centroides dos clusters.
    """)

    # Seção de características do algoritmo Hierárquico
    st.header("Características do Algoritmo Hierárquico")
    st.write("""
    O algoritmo de agrupamento hierárquico possui as seguintes características:

    - **Hierárquico**: Constrói uma árvore de clusters, chamada de dendrograma.
    - **Aglomerativo ou Divisivo**: Pode ser executado de forma aglomerativa ou divisiva.
    - **Não Requer Número de Clusters Pré-definido**: O número de clusters pode ser decidido com base no dendrograma.
    - **Visualização do Dendrograma**: Permite a visualização da estrutura hierárquica dos clusters.
    """)

    # Seção de vantagens
    st.header("Vantagens do Algoritmo Hierárquico")
    st.write("""
    O algoritmo de agrupamento hierárquico oferece várias vantagens:

    - **Visualização**: A visualização do dendrograma facilita a escolha do número de clusters.
    - **Não Necessita de Número de Clusters Inicial**: O número de clusters pode ser ajustado dinamicamente.
    - **Flexibilidade**: Pode ser aplicado com diferentes métodos de ligação para capturar diferentes tipos de estrutura de dados.
    """)

    # Seção de desvantagens
    st.header("Desvantagens do Algoritmo Hierárquico")
    st.write("""
    No entanto, o agrupamento hierárquico apresenta algumas desvantagens:

    - **Complexidade Computacional**: Pode ser computacionalmente caro para grandes conjuntos de dados.
    - **Sensibilidade a Ruído**: Pode ser sensível a ruídos e outliers.
    - **Menos Escalável**: Pode ter desempenho ruim em grandes conjuntos de dados.
    """)

    # Conclusão
    st.header("Conclusão")
    st.write("""
    O **algoritmo de agrupamento hierárquico** é uma técnica útil para explorar a estrutura dos dados e identificar clusters hierárquicos. Embora seja poderoso para entender a estrutura dos dados e decidir sobre o número de clusters, suas limitações de desempenho e escalabilidade devem ser consideradas.
    """)

    # Exemplo prático com dados gerados
    st.header("Exemplo Prático: Agrupamento de Dados com Hierárquico")

    # Gerar dados de exemplo
    X = generate_data()

    # Normalizar dados
    X_scaled = StandardScaler().fit_transform(X)

    # Parâmetros do agrupamento hierárquico
    n_clusters = st.slider("Número de Clusters", 2, 10, 3)
    linkage = st.selectbox("Método de Ligação", ["ward", "complete", "average", "single"])

    # Aplicar agrupamento hierárquico
    labels = apply_hierarchical(X_scaled, n_clusters, linkage)

    # Adicionar rótulos aos dados
    data = pd.DataFrame(X, columns=["Feature 1", "Feature 2"])
    data['Cluster'] = labels

    # Visualizar clusters
    st.subheader("Visualização dos Clusters")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data["Feature 1"], y=data["Feature 2"], hue=labels, palette="Set2", s=50, alpha=0.7, edgecolor='w')
    plt.title("Visualização dos Clusters com Agrupamento Hierárquico")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    st.pyplot(plt)

    # Gerar e exibir o dendrograma
    st.subheader("Dendrograma")
    plt.figure(figsize=(12, 8))
    Z = sch.linkage(X_scaled, method=linkage)
    sch.dendrogram(Z)
    plt.title("Dendrograma")
    plt.xlabel("Número de Amostras ou Cluster")
    plt.ylabel("Distância")
    st.pyplot(plt)

    # Exibir dados agrupados
    st.subheader("Dados Agrupados")
    st.write(data)

# Execução do código no Streamlit
if __name__ == "__main__":
    show_hierarchical()
