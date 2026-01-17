import streamlit as st
import google.generativeai as genai
import os

# Configuração da página
st.set_page_config(
    page_title="Máquina de Arbitragem de Lucro - Método Campbell",
    page_icon="💰",
    layout="centered"
)

# Configuração da API Key (tenta Secrets, se não houver pede ao usuário)
api_key = None

# Tenta pegar dos Secrets primeiro
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    # Se não houver nos Secrets, verifica se já está na sessão
    if "api_key" not in st.session_state:
        st.session_state.api_key = None

# Se não tem API Key, mostra campo para o administrador configurar
if not api_key and not st.session_state.api_key:
    with st.sidebar:
        st.warning("⚙️ Configuração necessária")
        temp_key = st.text_input(
            "API Key do Google AI",
            type="password",
            help="Cole sua API Key aqui. Ela será salva apenas durante esta sessão."
        )
        if temp_key:
            st.session_state.api_key = temp_key
            st.rerun()
        else:
            st.info("💡 **Para administradores:** Configure a API Key nos Secrets do Streamlit para o app funcionar automaticamente.")
            st.stop()

# Configura a API
final_key = api_key if api_key else st.session_state.api_key
genai.configure(api_key=final_key)

# Título e descrição
st.title("💰 Máquina de Arbitragem de Lucro")
st.markdown("**Método Marcus Campbell: Encontre Micro-Nichos de Baixa Concorrência e Alta Conversão**")
st.markdown("---")

