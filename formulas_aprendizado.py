import streamlit as st

st.title("Fórmulas de Aprendizado de Máquina")

# Métricas Avaliativas
st.header("Métricas Avaliativas")

# Fórmula da Acurácia
st.subheader("Acurácia")
st.latex(r'\text{Acurácia} = \frac{TP + TN}{TP + TN + FP + FN}')

# Fórmula da Precisão
st.subheader("Precisão")
st.latex(r'\text{Precisão} = \frac{TP}{TP + FP}')

# Fórmula do Recall
st.subheader("Recall")
st.latex(r'\text{Recall} = \frac{TP}{TP + FN}')

# Fórmula do F1-Score
st.subheader("F1-Score")
st.latex(r'F1 = 2 \cdot \frac{\text{Precisão} \cdot \text{Recall}}{\text{Precisão} + \text{Recall}}')

# Algoritmos de Classificação
st.header("Algoritmos de Classificação")

# Naive Bayes
st.subheader("Naive Bayes")
st.latex(r'P(C|X) = \frac{P(X|C) \cdot P(C)}{P(X)}')

# KNN
st.subheader("K-Nearest Neighbors (KNN)")
st.latex(r'd(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}')
st.write("Essa é a fórmula da distância euclidiana utilizada no KNN.")

# SVM (Máquinas de Vetores de Suporte)
st.subheader("SVM")
st.latex(r'w \cdot x + b = 0')
st.write("Essa é a fórmula que define o hiperplano em SVM.")

# Árvore de Decisão
st.subheader("Árvore de Decisão - Entropia")
st.latex(r'H(S) = - \sum_{i=1}^{c} p_i \log_2 p_i')

# Random Forest
st.subheader("Random Forest")
st.write("O algoritmo de Random Forest é composto por várias árvores de decisão independentes. A previsão final é uma média ponderada ou votação das previsões de cada árvore.")

# Redes Neurais
st.subheader("Redes Neurais")
st.latex(r'Z = W \cdot X + b')
st.latex(r'A = \sigma(Z)')
st.write("Essas fórmulas representam o funcionamento básico de um neurônio artificial, onde `Z` é o valor ponderado da entrada e `A` é a saída após a aplicação da função de ativação.")

# Algoritmos de Agrupamento
st.header("Algoritmos de Agrupamento")

# K-Means
st.subheader("K-Means")
st.latex(r'J = \sum_{i=1}^{k} \sum_{x_j \in C_i} ||x_j - \mu_i||^2')
st.write("Aqui `C_i` são os centróides e `x_j` são os dados pertencentes a esse centróide.")

# DBSCAN
st.subheader("DBSCAN")
st.write("O DBSCAN utiliza a noção de densidade de vizinhos, sem uma fórmula direta para isso. No entanto, ele define grupos com base em parâmetros como `eps` (distância) e `min_samples` (número mínimo de pontos próximos).")

# Agrupamento Hierárquico
st.subheader("Agrupamento Hierárquico")
st.latex(r'd(A, B) = \min_{a \in A, b \in B} d(a, b)')
st.write("Essa é a fórmula de ligação simples (single-link) para calcular a distância entre dois grupos de dados.")

# Algoritmos de Regras de Associação
st.header("Algoritmos de Regras de Associação")

# Apriori
st.subheader("Algoritmo Apriori")
st.latex(r'\text{Suporte}(A \Rightarrow B) = \frac{\text{Transações com } A \text{ e } B}{\text{Transações Totais}}')
st.latex(r'\text{Confiança}(A \Rightarrow B) = \frac{\text{Transações com } A \text{ e } B}{\text{Transações com } A}')

# Algoritmos de Regressão
st.header("Algoritmos de Regressão")

# Regressão Linear
st.subheader("Regressão Linear")
st.latex(r'y = \beta_0 + \beta_1 x')

# Regressão Linear Múltipla
st.subheader("Regressão Linear Múltipla")
st.latex(r'y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n')

# Regressão Polinomial
st.subheader("Regressão Polinomial")
st.latex(r'y = \beta_0 + \beta_1 x + \beta_2 x^2 + \dots + \beta_n x^n')

# Escalonamento de Dados
st.header("Escalonamento de Dados")

# Normalização
st.subheader("Normalização (Min-Max)")
st.latex(r'X_{\text{normalizado}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}')

