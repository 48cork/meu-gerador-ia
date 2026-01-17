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
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            headers = {'Content-Type': 'application/json'}
            prompt = f"Sugira um negócio para quem tem R$ {invest}, sabe {skill} e quer ganhar R$ {goal}. Responda em Português, de forma curta e organizada."
            payload = {"contents": [{"parts": [{"text": prompt}]}]}

            with st.spinner('Conectando à IA...'):
                response = requests.post(url, headers=headers, json=payload)
                result = response.json()
                
                if 'candidates' in result:
                    texto_ia = result['candidates'][0]['content']['parts'][0]['text']
                    st.markdown("---")
                    st.success("### ✅ Plano Gerado")
                    st.write(texto_ia)
                else:
                    st.error(f"Erro do Google: {result.get('error', {}).get('message', 'Erro desconhecido')}")
        except Exception as e:
            st.error(f"Erro: {e}")
