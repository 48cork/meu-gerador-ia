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
    skill = st.text_input("Habilidade", value="Cozinha")
with col3:    
    goal = st.text_input("Meta Mensal (R$)", value="3000")

if st.button("Gerar Estratégia Profissional"):
    if not api_key:
        st.error("Insira sua API Key!")
    else:
        try:
            # Endereço DIRETO da API v1 (Aqui não tem erro de v1beta!)
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
            
            headers = {'Content-Type': 'application/json'}
            
            prompt = f"Crie um plano de negócio para: Investimento R$ {invest}, Habilidade {skill}, Meta R$ {goal}. Responda EXCLUSIVAMENTE em JSON com as chaves: 'nome_negocio', 'conceito', 'passo_a_passo', 'estrategia_kiwify', 'bio_insta'."
            
            payload = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"response_mime_type": "application/json"}
            }

            with st.spinner('Conectando diretamente ao satélite da IA...'):
                response = requests.post(url, headers=headers, json=payload)
                result = response.json()
                
                # Extraindo o texto do JSON que o Google envia
                texto_ia = result['candidates'][0]['content']['parts'][0]['text']
                dados = json.loads(texto_ia)
                
                st.success(f"### Negócio: {dados['nome_negocio']}")
                c1, c2 = st.columns(2)
                with c1:
                    st.info(f"**💡 Conceito:**\n\n{dados['conceito']}")
                    st.warning(f"**🎯 Estratégia Kiwify:**\n\n{dados['estrategia_kiwify']}")
                with c2:
                    st.success(f"**📝 Passo a Passo:**\n\n{dados['passo_a_passo']}")
                    st.code(f"Bio Sugerida:\n{dados['bio_insta']}", language="text")

        except Exception as e:
            st.error(f"Erro na conexão direta: {e}")
            st.write("Resposta do servidor:", result) # Isso nos ajudará a ver o que houve
