
                import streamlit as st
import requests
import json

st.set_page_config(page_title="Business AI Pro", page_icon="💰", layout="wide")

with st.sidebar:
    st.title("Configuração")
    api_key = st.text_input("Sua Gemini API Key:", type="password")
    st.info("Obtenha em: aistudio.google.com")

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
            # ESTA É A URL EXATA QUE O GOOGLE EXIGE EM 2026
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            
            headers = {'Content-Type': 'application/json'}
            
            prompt = f"Sugira um negócio para quem tem R$ {invest}, sabe {skill} e quer ganhar R$ {goal}. Responda em Português, de forma curta e organizada."
            
            payload = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }]
            }

            with st.spinner('Conectando ao cérebro da IA...'):
                response = requests.post(url, headers=headers, json=payload)
                result = response.json()
                
                if 'error' in result:
                    # Se der erro, vamos mostrar exatamente o que o Google diz
                    st.error(f"Erro do Google: {result['error']['message']}")
                    st.info("Dica: Verifique se sua chave foi criada no site aistudio.google.com")
                elif 'candidates' in result:
                    texto_ia = result['candidates'][0]['content']['parts'][0]['text']
                    st.markdown("---")
                    st.success("### ✅ Plano de Negócio Gerado")
                    st.write(texto_ia)
                else:
                    st.error("Ocorreu um erro inesperado.")
                    st.write("Resposta do servidor:", result)

        except Exception as e:
            st.error(f"Erro de conexão: {e}")
