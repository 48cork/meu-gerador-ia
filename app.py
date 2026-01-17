import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gerador de Negócios IA", page_icon="🚀")

with st.sidebar:
    st.title("Configuração")
    api_key = st.text_input("Insira sua Gemini API Key:", type="password")
    st.info("Obtenha sua chave gratuita em: aistudio.google.com")

st.title("🚀 Gerador de Ideias de Negócios")

with st.form("meu_formulario"):
    invest = st.text_input("Investimento disponível (Ex: R$ 500)")
    skill = st.text_input("Suas habilidades (Ex: Cozinha, Internet)")
    goal = st.text_input("Meta mensal (Ex: R$ 3000)")
    submit = st.form_submit_button(label='Gerar Plano de Negócio')

if submit:
    if not api_key:
        st.error("Por favor, insira sua API Key na barra lateral.")
    else:
        try:
            # Configuração simples e direta
            genai.configure(api_key=api_key)
            
            # Usando o nome do modelo sem o prefixo 'models/' para evitar conflito de URL
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"Sugira um negócio para quem tem {invest}, sabe {skill} e quer ganhar {goal}. Liste: 1. Conceito, 2. Kiwify, 3. Tráfego, 4. Bio."
            
            with st.spinner('A IA está pensando...'):
                response = model.generate_content(prompt)
                st.markdown("---")
                st.subheader("💡 Sua Oportunidade:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Erro: {e}")
