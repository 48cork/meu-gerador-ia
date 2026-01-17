import streamlit as st
import google.generativeai as genai

# Configuração visual da página
st.set_page_config(page_title="Gerador de Negócios IA", page_icon="🚀")

# Barra lateral para configuração da Chave de API
with st.sidebar:
    st.title("Configuração")
    api_key = st.text_input("Insira sua Gemini API Key:", type="password")
    st.info("Obtenha sua chave gratuita em: aistudio.google.com")

st.title("🚀 Gerador de Ideias de Negócios 2026")
st.write("Transforme seu perfil em um plano de negócios lucrativo.")

# Formulário de entrada de dados
with st.form("meu_formulario"):
    investimento = st.text_input("Quanto você tem para investir? (Ex: R$ 500)")
    habilidades = st.text_input("Quais suas habilidades/hobbies? (Ex: Cozinha, Internet)")
    objetivo = st.text_input("Quanto quer ganhar por mês? (Ex: R$ 3000)")
    submit_button = st.form_submit_button(label='Gerar Plano de Negócio')

# Lógica de processamento
if submit_button:
    if not api_key:
        st.error("Por favor, insira sua API Key na barra lateral para ativar a IA.")
    else:
        try:
            # Configura a IA com a chave fornecida
            genai.configure(api_key=api_key)
           model = genai.GenerativeModel('gemini-1.5-flash')
            
            # O Prompt estratégico focado na Kiwify
            prompt = f"""
            Aja como um estrategista de vendas da Kiwify. 
            O usuário quer investir R$ {investimento}, tem habilidades em {habilidades} e busca ganhar R$ {objetivo}/mês.
            Sugira 1 ideia de negócio e infoproduto para ele vender como AFILIADO na Kiwify:
            
            1. CONCEITO: (Nome do negócio e o que é).
            2. O QUE BUSCAR NA KIWIFY: (Palavras-chave exatas para busca no Marketplace).
            3. ESTRATÉGIA DE TRÁFEGO: (Roteiro curto para atrair público sem anúncios).
            4. FRASE DE IMPACTO PARA BIO: (Copy para gerar cliques no link).
            """
            
            with st.spinner('A IA está analisando as melhores opções para você...'):
                response = model.generate_content(prompt)
                st.markdown("---")
                st.subheader("💡 Sua Oportunidade Identificada:")
                st.write(response.text)
                st.success("Dica: Use as palavras-chave acima na Kiwify para começar!")
                
        except Exception as e:
            st.error(f"Erro ao conectar com a IA. Verifique sua chave. Detalhes: {e}")
          
