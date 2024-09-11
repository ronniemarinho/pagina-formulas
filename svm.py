import streamlit as st
import numpy as np


def show_svm():
    st.title("Algoritmo SVM (Support Vector Machine)")

    # Introdução ao SVM
    st.header("Introdução ao SVM")
    st.write("""
    A Máquina de Vetores de Suporte (SVM) é um algoritmo de aprendizado supervisionado amplamente utilizado para tarefas de classificação e regressão. 
    A ideia principal é encontrar um hiperplano em um espaço de alta dimensão que separa diferentes classes de maneira ótima. O SVM é muito eficaz em espaços de alta dimensão e é utilizado em diversas áreas, como classificação de texto e reconhecimento de imagens.
    """)

    # Hiperplano de Separação
    st.header("Hiperplano de Separação")
    st.write("""
    O objetivo do SVM é encontrar o hiperplano que melhor separa as diferentes classes. O hiperplano é uma linha de decisão que divide o espaço de características e maximiza a margem entre as classes. A margem é a distância entre o hiperplano e os vetores de suporte, que são os pontos de dados mais próximos ao hiperplano.
    """)

    st.subheader("Equação do Hiperplano")
    st.latex(r'w \cdot x + b = 0')
    st.write("""
    Onde:
    - \( w \) é o vetor de pesos (ou coeficientes),
    - \( x \) são os dados de entrada,
    - \( b \) é o termo de viés.
    """)

    # Margem Máxima
    st.header("Margem Máxima")
    st.write("""
    O SVM tenta maximizar a margem, ou seja, a distância entre o hiperplano de separação e os pontos de dados mais próximos (os vetores de suporte). Um modelo com uma margem maior geralmente tem uma melhor capacidade de generalização.
    """)

    # Tipos de SVM
    st.header("Tipos de SVM")

    st.subheader("SVM Linear")
    st.write("""
    O SVM Linear é utilizado quando os dados são linearmente separáveis, ou seja, é possível separar as classes com uma linha reta (ou plano, em dimensões mais altas).
    """)

    st.subheader("SVM com Kernel")
    st.write("""
    Quando os dados não são linearmente separáveis, o SVM usa **kernels** para projetar os dados em uma dimensão superior, onde eles se tornam separáveis. Os principais tipos de kernels incluem:

    - **Kernel Linear**: Mantém os dados em seu espaço original.
    - **Kernel Polinomial**: Mapeia os dados em uma dimensão polinomialmente superior.
    - **Kernel RBF (Radial Basis Function)**: Transforma os dados em uma dimensão infinita, com base na distância dos pontos centrais.
    """)

    # Fórmulas do SVM
    st.header("Função de Otimização do SVM")
    st.latex(r' \min_{w,b} \frac{1}{2} ||w||^2')
    st.write("""
    A função de otimização do SVM busca minimizar a norma do vetor de pesos \( w \), enquanto maximiza a margem entre as classes.
    """)

    # Vantagens e Desvantagens do SVM
    st.header("Vantagens e Desvantagens do SVM")

    st.subheader("Vantagens")
    st.write("""
    1. **Eficiente em Espaços de Alta Dimensão**: Funciona bem mesmo quando o número de características é maior que o número de amostras.
    2. **Uso de Kernels**: O SVM pode ser aplicado em casos onde as classes não são linearmente separáveis usando diferentes funções kernel.
    3. **Margem Máxima**: Garante uma boa capacidade de generalização, ao maximizar a margem de separação entre as classes.
    4. **Versátil**: Pode ser usado tanto para classificação quanto para regressão, através do SVR (Support Vector Regression).
    """)

    st.subheader("Desvantagens")
    st.write("""
    1. **Custo Computacional Alto**: O tempo de treinamento pode ser lento para grandes conjuntos de dados.
    2. **Escolha do Kernel**: A escolha do kernel e dos parâmetros (como o parâmetro \(C\)) pode ser complexa e requer ajuste fino.
    3. **Sensível a Dados Desequilibrados**: O SVM pode ter um desempenho ruim quando as classes estão desequilibradas.
    4. **Não Fornece Probabilidades**: As previsões do SVM não fornecem probabilidades diretamente, apenas uma classificação ou valor contínuo.
    """)

    # Aplicações de SVM
    st.header("Aplicações do SVM")
    st.write("""
    O SVM é amplamente utilizado em várias áreas, como:

    - **Classificação de Imagens**: Reconhecimento de faces, classificação de objetos.
    - **Classificação de Texto**: Categorias de e-mails, análise de sentimentos.
    - **Bioinformática**: Classificação de sequências biológicas e diagnóstico médico.
    - **Reconhecimento de Padrões**: Classificação de sinais e padrões em diversos campos.
    """)

    # Principais Características do SVM
    st.header("Principais Características do SVM")
    st.write("""
    - **Vetores de Suporte**: Apenas alguns pontos (vetores de suporte) são relevantes para determinar o hiperplano de separação, tornando o modelo eficiente em termos de memória.
    - **Versatilidade**: Pode ser usado com diferentes tipos de kernels para tratar problemas lineares e não lineares.
    - **Capacidade de Generalização**: Com a margem máxima, o SVM evita overfitting e generaliza bem em novos dados.
    """)

    # Conclusão
    st.header("Conclusão")
    st.write("""
    O SVM é um algoritmo poderoso e flexível para tarefas de classificação e regressão, especialmente em problemas complexos com dados de alta dimensionalidade. 
    Sua capacidade de usar kernels para transformar dados e maximizar a margem entre classes faz dele uma escolha popular em muitas aplicações práticas.
    """)


# Exibir no Streamlit
if __name__ == '__main__':
    show_svm()
