import streamlit as st
import requests
import json

st.set_page_config(page_title="Business AI Pro", page_icon="💰", layout="wide")

with st.sidebar:
    st.title("Configuração")
    api_key = st.text_input("Sua Gemini API Key:", type="password")

st.title("🚀 Consultoria de Negócios com IA")

col1, col2, col3 = st.columns(3)
with col1:
    invest = st.text_input("Investimento (R$)", value="500")
with col2:
    skill = st.text_input("Habilidade", value="Internet")
with col3:    
    goal = st.text_input("Meta Mensal (R$)", value="3000")

if st.button("Gerar Estratégia Profissional"):
    if not api_key:
        st.error("Por favor, insira sua API Key na lateral!")
    else:
        try:
            # AQUI ESTÁ A MUDANÇA: Usamos 'gemini-pro' e a versão 'v1beta'
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
            
            headers = {'Content-Type': 'application/json'}
            
            prompt = f"Sugira um negócio para quem tem R$ {invest}, sabe {skill} e quer ganhar R$ {goal}. Responda em Português, de forma curta e organizada."
            
            payload = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }]
            }

            with st.spinner('O Gemini Pro está analisando seu mercado...'):
                response = requests.post(url, headers=headers, json=payload)
                result = response.json()
                
                if 'error' in result:
                    st.error(f"Erro do Google: {result['error']['message']}")
                elif 'candidates' in result:
                    texto_ia = result['candidates'][0]['content']['parts'][0]['text']
                    st.markdown("---")
                    st.success("### ✅ Estratégia Gerada pelo Gemini Pro")
                    st.write(texto_ia)
                else:
                    st.error("Resposta inesperada. Verifique se sua chave API está ativa.")

        except Exception as e:
            st.error(f"Erro de conexão: {e}")
