import streamlit as st

def show_pre_processamento():
    st.title("Fórmulas de Pré-processamento em Aprendizado de Máquina")

    # Normalização (Min-Max Scaling)
    st.header("Normalização (Min-Max Scaling)")
    st.latex(r'X_{\text{normalizado}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}')
    st.write("""
    A normalização ajusta os valores dos atributos para que eles fiquem em uma escala fixa, normalmente entre 0 e 1. 
    Essa técnica é útil quando os dados apresentam escalas diferentes.
    """)

    # Padronização (Z-score Standardization)
    st.header("Padronização (Z-score Standardization)")
    st.latex(r'Z = \frac{X - \mu}{\sigma}')
    st.write("""
    A padronização transforma os dados para que tenham média 0 e desvio padrão 1. 
    Ela é utilizada quando os atributos possuem distribuições gaussianas.
    """)

    # Binarização (Thresholding)
    st.header("Binarização")
    st.latex(r'X_{\text{binarizado}} = \begin{cases} 1 & \text{se } X > T \\ 0 & \text{se } X \leq T \end{cases}')
    st.write("""
    A binarização converte os valores dos dados para 0 ou 1 com base em um limite \(T\). 
    Essa técnica é usada para transformar atributos contínuos em binários.
    """)

    # Imputação de Dados Faltantes (pela Média)
    st.header("Imputação de Dados Faltantes (Média)")
    st.latex(r'X_{\text{imputado}} = \frac{1}{n} \sum_{i=1}^{n} X_i')
    st.write("""
    A imputação pela média substitui os valores faltantes pela média dos valores observados do atributo. 
    Essa técnica é útil para lidar com dados ausentes de maneira simples e eficaz.
    """)

    # Imputação de Dados Faltantes (Mediana)
    st.header("Imputação de Dados Faltantes (Mediana)")
    st.latex(r'X_{\text{imputado}} = \text{Mediana}(X)')
    st.write("""
    A imputação pela mediana substitui os valores faltantes pela mediana dos valores observados do atributo. 
    Essa técnica é útil quando os dados são assimétricos ou contêm outliers, pois a mediana é menos sensível a valores extremos.
    """)

    # Moda
    st.header("Imputação de Dados Faltantes (Moda)")
    st.latex(r'\text{Moda} = \text{valor que aparece com maior frequência}')
    st.write("""
    A moda é o valor ou valores que ocorrem com mais frequência em um conjunto de dados. 
    Pode haver mais de uma moda se vários valores aparecerem com a mesma frequência máxima.
    """)

    # Codificação One-Hot
    st.header("Codificação One-Hot (One-Hot Encoding)")
    st.latex(r'X_{\text{one-hot}} = \begin{cases} 1 & \text{se a categoria é a mesma} \\ 0 & \text{caso contrário} \end{cases}')
    st.write("""
    A codificação One-Hot transforma variáveis categóricas em variáveis binárias. 
    Cada categoria de uma variável categórica é representada por uma nova coluna binária, facilitando a entrada para algoritmos de aprendizado de máquina.
    """)
