import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix, classification_report

def show_knn():
    st.title("Algoritmo K-Nearest Neighbors (KNN)")

    # Introdução ao KNN
    st.header("Introdução ao KNN")
    st.write("""
    O algoritmo K-Nearest Neighbors (KNN) é um classificador baseado em instâncias que faz previsões com base na proximidade dos dados. 
    Para um ponto de dados de teste, o KNN identifica os \( K \) pontos de treinamento mais próximos e faz a previsão com base na maioria das classes desses pontos vizinhos.
    """)

    # Fórmula de Distância Euclidiana
    st.header("Distância Euclidiana")
    st.latex(r'd(x, x_{i}) = \sqrt{\sum_{j=1}^{n} (x_j - x_{ij})^2}')
    st.write("""
    A distância euclidiana é frequentemente usada para medir a similaridade entre dois pontos. 
    Onde \( x \) é o ponto de teste e \( x_{i} \) é um ponto de treinamento. 
    A fórmula calcula a raiz quadrada da soma das diferenças quadráticas em cada dimensão.
    """)

    # Outras Métricas de Distância
    st.header("Outras Métricas de Distância")

    st.subheader("Distância de Manhattan")
    st.latex(r'd(x, x_{i}) = \sum_{j=1}^{n} |x_j - x_{ij}|')
    st.write("""
    A distância de Manhattan calcula a soma das diferenças absolutas entre as coordenadas. 
    É útil quando as diferenças absolutas são mais significativas do que as quadráticas.
    """)

    st.subheader("Distância de Minkowski")
    st.latex(r'd(x, x_{i}) = \left( \sum_{j=1}^{n} |x_j - x_{ij}|^p \right)^{1/p}')
    st.write("""
    A distância de Minkowski é uma generalização das distâncias Euclidiana e de Manhattan, onde \( p \) é um parâmetro que determina o tipo de distância:
    - \( p = 1 \): Distância de Manhattan
    - \( p = 2 \): Distância Euclidiana
    """)

    st.subheader("Distância de Chebyshev")
    st.latex(r'd(x, x_{i}) = \max_{j} |x_j - x_{ij}|')
    st.write("""
    A distância de Chebyshev considera a maior diferença absoluta entre as coordenadas. 
    É útil em problemas onde se deseja limitar a diferença máxima entre as características.
    """)

    # Importância da Escolha do Valor de K
    st.header("Importância da Escolha do Valor de \( K \)")
    st.write("""
    A escolha do valor de \( K \) é crítica para o desempenho do algoritmo KNN:

    - **Valor de K pequeno**:
        - Pode levar a um modelo com alta variância, sensível ao ruído nos dados (**overfitting**).
        - O modelo pode captar padrões específicos do conjunto de treinamento que não generalizam bem.
    - **Valor de K grande**:
        - Pode levar a um modelo com alta tendência, subestimando a estrutura dos dados (**underfitting**).
        - O modelo pode ser muito generalista e não captar padrões importantes.

    É comum usar técnicas de validação cruzada para encontrar o valor ótimo de \( K \) para um conjunto de dados específico.
    """)

    # Importância da Escolha da Métrica de Distância
    st.header("Importância da Escolha da Métrica de Distância")
    st.write("""
    A métrica de distância define como a similaridade entre os pontos é medida. A escolha da métrica pode afetar significativamente o desempenho do KNN:

    - **Distância Euclidiana**:
        - Apropriada quando as características são contínuas e a escala é relevante.
    - **Distância de Manhattan**:
        - Útil quando as diferenças absolutas são mais importantes.
    - **Distância de Minkowski**:
        - Permite ajustar o parâmetro \( p \) para equilibrar entre Euclidiana e Manhattan.
    - **Distância de Chebyshev**:
        - Útil em cenários onde a máxima diferença é crucial.

    Além disso, é importante padronizar ou normalizar os dados antes de aplicar o KNN, especialmente quando as características têm escalas diferentes, para que nenhuma característica domine o cálculo da distância.
    """)

    # Principais Características do KNN
    st.header("Principais Características do KNN")
    st.write("""
    - **Não Paramétrico**: O KNN não faz suposições sobre a distribuição dos dados, o que o torna flexível para diferentes tipos de problemas.
    - **Baseado em Instâncias**: Armazena todos os dados de treinamento e faz previsões ao calcular distâncias durante a fase de teste.
    - **Simplicidade**: Fácil de entender e implementar, ideal para introdução aos conceitos de aprendizado de máquina.
    """)

    # Vantagens do KNN
    st.header("Vantagens do KNN")
    st.write("""
    1. **Simples e Intuitivo**: Fácil implementação e compreensão.
    2. **Flexibilidade**: Pode ser usado para problemas de classificação e regressão.
    3. **Eficaz com Dados Multiclasse**: Naturalmente lida com múltiplas classes sem necessidade de ajustes especiais.
    """)

    # Desvantagens do KNN
    st.header("Desvantagens do KNN")
    st.write("""
    1. **Custo Computacional Elevado**: Ineficiente para grandes conjuntos de dados devido ao cálculo de distâncias para todos os pontos.
    2. **Sensibilidade ao Ruído**: Outliers e ruído nos dados podem afetar significativamente o desempenho.
    3. **Dependência da Escala dos Dados**: Requer normalização ou padronização dos dados para evitar que características com maiores magnitudes dominem o cálculo de distância.
    """)

    # Conclusão
    st.header("Conclusão")
    st.write("""
    O algoritmo KNN é uma ferramenta poderosa e simples para tarefas de classificação e regressão. 
    Sua eficácia depende da escolha adequada do valor de \( K \) e da métrica de distância utilizada. 
    Embora tenha suas limitações, especialmente com grandes volumes de dados e alta dimensionalidade, 
    o KNN continua sendo uma abordagem valiosa em situações onde a simplicidade e a interpretabilidade são importantes.
    """)
