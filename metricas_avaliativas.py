import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, auc

def show_metricas_avaliativas():
    st.title("Métricas Avaliativas em Aprendizado de Máquina")

    # Acurácia
    st.header("Acurácia")
    st.latex(r'\text{Acurácia} = \frac{\text{Número de Previsões Corretas}}{\text{Número Total de Previsões}}')
    st.write("""
    A acurácia é a proporção de previsões corretas em relação ao total de previsões feitas. 
    É uma métrica útil quando as classes estão equilibradas.
    """)

    # Precisão
    st.header("Precisão")
    st.latex(r'\text{Precisão} = \frac{\text{Verdadeiros Positivos}}{\text{Verdadeiros Positivos} + \text{Falsos Positivos}}')
    st.write("""
    A precisão é a proporção de verdadeiros positivos em relação ao total de previsões positivas feitas. 
    É útil quando o custo de falsos positivos é alto.
    """)

    # Revocação
    st.header("Revocação")
    st.latex(r'\text{Revocação} = \frac{\text{Verdadeiros Positivos}}{\text{Verdadeiros Positivos} + \text{Falsos Negativos}}')
    st.write("""
    A revocação é a proporção de verdadeiros positivos identificados corretamente em relação ao total de positivos reais. 
    É útil quando o custo de falsos negativos é alto.
    """)

    # F1-Score
    st.header("F1-Score")
    st.latex(r'\text{F1-Score} = 2 \times \frac{\text{Precisão} \times \text{Revocação}}{\text{Precisão} + \text{Revocação}}')
    st.write("""
    O F1-Score é a média harmônica entre precisão e revocação. 
    É uma métrica importante quando há um trade-off entre precisão e revocação e é necessário equilibrar os dois.
    """)

    # Matriz de Confusão
    st.header("Matriz de Confusão")

    # Gerar dados de exemplo
    y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]

    # Calcular a matriz de confusão
    cm = confusion_matrix(y_true, y_pred)

    # Plotar a matriz de confusão
    fig, ax = plt.subplots(figsize=(2.5, 1.5))  # Ajuste o tamanho da figura aqui
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['Classe 0', 'Classe 1'], yticklabels=['Classe 0', 'Classe 1'],
                annot_kws={"size": 10})  # Ajuste o tamanho do texto das anotações
    ax.set_xlabel('Predito', fontsize=6)
    ax.set_ylabel('Real', fontsize=6)
    #ax.set_title('Matriz de Confusão', fontsize=7)
    ax.tick_params(axis='both', which='major', labelsize=5)  # Ajuste o tamanho dos rótulos dos eixos

    # Exibir a figura no Streamlit
    st.pyplot(fig)

    st.write("""
    A matriz de confusão é uma tabela que é frequentemente usada para descrever o desempenho de um modelo de classificação. 
    Ela mostra o número de previsões corretas e incorretas, divididas por classe.
    """)

    # Curva ROC e AUC
    st.header("Curva ROC e AUC")

    # Gerar dados de exemplo
    y_score = np.random.rand(len(y_true))  # Pontuações de exemplo
    fpr, tpr, _ = roc_curve(y_true, y_score)
    roc_auc = auc(fpr, tpr)

    # Plotar a curva ROC
    fig, ax = plt.subplots(figsize=(6, 4))  # Ajuste o tamanho da figura aqui
    ax.plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
    ax.plot([0, 1], [0, 1], color='grey', lw=2, linestyle='--')
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('Taxa de Falsos Positivos', fontsize=12)
    ax.set_ylabel('Taxa de Verdadeiros Positivos', fontsize=12)
    ax.set_title('Curva ROC', fontsize=14)
    ax.legend(loc='lower right', fontsize=10)

    # Exibir a figura no Streamlit
    st.pyplot(fig)

    st.write("""
    A Curva ROC (Receiver Operating Characteristic) é um gráfico que mostra a taxa de verdadeiros positivos em relação à taxa de falsos positivos para diferentes limiares de decisão. 
    A métrica AUC (Área sob a curva) quantifica a performance global do modelo, com valores mais altos indicando um melhor desempenho.
    """)
