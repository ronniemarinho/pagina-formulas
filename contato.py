import streamlit as st

def show_contato():
    st.markdown("<h2>Contato</h2>", unsafe_allow_html=True)
    st.write("Preencha o formulário para entrar em contato comigo.")
    with st.form(key='contact_form'):
        name = st.text_input("Nome")
        email = st.text_input("Email")
        message = st.text_area("Mensagem")
        submit_button = st.form_submit_button("Enviar")
        if submit_button:
            st.write(f"Obrigado, {name}! Sua mensagem foi enviada.")
