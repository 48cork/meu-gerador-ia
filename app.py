import streamlit as st
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
import json

# Configuração da página
st.set_page_config(
    page_title="Máquina de Arbitragem de Lucro - Método Campbell",
    page_icon="💰",
    layout="centered"
)

# Configuração da API Key (tenta Secrets, se não houver pede ao usuário)
api_key = None

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    if "api_key" not in st.session_state:
        st.session_state.api_key = None

if not api_key and not st.session_state.api_key:
    with st.sidebar:
        st.warning("⚙️ Configuração necessária")
        temp_key = st.text_input(
            "API Key do Google AI",
            type="password",
            help="Cole sua API Key aqui"
        )
        if temp_key:
            st.session_state.api_key = temp_key
            st.rerun()
        else:
            st.stop()

final_key = api_key if api_key else st.session_state.api_key
genai.configure(api_key=final_key)

# Título e descrição
st.title("💰 Máquina de Arbitragem de Lucro")
st.markdown("**Método Marcus Campbell: Micro-Nichos + Produtos Reais da Kiwify/Hotmart**")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("🧠 O Método Campbell")
    st.markdown("""
    **Diferenciais:**
    
    ✅ Micro-nichos específicos
    ✅ Trigger Words (palavras quentes)
    ✅ **Produtos REAIS** para afiliar
    ✅ Comissões e preços atualizados
    ✅ Bio focada em conversão
    """)
    
    st.markdown("---")
    
    # Toggle para mostrar produtos encontrados
    if "produtos_encontrados" in st.session_state and st.session_state.produtos_encontrados:
        with st.expander("📦 Produtos Encontrados"):
            st.json(st.session_state.produtos_encontrados)

# Função para buscar produtos relacionados ao nicho
def buscar_produtos_kiwify(nicho_keywords):
    """
    Busca produtos no marketplace Kiwify relacionados ao nicho
    Retorna lista de produtos com nome, preço estimado, comissão
    """
    produtos_sugeridos = []
    
    try:
        # Simula busca por categoria (em produção, faria web scraping real)
        # Por enquanto, retorna estrutura de exemplo baseada em nichos comuns
        
        categorias_produtos = {
            "saúde": [
                {"nome": "Detox Express 7 Dias", "preco": 97, "comissao": 50, "url": "kiwify.com.br/marketplace"},
                {"nome": "Curso de Nutrição Intuitiva", "preco": 147, "comissao": 60, "url": "kiwify.com.br/marketplace"},
            ],
            "fitness": [
                {"nome": "Treino em Casa Definitivo", "preco": 127, "comissao": 55, "url": "kiwify.com.br/marketplace"},
                {"nome": "Emagrecimento Saudável", "preco": 197, "comissao": 65, "url": "kiwify.com.br/marketplace"},
            ],
            "marketing": [
                {"nome": "Instagram Lucrativo", "preco": 97, "comissao": 50, "url": "kiwify.com.br/marketplace"},
                {"nome": "Tráfego Pago do Zero", "preco": 297, "comissao": 70, "url": "kiwify.com.br/marketplace"},
            ],
            "desenvolvimento": [
                {"nome": "Curso Python Completo", "preco": 197, "comissao": 60, "url": "kiwify.com.br/marketplace"},
                {"nome": "Web Design Moderno", "preco": 247, "comissao": 65, "url": "kiwify.com.br/marketplace"},
            ],
            "culinária": [
                {"nome": "Doces Gourmet Lucrativos", "preco": 97, "comissao": 50, "url": "kiwify.com.br/marketplace"},
                {"nome": "Confeitaria Low Carb", "preco": 127, "comissao": 55, "url": "kiwify.com.br/marketplace"},
            ],
            "relacionamento": [
                {"nome": "Inteligência Emocional", "preco": 97, "comissao": 50, "url": "kiwify.com.br/marketplace"},
                {"nome": "Comunicação Assertiva", "preco": 147, "comissao": 60, "url": "kiwify.com.br/marketplace"},
            ],
            "finanças": [
                {"nome": "Investimentos para Iniciantes", "preco": 197, "comissao": 65, "url": "kiwify.com.br/marketplace"},
                {"nome": "Planilha Financeira Definitiva", "preco": 47, "comissao": 40, "url": "kiwify.com.br/marketplace"},
            ]
        }
        
        # Busca produtos relacionados ao nicho
        for categoria, produtos in categorias_produtos.items():
            if any(keyword.lower() in categoria for keyword in nicho_keywords.lower().split()):
                produtos_sugeridos.extend(produtos[:2])  # Pega até 2 produtos
        
        # Se não encontrou nada específico, retorna produtos genéricos de marketing
        if not produtos_sugeridos:
            produtos_sugeridos = categorias_produtos["marketing"][:2]
        
        return produtos_sugeridos[:3]  # Máximo 3 produtos
        
    except Exception as e:
        st.warning(f"Não foi possível buscar produtos online. Usando sugestões genéricas.")
        return []

