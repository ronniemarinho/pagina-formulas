import streamlit as st


def show_servicos():
    st.markdown("<h2>Ferramentas e Aplicações</h2>", unsafe_allow_html=True)
    st.write("""
        Ofereço os seguintes serviços:
        - **Consultoria em Ciência de Dados:** Ofereço consultoria para empresas e instituições.
        - **Ensino e Treinamento:** Ministro cursos e treinamentos em ciência de dados.
    """)

    st.markdown("<h3>Meus Aplicativos</h3>", unsafe_allow_html=True)

    # Adicione links para seus aplicativos
    st.markdown("""
        <ul>
            <li><a href="https://logicafuzzyacademico.streamlit.app/" target="_blank">App de Lógica Fuzzy Acadêmico</a>: Um aplicativo que utiliza lógica fuzzy para avaliações e decisões.</li>
            <li><a href="https://previsaotemporedes.streamlit.app/" target="_blank">Previsão do tempo com redes neurais</a>: Aplicativo para a classificação do tempo</li>
            <li><a href="https://regressaolinear.streamlit.app/" target="_blank">Regressão Linear para compra de uma casa</a>: Aplicativo para predição de valor de uma casa</li>
            <li><a href="https://previsaotemporedes.streamlit.app/" target="_blank">Previsão do tempo com redes neurais</a>: Aplicativo para a classificação do tempo</li>
            <li><a href="https://vendadashboard.streamlit.app/" target="_blank">Dashboard</a>: Dashboard de Vendas</li>
            <li><a href="https://chatbootfatec.streamlit.app/" target="_blank">Chatboot</a>: Chatboot de vestibular</li>
            <li><a href="https://otimizandobusca.streamlit.app/" target="_blank">Otimizando Rota</a>: Aplicativo para encontrar o menor caminho</li>
            <li><a href="https://sentimentotweet.streamlit.app/" target="_blank">Análise de sentimento</a>: Aplicativo para a classificação de sentimento em textos do tweeter</li>

        </ul>
    """, unsafe_allow_html=True)


# Execução do código no Streamlit
if __name__ == "__main__":
    show_servicos()
