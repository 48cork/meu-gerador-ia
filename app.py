import streamlit as st
import requests
import json

# Configuração da página
st.set_page_config(
    page_title="Gerador de Ideias de Negócios com IA",
    page_icon="💡",
    layout="centered"
)

# Título e descrição
st.title("💡 Gerador de Ideias de Negócios")
st.markdown("**Transforme suas habilidades em um negócio lucrativo com ajuda da Inteligência Artificial**")
st.markdown("---")

# Sidebar para API Key
with st.sidebar:
    st.header("🔑 Configuração")
    api_key = st.text_input(
        "Google AI API Key",
        type="password",
        help="Cole aqui sua API Key do Google AI Studio (https://aistudio.google.com/app/apikey)"
    )
    
    st.markdown("---")
    st.markdown("### 📚 Como usar:")
    st.markdown("""
    1. Insira sua API Key do Google AI
    2. Preencha o formulário
    3. Clique em 'Gerar Plano de Negócio'
    4. Receba um plano completo com:
       - Ideia de negócio personalizada
       - Estratégia de vendas na Kiwify
       - Bio otimizada para Instagram
    """)

# Função para chamar a API do Google Gemini
def gerar_plano_negocio(investimento, habilidades, meta_ganho, api_key):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    prompt = f"""Você é um consultor de negócios especializado em ajudar pessoas a empreenderem online.

Com base nas informações abaixo, crie um plano de negócio completo e prático:

💰 Investimento disponível: R$ {investimento}
🎯 Habilidades: {habilidades}
📊 Meta de ganho mensal: R$ {meta_ganho}

Por favor, forneça:

1. IDEIA DE NEGÓCIO
   - Qual negócio digital é ideal para esse perfil?
   - Por que essa ideia faz sentido com essas habilidades?
   - Qual o potencial de ganho realista nos primeiros 3 meses?

2. PLANO DE AÇÃO (passo a passo)
   - O que fazer na primeira semana
   - Como criar o produto/serviço
   - Onde encontrar os primeiros clientes

3. COMO VENDER NA KIWIFY
   - Passo a passo para criar uma conta
   - Como cadastrar o produto
   - Configuração de pagamento e checkout
   - Dicas para aumentar a conversão

4. BIO DO INSTAGRAM (pronta para copiar e colar)
   - Crie uma bio profissional e atraente
   - Deve comunicar autoridade e gerar interesse
   - Incluir call-to-action

5. PRIMEIROS PASSOS PRÁTICOS
   - 3 ações concretas para começar hoje
   - Recursos gratuitos que podem ajudar
   - Erros comuns a evitar

Seja específico, prático e motivador. Use exemplos reais quando possível."""

    headers = {"Content-Type": "application/json"}
    
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 2048
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if "candidates" in result and len(result["candidates"]) > 0:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "Erro: Resposta da API não contém o formato esperado."
            
    except requests.exceptions.RequestException as e:
        return f"Erro na conexão com a API: {str(e)}"
    except Exception as e:
        return f"Erro inesperado: {str(e)}"

# Formulário principal
with st.form("formulario_negocio"):
    st.subheader("📝 Preencha suas informações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        investimento = st.number_input(
            "💰 Quanto você pode investir? (R$)",
            min_value=0,
            max_value=100000,
            value=500,
            step=100,
            help="Valor em reais que você tem disponível para começar"
        )
    
    with col2:
        meta_ganho = st.number_input(
            "🎯 Meta de ganho mensal (R$)",
            min_value=500,
            max_value=100000,
            value=3000,
            step=500,
            help="Quanto você deseja ganhar por mês?"
        )
    
    habilidades = st.text_area(
        "🎯 Quais são suas principais habilidades?",
        placeholder="Ex: Design gráfico, edição de vídeos, escrita, marketing digital, programação, fotografia...",
        height=100,
        help="Liste suas habilidades, experiências e conhecimentos"
    )
    
    submitted = st.form_submit_button("🚀 Gerar Plano de Negócio", use_container_width=True)

# Processar quando o formulário for enviado
if submitted:
    if not api_key:
        st.error("⚠️ Por favor, insira sua API Key do Google AI na barra lateral.")
    elif not habilidades:
        st.error("⚠️ Por favor, descreva suas habilidades.")
    else:
        with st.spinner("🤖 A IA está criando seu plano personalizado... Isso pode levar alguns segundos."):
            resultado = gerar_plano_negocio(investimento, habilidades, meta_ganho, api_key)
            
            st.markdown("---")
            st.markdown("## 📋 Seu Plano de Negócio Personalizado")
            st.markdown(resultado)
            
            # Botão para copiar o resultado
            st.download_button(
                label="💾 Baixar Plano Completo",
                data=resultado,
                file_name="plano_de_negocio.txt",
                mime="text/plain"
            )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.9em;'>
    Criado com ❤️ usando Streamlit e Google Gemini AI
    </div>
    """,
    unsafe_allow_html=True
)