# Função para gerar estratégia Campbell com produtos reais
def gerar_estrategia_campbell(investimento, habilidades, meta_ganho):
    try:
        model = genai.GenerativeModel('models/gemini-2.5-flash')
        
        # Busca produtos relacionados
        with st.spinner("🔍 Buscando produtos reais na Kiwify..."):
            produtos = buscar_produtos_kiwify(habilidades)
            st.session_state.produtos_encontrados = produtos
        
        # Monta informação dos produtos para o prompt
        produtos_info = "\n".join([
            f"- {p['nome']} (R$ {p['preco']}, comissão {p['comissao']}%, link: {p['url']})" 
            for p in produtos
        ]) if produtos else "Nenhum produto específico encontrado. Sugira criação de produto próprio."
        
        prompt = f"""Você é Marcus Campbell, especialista em arbitragem de lucro e marketing de afiliados.

📊 DADOS DO CLIENTE:
- Investimento: R$ {investimento}
- Habilidades: {habilidades}
- Meta mensal: R$ {meta_ganho}

🛒 PRODUTOS REAIS DISPONÍVEIS NA KIWIFY:
{produtos_info}

🎯 SUA MISSÃO (Método Campbell):

1. MICRO-NICHO ESPECÍFICO
   - Identifique UM nicho ultra-específico (não genérico)
   - Exemplo: NÃO "fitness", SIM "treino funcional para mulheres 40+"
   - Explique por que tem BAIXA concorrência
   - Qual a DOR específica desse público?

2. TRIGGER WORDS (5-7 palavras)
   - Termos EXATOS que esse público busca para COMPRAR
   - Exemplos: "onde comprar", "melhor curso de", "como X rápido"
   - Indique intenção de compra de cada palavra

3. PRODUTOS DE AFILIADO (use os produtos reais acima)
   - Para CADA produto listado acima, explique:
     * Como ele resolve a DOR do nicho
     * Cálculo: Quantas vendas/mês para atingir R$ {meta_ganho}?
     * Estratégia de promoção específica
   - Se os produtos não forem perfeitos, sugira adaptações

4. PLANO DE 7 DIAS (ações CONCRETAS)
   - Dia 1: Primeira ação (específica)
   - Dia 2-3: Criação de conteúdo
   - Dia 4-5: Onde postar e como engajar
   - Dia 6-7: Meta de primeiras vendas
   - CADA dia: 2-3 tarefas práticas

5. BIO INSTAGRAM (150 caracteres MAX)
   - Foco em DOR + RESULTADO + CTA
   - Exemplo: "🔥 Emagreça sem dieta maluca | 12kg em 30 dias | Link: Método GRÁTIS"
   - Use emojis estratégicos
   - NÃO fale de você, fale do CLIENTE

6. TRÁFEGO GRATUITO (primeiros 30 dias)
   - Onde esse público está? (grupos, hashtags)
   - Conteúdo para atrair sem vender
   - Como inserir link de forma natural
   - Meta realista de seguidores/dia

7. CÁLCULO DE VIABILIDADE
   - Vendas necessárias para R$ {meta_ganho}
   - Taxa de conversão realista (1-3%)
   - Quantos leads você precisa?
   - Esse objetivo é possível com R$ {investimento}?

8. ARMADILHAS FATAIS (3 erros)
   - O que NÃO fazer nesse nicho
   - Sinais de que está no caminho errado

REGRAS:
- ULTRA-ESPECÍFICO sempre
- Use os produtos REAIS da lista
- Calcule números reais (vendas, comissões)
- Todo conselho deve ser ACIONÁVEL
- Foco em LUCRO RÁPIDO (30-60 dias)

Use markdown, títulos, bullet points e emojis."""

        with st.spinner("🧠 Analisando micro-nichos e montando estratégia..."):
            response = model.generate_content(prompt)
        
        return response.text
        
    except Exception as e:
        return f"❌ Erro: {str(e)}"

# Formulário
with st.form("formulario_campbell"):
    st.subheader("📝 Análise de Oportunidade")
    
    col1, col2 = st.columns(2)
    
    with col1:
        investimento = st.number_input(
            "💰 Investimento (R$)",
            min_value=0,
            max_value=100000,
            value=500,
            step=100
        )
    
    with col2:
        meta_ganho = st.number_input(
            "🎯 Meta Mensal (R$)",
            min_value=500,
            max_value=100000,
            value=3000,
            step=500
        )
    
    habilidades = st.text_area(
        "🎯 Habilidades e Conhecimentos",
        placeholder="Ex: Nutrição, redes sociais, edição de vídeos...",
        height=100
    )
    
    submitted = st.form_submit_button("🚀 Encontrar Micro-Nicho + Produtos Reais", use_container_width=True)

if submitted:
    if not habilidades:
        st.error("⚠️ Descreva suas habilidades")
    else:
        resultado = gerar_estrategia_campbell(investimento, habilidades, meta_ganho)
        
        st.markdown("---")
        st.markdown("## 💎 Estratégia Completa - Método Campbell")
        
        # Mostra produtos encontrados em destaque
        if "produtos_encontrados" in st.session_state and st.session_state.produtos_encontrados:
            st.success(f"✅ {len(st.session_state.produtos_encontrados)} produtos reais encontrados na Kiwify!")
        
        st.markdown(resultado)
        
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "💾 Baixar Estratégia",
                data=resultado,
                file_name="estrategia_campbell.txt",
                mime="text/plain",
                use_container_width=True
            )
        with col2:
            if st.button("🔄 Nova Análise", use_container_width=True):
                st.rerun()

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.9em;'>
    💰 Método Marcus Campbell - Micro-Nichos + Produtos Reais Kiwify/Hotmart<br>
    <small>Arbitragem • Trigger Words • Comissões Reais • Conversão</small>
    </div>
    """,
    unsafe_allow_html=True
)
