import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gerador de Negócios IA", page_icon="🚀")

with st.sidebar:
    st.title("Configuração")
    api_key = st.text_input("Insira sua Gemini API Key:", type="password")
    st.info("Obtenha sua chave gratuita em: aistudio.google.com")

st.title("🚀 Gerador de Ideias de Negócios")
st.write("Transforme seu perfil em um plano de negócios lucrativo.")

with st.form("meu_formulario"):
    investimento = st.text_input("Quanto você tem para investir? (Ex: R$ 500)")
    habilidades = st.text_input("Quais suas habilidades/hobbies? (Ex: Cozinha, Internet)")
    objetivo = st.text_input("Quanto quer ganhar por mês? (Ex: R$ 3000)")
    submit_button = st.form_submit_button(label='Gerar Plano de Negócio')

if submit_button:
    if not api_key:
        st.error("Por favor, insira sua API Key na barra lateral.")
    else:
        try:
            genai.configure(api_key=api_key)
            # Alteração para a versão de produção estável:
            model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
            
            prompt = f"Aja como um estrategista de vendas. Sugira um negócio para quem tem R$ {investimento}, sabe sobre {habilidades} e quer ganhar R$ {objetivo}. Liste: 1. Conceito, 2. O que buscar na Kiwify, 3. Tráfego, 4. Frase Bio."
            
            with st.spinner('IA analisando...'):
                response = model.generate_content(prompt)
                st.markdown("---")
                st.subheader("💡 Sua Oportunidade:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Erro ao conectar com a IA: {e}")
   