# Padronização (Z-score)
st.subheader("Padronização (Z-score)")
st.latex(r'Z = \frac{X - \mu}{\sigma}')
st.write("Onde `μ` é a média dos dados e `σ` é o desvio padrão.")

# Outras Fórmulas Relevantes
st.header("Outras Fórmulas Relevantes")

# Função Sigmoide
st.subheader("Função Sigmoide")
st.latex(r'\sigma(x) = \frac{1}{1 + e^{-x}}')

# Função de Custo Logística (para classificação binária)
st.subheader("Função de Custo Logística")
st.latex(r'J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} [y^{(i)} \log h_\theta(x^{(i)}) + (1 - y^{(i)}) \log (1 - h_\theta(x^{(i)}))]')

import streamlit as st

st.title("Fórmulas de Aprendizado de Máquina")

# Funções de Ativação para Redes Neurais
st.header("Funções de Ativação para Redes Neurais")

# Função Sigmoide
st.subheader("Função Sigmoide")
st.latex(r'\sigma(x) = \frac{1}{1 + e^{-x}}')

# Função Degrau (Step Function)
st.subheader("Função Degrau")
st.latex(r'\text{Step}(x) = \begin{cases} 1 & \text{se } x \geq 0 \\ 0 & \text{se } x < 0 \end{cases}')

# Função ReLU (Rectified Linear Unit)
st.subheader("Função ReLU")
st.latex(r'\text{ReLU}(x) = \max(0, x)')

# Seleção de Atributo em Árvore de Decisão
st.header("Seleção de Atributo em Árvore de Decisão")

# Fórmula do Ganho de Informação
st.subheader("Ganho de Informação")
st.latex(r'\text{Ganho de Informação} = \text{Entropia}(S) - \sum_{v \in \text{Valores}} \frac{|S_v|}{|S|} \cdot \text{Entropia}(S_v)')
st.write("Onde `S` representa o conjunto de exemplos e `S_v` representa os exemplos que têm valor `v` para o atributo.")

# Fórmulas para o KNN
st.header("Distâncias e Correlações Utilizadas no KNN")

# Distância de Minkowski
st.subheader("Distância de Minkowski")
st.latex(r'd(x, y) = \left( \sum_{i=1}^{n} |x_i - y_i|^p \right)^{1/p}')
st.write("A Distância de Minkowski é uma generalização das distâncias de Manhattan e Euclidiana, com `p` como um parâmetro.")

# Distância de Manhattan (caso especial de Minkowski com p=1)
st.subheader("Distância de Manhattan")
st.latex(r'd(x, y) = \sum_{i=1}^{n} |x_i - y_i|')

# Coeficiente de Correlação de Pearson
st.subheader("Coeficiente de Correlação de Pearson")
st.latex(r'r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2 \sum_{i=1}^{n}(y_i - \bar{y})^2}}')
st.write("O Coeficiente de Correlação de Pearson mede a força e a direção da relação linear entre duas variáveis.")

# Importância de `k` no KNN
st.header("Importância do Valor de k no KNN")
st.write("""
O valor de `k` no K-Nearest Neighbors (KNN) define o número de vizinhos mais próximos considerados para classificar um novo ponto de dados. Um `k` pequeno pode resultar em alta variância e overfitting, enquanto um `k` muito grande pode levar a underfitting, pois a decisão será influenciada por muitos vizinhos, potencialmente de classes diferentes.
""")

# Fórmulas Adicionais (opcional)
st.header("Outras Fórmulas Importantes em Aprendizado de Máquina")

# Normalização
st.subheader("Normalização (Min-Max Scaling)")
st.latex(r'x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}')

# Padronização (Z-score)
st.subheader("Padronização (Z-score)")
st.latex(r'z = \frac{x - \mu}{\sigma}')
st.write("Onde `μ` é a média e `σ` é o desvio padrão da amostra.")

# Fórmula de Regressão Linear Simples
st.subheader("Regressão Linear Simples")
st.latex(r'y = \beta_0 + \beta_1 x')

# Fórmula de Regressão Linear Múltipla
st.subheader("Regressão Linear Múltipla")
st.latex(r'y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n')

# Fórmula de Regressão Polinomial
st.subheader("Regressão Polinomial")
st.latex(r'y = \beta_0 + \beta_1 x + \beta_2 x^2 + \dots + \beta_n x^n')