# Sidebar com explicação do método
with st.sidebar:
    st.header("🧠 O Método Campbell")
    st.markdown("""
    **O que é diferente aqui?**
    
    ❌ **NÃO fazemos:**
    - Ideias genéricas de negócio
    - Mercados saturados
    - Sugestões sem estratégia
    
    ✅ **FAZEMOS:**
    - Identificar MICRO-NICHOS específicos
    - Encontrar "Trigger Words" (palavras de busca quente)
    - Mapear ofertas de afiliado prontas
    - Bio de Instagram focada em CONVERSÃO
    
    **Resultado:** Menos concorrência, mais lucro, início rápido.
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Como funciona:")
    st.markdown("""
    1. Você informa investimento e habilidades
    2. A IA analisa micro-nichos de oportunidade
    3. Recebe um plano completo com:
       - Nicho específico de baixa concorrência
       - Palavras-chave que convertem
       - Ofertas de afiliado prontas (Kiwify/Hotmart)
       - Bio Instagram focada em CTA
    """)

# Função para gerar análise estilo Marcus Campbell
def gerar_estrategia_campbell(investimento, habilidades, meta_ganho):
    try:
        # Usa o modelo que funcionou
        model = genai.GenerativeModel('models/gemini-2.5-flash')
        
        # Prompt estilo Marcus Campbell
        prompt = f"""Você é Marcus Campbell, especialista em arbitragem de lucro e marketing de afiliados.

Sua missão é encontrar MICRO-NICHOS de BAIXA CONCORRÊNCIA e ALTA CONVERSÃO.

📊 DADOS DO CLIENTE:
- Investimento disponível: R$ {investimento}
- Habilidades: {habilidades}
- Meta de ganho mensal: R$ {meta_ganho}

🎯 ANÁLISE OBRIGATÓRIA (Método Campbell):

1. IDENTIFICAÇÃO DO MICRO-NICHO
   - NÃO sugira mercados genéricos (ex: "venda de bolos")
   - SUGIRA nichos ultra-específicos (ex: "bolos sem glúten para festas corporativas")
   - Explique por que esse micro-nicho tem BAIXA concorrência
   - Identifique a DOR específica desse público

2. TRIGGER WORDS (Palavras de Busca Quente)
   - Liste 5-7 termos EXATOS que esse público busca no Google quando quer COMPRAR
   - Exemplo: "onde comprar", "melhor curso de", "como fazer X rápido"
   - Mostre o volume de busca estimado (baixo/médio/alto)
   - Indique a intenção de compra (qual palavra mostra que a pessoa vai pagar)

3. OFERTAS DE AFILIADO PRONTAS
   - Identifique 3-5 produtos digitais da KIWIFY ou HOTMART que você pode promover NESTE nicho
   - Para cada produto, indique:
     * Nome aproximado do produto (ex: "Curso de Confeitaria Low Carb")
     * Comissão estimada (ex: 50% de R$ 197 = R$ 98,50 por venda)
     * Por que esse produto resolve a DOR identificada
   - Se não existir produto perfeito, sugira a criação de um mini-produto digital simples

4. ESTRATÉGIA DE TRÁFEGO GRATUITO (Primeiros 30 dias)
   - Onde esse público específico está? (grupos, fóruns, Instagram, TikTok)
   - Como capturar atenção SEM pagar anúncios
   - Qual conteúdo criar para atrair esse nicho
   - Como inserir o link de afiliado de forma natural

5. BIO DO INSTAGRAM FOCADA EM CONVERSÃO
   - Crie uma bio de 150 caracteres MÁXIMO
   - FOCO TOTAL em despertar curiosidade e gerar clique no link
   - Deve conter:
     * Problema que você resolve (dor específica)
     * Promessa clara (resultado específico)
     * CTA direto ("Link na bio com X grátis")
   - Use emojis estratégicos
   - NÃO fale de você, fale do RESULTADO para o cliente

6. PLANO DE 7 DIAS (Ação Imediata)
   - Dia 1: O que fazer HOJE para começar
   - Dia 2-3: Criação de conteúdo/oferta
   - Dia 4-5: Onde postar e como engajar
   - Dia 6-7: Primeiras vendas (meta realista)
   - Cada dia deve ter 2-3 tarefas CONCRETAS

7. CÁLCULO DE VIABILIDADE
   - Quantas vendas por mês são necessárias para atingir R$ {meta_ganho}?
   - Qual a taxa de conversão realista nesse nicho? (ex: 2%)
   - Quantos seguidores/visitantes você precisa?
   - Esse objetivo é realista com R$ {investimento} de investimento?

8. ARMADILHAS A EVITAR (Método Campbell)
   - 3 erros FATAIS que iniciantes cometem nesse nicho
   - Como NÃO perder tempo com estratégias que não funcionam
   - Sinais de que você está no caminho errado

IMPORTANTE:
- Seja ULTRA-ESPECÍFICO. Nada genérico.
- Todo conselho deve ser ACIONÁVEL (com passos claros).
- Foque em LUCRO RÁPIDO, não em construir marca a longo prazo.
- Use dados e números sempre que possível.
- Se o nicho for muito competitivo, sugira um micro-recorte.

Formato: Use markdown com títulos, bullet points e emojis para facilitar a leitura."""

        # Gera o conteúdo
        with st.spinner("🧠 Analisando micro-nichos e estratégias de arbitragem..."):
            response = model.generate_content(prompt)
        
        return response.text
        
    except Exception as e:
        return f"""❌ **Erro ao gerar estratégia**

**Detalhes:** {str(e)}

**Solução:** Tente novamente em alguns segundos. Se o erro persistir, entre em contato com o suporte."""

# Formulário principal
with st.form("formulario_campbell"):
    st.subheader("📝 Análise de Oportunidade")
    
    col1, col2 = st.columns(2)
    
    with col1:
        investimento = st.number_input(
            "💰 Investimento Disponível (R$)",
            min_value=0,
            max_value=100000,
            value=500,
            step=100,
            help="Quanto você pode investir para começar"
        )
    
    with col2:
        meta_ganho = st.number_input(
            "🎯 Meta de Ganho Mensal (R$)",
            min_value=500,
            max_value=100000,
            value=3000,
            step=500,
            help="Quanto você quer ganhar por mês"
        )
    
    habilidades = st.text_area(
        "🎯 Suas Habilidades e Conhecimentos",
        placeholder="Ex: Conheço bem de nutrição, tenho experiência com redes sociais, sei editar vídeos básicos...",
        height=100,
        help="Liste o que você sabe fazer ou tem facilidade para aprender"
    )
    
    submitted = st.form_submit_button("🚀 Encontrar Meu Micro-Nicho Lucrativo", use_container_width=True)

# Processar quando o formulário for enviado
if submitted:
    if not habilidades:
        st.error("⚠️ Por favor, descreva suas habilidades para encontrarmos o melhor micro-nicho.")
    else:
        resultado = gerar_estrategia_campbell(investimento, habilidades, meta_ganho)
        
        st.markdown("---")
        st.markdown("## 💎 Sua Estratégia de Arbitragem - Método Campbell")
        st.markdown(resultado)
        
        # Botões de ação
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="💾 Baixar Estratégia Completa",
                data=resultado,
                file_name="estrategia_campbell.txt",
                mime="text/plain",
                use_container_width=True
            )
        with col2:
            st.button("🔄 Gerar Nova Análise", use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.9em;'>
    💰 Máquina de Arbitragem de Lucro - Método Marcus Campbell<br>
    <small>Micro-Nichos • Trigger Words • Ofertas de Afiliado • Conversão</small>
    </div>
    """,
    unsafe_allow_html=True
)
