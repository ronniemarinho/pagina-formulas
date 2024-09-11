import streamlit as st
from pre_processamento import show_pre_processamento
from metricas_avaliativas import show_metricas_avaliativas
from knn import show_knn
from naive import show_naive_bayes
from arvore import show_decision_tree
from svm import show_svm
from redesneurais import show_single_layer_perceptron
from rede_multilayer import show_multilayer_perceptron
from random_forest import show_random_forest
from apriori import show_apriori
from kmeans import show_kmeans
from dbscam import show_dbscan
from hierarquico import show_hierarchical
from fuzy import show_fuzzy_logic
from a_estrela import show_astar
from gulosa import show_greedy_search
from genetico import show_genetic_algorithm
#from tratamento_base import show_data_processing


def show_disciplina(conteudo):
    if conteudo == 'Pré-processamento':
        show_pre_processamento()
        # Adicione detalhes específicos sobre Pré-processamento aqui
    elif conteudo == 'Naive Bayes':
        show_naive_bayes()
    elif conteudo == 'Busca Gulosa':
        show_greedy_search()
    elif conteudo == 'Algoritmo Genético':
        show_genetic_algorithm()
    elif conteudo == 'Busca A*':
        show_astar()
    elif conteudo == 'KNN':
        show_knn()
   # elif conteudo == 'Tratamento de Base de Dados':
       # show_data_processing()
    elif conteudo == 'Apriori':
        show_apriori()
    elif conteudo == 'Lógica Fuzzy':
        show_fuzzy_logic()
    elif conteudo == 'DBSCAN':
        show_dbscan()
        # Adicione detalhes específicos sobre Algoritmos aqui
    elif conteudo == 'Métricas de Avaliação':
        show_metricas_avaliativas()
        # Adicione detalhes específicos sobre Métricas de Avaliação aqui
    elif conteudo == 'Árvore de Decisão':
        show_decision_tree()
    elif conteudo == 'Redes Neurais de uma Camada':
        show_single_layer_perceptron()
    elif conteudo == 'Redes Neurais Multicamada':
        show_multilayer_perceptron()
    elif conteudo == 'Random Forest':
        show_random_forest()
    elif conteudo == 'SVM':
        show_svm()
    elif conteudo == 'KMeans':
        show_kmeans()
    elif conteudo == 'Agrupamento Hierárquico':
        show_hierarchical()
        # Adicione detalhes específicos sobre Busca Heurística aqui
    elif conteudo == 'Lógica Fuzzy':
        st.write("Aqui está o conteúdo sobre Lógica Fuzzy.")
        # Adicione detalhes específicos sobre Lógica Fuzzy aqui
    elif conteudo == 'Algoritmos Genéticos':
        st.write("Aqui está o conteúdo sobre Algoritmos Genéticos.")
        # Adicione detalhes específicos sobre Algoritmos Genéticos aqui
    elif conteudo == 'Paradigmas Emergentes':
        st.write("Aqui está o conteúdo sobre Paradigmas Emergentes em Ciência de Dados.")
        # Adicione detalhes específicos sobre Paradigmas Emergentes aqui
    elif conteudo == 'Ciência de Dados e Marketing Digital':
        st.write("Aqui está o conteúdo sobre Ciência de Dados e Marketing Digital.")
        # Adicione detalhes específicos sobre Ciência de Dados e Marketing Digital aqui


def show_portfolio():

    # st.image("project1.jpg", caption="Projeto 1")
    # st.image("project2.jpg", caption="Projeto 2")
    st.title("Conteúdos das Disciplinas")

    disciplina = st.selectbox(
        'Escolha uma disciplina:',
        ['Aprendizado de Máquina', 'Inteligência Computacional']
    )

    if disciplina == 'Aprendizado de Máquina':
        conteudo = st.selectbox(
            'Escolha um tópico:',
            ['Pré-processamento','Naive Bayes','KNN','Árvore de Decisão','Random Forest','SVM','Redes Neurais de uma Camada','Redes Neurais Multicamada','Apriori','KMeans','DBSCAN','Agrupamento Hierárquico','Métricas de Avaliação','Tratamento de Base de Dados']
        )
    elif disciplina == 'Inteligência Computacional':
        conteudo = st.selectbox(
            'Escolha um tópico:',
            ['Busca A*','Busca Gulosa', 'Lógica Fuzzy', 'Algoritmo Genético']
        )
    elif disciplina == 'Paradigmas Emergentes em Ciência de Dados':
        conteudo = 'Paradigmas Emergentes'
    elif disciplina == 'Ciência de Dados e Marketing Digital':
        conteudo = 'Ciência de Dados e Marketing Digital'

    show_disciplina(conteudo)

