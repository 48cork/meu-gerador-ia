import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gerador de Negócios IA", page_icon="🚀")

with st.sidebar:
    st.title("Configuração")
    api_key = st.text_input("Insira sua Gemini API Key:", type="password")
    st.info("Obtenha sua chave gratuita em: aistudio.google.com")

st.title("🚀 Gerador de Ideias de Negócios")

with st.form("meu_formulario"):
    investimento = st.text_input("Quanto você tem para investir? (Ex: R$ 500)")
    habilidades = st.text_input("Quais suas habilidades? (Ex: Cozinha, Internet)")
    objetivo = st.text_input("Quanto quer ganhar por mês? (Ex: R$ 3000)")
    submit_button = st.form_submit_button(label='Gerar Plano de Negócio')

if submit_button:
    if not api_key:
        st.error("Por favor, insira sua API Key na barra lateral.")
    else:
        try:
            # Comando para forçar a versão estável
            genai.configure(api_key=api_key, transport='rest') 
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"Sugira um negócio para quem tem R$ {investimento}, sabe {habilidades} e quer ganhar R$ {objetivo}. Liste: 1. Conceito, 2. Kiwify, 3. Tráfego, 4. Bio."
            
            with st.spinner('IA analisando...'):
                response = model.generate_content(prompt)
                st.markdown("---")
                st.write(response.text)
        except Exception as e:
            st.error(f"Erro: {e}")
            st.error(f"Erro ao conectar com a IA: {e}")
   
