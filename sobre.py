import streamlit as st

def show_sobre():
    col1, col2, col3 = st.columns([1, 1, 1])  # Cria 3 colunas com largura diferente



    def show_image():
        col1, col2, col3 = st.columns([1, 1, 1])  # Cria 3 colunas com largura diferente

        with col2:  # Utiliza a coluna do meio para centralizar
            st.image("ronnie_serio.jpg", caption="Prof. Dr. Ronnie Shida Marinho",
                     use_column_width='true',width=400)  # Ajusta o tamanho da imagem

    show_image()

    st.write("""
        Sobre o Professor Dr. Ronnie

Sou Doutor em Ciência da Informação pela Universidade Estadual Paulista (UNESP-CAPES 7), Mestre em Ciências da Computação e Matemática Computacional pela Universidade de São Paulo (USP-CAPES 7), Especialista em Metodologias em Educação a Distância pela Universidade Virtual de São Paulo (UNIVESP) e Bacharel em Ciências da Computação pelo Centro Universitário Eurípedes de Marília (UNIVEM - bolsista PROUNI integral). Também sou Técnico em Programação de Computadores pelo Centro Paula Souza (ETEC).

Minha trajetória acadêmica e profissional é marcada por uma ampla experiência em docência de nível superior e técnico. Lecionei nas seguintes instituições: UNESP (2023), IFSP (2021-2022), FATEC (2019-2021), UNIVESP (facilitador de 2019 a 2021) e Prefeitura Municipal de Tupã (2018-2019). Atualmente, sou professor efetivo da FATEC Adamantina no curso de Ciência de Dados, onde atuo na área de ensino, pesquisa e extensão da instituição. Meu foco é em Inteligência Artificial e Aprendizado de Máquina, com ênfase em temas como análise de sentimento, sistemas de recomendação, processamento de linguagem natural, mineração de dados e inteligência computacional. Também faço parte do grupo de estudos em web semântica e análise de dados da USP (NEWSDA).

Com vasta experiência em ensino e pesquisa, oriento alunos e desenvolvo projetos inovadores focados em inteligência artificial e suas aplicações em várias áreas.
    """)
