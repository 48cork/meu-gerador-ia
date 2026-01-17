import streamlit as st
import google.generativeai as genai
import json

st.set_page_config(page_title="Business AI Pro", page_icon="💰", layout="wide")

# Interface lateral
with st.sidebar:
    st.title("Configuração")
    api_key = st.text_input("Sua Gemini API Key:", type="password")

st.title("🚀 Consultoria de Negócios com IA")
st.write("Gere um plano estruturado em segundos.")

# Formulário de entrada
col1, col2, col3 = st.columns(3)
with col1:
    invest = st.text_input("Investimento (R$)", value="500")
with col2:
    skill = st.text_input("Habilidade", value="Cozinha")
with col3:
    goal = st.text_input("Meta Mensal (R$)", value="3000")

if st.button("Gerar Estratégia Profissional"):
    if not api_key:
        st.error("Insira sua API Key na lateral!")
    else:
        try:
            genai.configure(api_key=api_key)
            # Configura a IA para responder estritamente em JSON
            model = genai.GenerativeModel(
                model_name='gemini-1.5-flash',
                generation_config={"response_mime_type": "application/json"}
            )
            
            prompt = f"""
            Crie um plano de negócio para: Investimento R$ {invest}, Habilidade {skill}, Meta R$ {goal}.
            Responda EXCLUSIVAMENTE no formato JSON com as chaves: 
            'nome_negocio', 'conceito', 'passo_a_passo', 'estrategia_kiwify', 'bio_insta'.
            """
            
            with st.spinner('Processando dados...'):
                response = model.generate_content(prompt)
                # Transforma o texto da IA em um objeto JSON (dicionário)
                dados = json.loads(response.text)
                
                # Exibição organizada na tela
                st.success(f"### Negócio: {dados['nome_negocio']}")
                
                c1, c2 = st.columns(2)
                with c1:
                    st.info(f"**💡 Conceito:**\n\n{dados['conceito']}")
                    st.warning(f"**🎯 Estratégia Kiwify:**\n\n{dados['estrategia_kiwify']}")
                with c2:
                    st.success(f"**📝 Passo a Passo:**\n\n{dados['passo_a_passo']}")
                    st.code(f"Bio Sugerida:\n{dados['bio_insta']}", language="text")

        except Exception as e:
            st.error(f"Erro na geração: {e}")
