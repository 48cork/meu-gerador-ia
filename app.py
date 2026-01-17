import streamlit as st
import google.generativeai as genai

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
    
    # Botão para listar modelos disponíveis
    if api_key:
        if st.button("🔍 Descobrir Modelos Disponíveis"):
            try:
                genai.configure(api_key=api_key)
                st.write("**Modelos disponíveis para sua API Key:**")
                modelos = genai.list_models()
                modelos_texto = []
                for m in modelos:
                    if 'generateContent' in m.supported_generation_methods:
                        modelos_texto.append(f"✅ {m.name}")
                        st.success(f"✅ {m.name}")
                
                if not modelos_texto:
                    st.error("❌ Nenhum modelo disponível para generateContent")
                    
            except Exception as e:
                st.error(f"Erro ao listar modelos: {str(e)}")
    
    st.markdown("---")
    st.markdown("### 📚 Como usar:")
    st.markdown("""
    1. Insira sua API Key do Google AI
    2. Clique em "Descobrir Modelos" para ver quais estão disponíveis
    3. Preencha o formulário abaixo
    4. Clique em 'Gerar Plano de Negócio'
    """)

# Função para gerar plano de negócio
def gerar_plano_negocio(investimento, habilidades, meta_ganho, api_key):
    try:
        # Configura a API Key
        genai.configure(api_key=api_key)
        
        # Lista TODOS os modelos disponíveis e tenta usar o primeiro que suporta generateContent
        st.info("🔄 Procurando modelo disponível...")
        
        modelos_disponiveis = genai.list_models()
        model = None
        modelo_usado = None
        
        for m in modelos_disponiveis:
            if 'generateContent' in m.supported_generation_methods:
                try:
                    model = genai.GenerativeModel(m.name)
                    modelo_usado = m.name
                    st.info(f"🎯 Usando modelo: {m.name}")
                    break
                except:
                    continue
        
        if not model:
            return """❌ **Nenhum modelo disponível encontrado**

Sua API Key não tem acesso a modelos que suportam geração de conteúdo.

**Soluções:**

1. **Crie uma NOVA API Key:**
   - Acesse: https://aistudio.google.com/app/apikey
   - Delete a chave atual
   - Crie uma nova chave
   - Cole aqui e teste novamente

2. **Verifique sua região:**
   - Alguns países têm restrições
   - Tente usar uma VPN conectada aos EUA

3. **Teste no Google AI Studio:**
   - Acesse: https://aistudio.google.com/
   - Tente gerar texto diretamente
   - Se funcionar lá, o problema pode estar na nossa integração

4. **Verifique sua conta Google:**
   - Algumas contas novas têm limitações temporárias
   - Aguarde 24h e tente novamente"""

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

        # Gera o conteúdo
        response = model.generate_content(prompt)
        
        st.success(f"✅ Plano gerado com sucesso usando {modelo_usado}!")
        return response.text
        
    except Exception as e:
        erro_msg = str(e)
        
        return f"""❌ **Erro ao gerar o plano de negócio**

**Detalhes técnicos:** {erro_msg}

**Próximos passos:**

1. Clique no botão "🔍 Descobrir Modelos Disponíveis" na barra lateral
2. Veja quais modelos aparecem como disponíveis
3. Me envie essa lista para eu ajustar o código
4. Se nenhum modelo aparecer, crie uma nova API Key"""

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
            
            # Botão para copiar o resultado (só aparece se não for mensagem de erro)
            if not resultado.startswith("❌"):
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
    Criado com ❤️ usando Streamlit e Google Gemini AI<br>
    <small>💡 Dica: Clique em "Descobrir Modelos Disponíveis" para diagnosticar problemas</small>
    </div>
    """,
    unsafe_allow_html=True
)
