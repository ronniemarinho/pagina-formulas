import streamlit as st
from sobre import show_sobre
from disciplina import show_portfolio
from servicos import show_servicos
from contato import show_contato

# Configuração da página
st.set_page_config(
    page_title="Professor Dr. Ronnie - Portfólio",
    page_icon=":book:",
    layout="wide"
)

# Mostrar imagem centralizada
def show_image():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("iaia.png", width=400)

show_image()

# Centralizar o título após a imagem
st.markdown("<h1 style='text-align: center;'>Horizonte IA</h1>", unsafe_allow_html=True)

# Adicionar o CSS para centralizar o menu e ajustar o rodapé
st.markdown(
    """
    <style>
    div[role="tablist"] {
        display: flex;
        justify-content: center;
    }
    div[role="tab"] {
        font-size: 20px !important;
        font-weight: bold;
    }
    .footer {
        background-color: black;
        color: white;
        padding: 20px;
        text-align: center;
        width: 100%;
        position: relative;
        bottom: 0;
    }
    .footer a {
        color: white;
        text-decoration: none;
        margin: 0 10px;
    }
    .footer a:hover {
        color: #ff7f0e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Criação das abas do menu com cabeçalhos markdown para simular tamanhos maiores
tab1, tab2, tab3, tab4 = st.tabs(["# Sobre", "# Disciplinas", "# Ferramentas e Aplicações", "# Contato"])

# Conteúdo de cada aba
with tab1:
    show_sobre()

with tab2:
    show_portfolio()

with tab3:
    show_servicos()

with tab4:
    show_contato()

# Rodapé com redes sociais e informações úteis
st.markdown(
    """
    <div class="footer">
        <p>Conecte-se nas redes sociais:</p>
        <a href="https://www.linkedin.com/in/ronnie-shida-89360175/?originalSubdomain=br" target="_blank">LinkedIn</a> |
        <a href="https://www.instagram.com/ronnieshida/" target="_blank">Instagram</a> |
        <a href="http://lattes.cnpq.br/6250414900321960" target="_blank">Lattes</a> |
        <a href="https://web.facebook.com/ronnie.shida" target="_blank">Facebook</a> |
        <a href="mailto:ronnie.marinho@fatec.sp.gov.br">Email</a>
        <br><br>
        <p>&copy; 2024 Professor Dr. Ronnie. </p>
        <p>Todos os direitos reservados.</p>
    </div>
    """,
    unsafe_allow_html=True
)
