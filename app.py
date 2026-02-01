import streamlit as st
import pandas as pd
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re

# CONFIGURAÇÃO DO AGENTE
st.set_page_config(page_title="Agente Arbitragem Pro", page_icon="🤖", layout="wide")

# CSS PERSONALIZADO
st.markdown("""
<style>
    .main-header {text-align: center; color: #4CAF50; font-size: 3em; font-weight: bold; padding: 1em 0;}
    .sub-header {text-align: center; color: #555; font-size: 1.5em; margin-bottom: 1em;}
    .stButton>button {width: 100%; border-radius: 5px; height: 3em;}
    .metric-card {background-color: #f8f9fa; padding: 1em; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);}
    
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: #555;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #ddd;
        z-index: 100;
    }
    .content-spacer { height: 50px; }
</style>
""", unsafe_allow_html=True)

def salvar_no_historico(dados):
    arquivo = 'historico_arbitragem.csv'
    df_novo = pd.DataFrame([dados])
    df_novo.to_csv(arquivo, mode='a', header=not os.path.exists(arquivo), index=False, sep=';', encoding='utf-8-sig')

def analisar_viabilidade(roi, margem):
    if roi >= 50 and margem >= 20:
        return "💎 OPERAÇÃO OURO", "Excelente! Margem e ROI acima da média do mercado."
    elif roi >= 20 and margem >= 10:
        return "✅ VIÁVEL", "Operação saudável. Pode prosseguir com cautela."
    else:
        return "⚠️ ALTO RISCO", "Margem apertada. Cuidado com custos variáveis."

def obter_cotacao(moeda_origem):
    """Obtém cotação do AwesomeAPI (USD ou EUR para BRL)"""
    try:
        pair = f"{moeda_origem}-BRL"
        response = requests.get(f"https://economia.awesomeapi.com.br/last/{pair}")
        dados = response.json()
        key = pair.replace('-', '')
        return float(dados[key]['bid'])
    except:
        return 5.0 if moeda_origem == "USD" else 5.5

def buscar_dados_web(termo, contexto):
    """
    Busca contextualizada:
    - brasil: Busca genérica de preços br
    - clickbank: Busca USD
    - digistore: Busca EUR
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    cotacao = 1.0
    queries = []
    
    if contexto == 'brasil':
        queries = [f'site:mercadolivre.com.br "{termo}"', f'"{termo}" preço']
        moeda_regex = r'R\$\s*(\d+[.,]?\d*)'
    elif contexto == 'clickbank':
        cotacao = obter_cotacao('USD')
        queries = [f'site:clickbank.com "{termo}" price', f'"{termo}" review price']
        moeda_regex = r'\$\s?(\d+\.?\d*)'
    elif contexto == 'digistore':
        cotacao = obter_cotacao('EUR')
        queries = [f'site:digistore24.com "{termo}" price', f'"{termo}" kosten']
        moeda_regex = r'€\s?(\d+[.,]?\d*)'
    
    try:
        url = f"https://www.google.com/search?q={queries[0]}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        
        precos = re.findall(moeda_regex, text)
        valores = []
        for p in precos:
            try:
                # Limpeza simples
                p_clean = p.replace(',', '.') if contexto != 'brasil' else p.replace('.', '').replace(',', '.')
                val = float(p_clean)
                if 5 < val < 5000: valores.append(val)
            except: pass
            
        if valores:
            media = sum(valores) / len(valores)
            media_brl = media * cotacao
            return media_brl, f"Média encontrada: {media:.2f} ({cotacao:.2f} BRL/un)"
            
    except Exception as e:
        return 0.0, f"Erro: {str(e)}"
    
    return 0.0, "Preço não encontrado."

def render_aba(contexto, label_tab):
    st.markdown(f"<div class='sub-header'>{label_tab}</div>", unsafe_allow_html=True)
    
    # Session State
    k_nome = f"{contexto}_nome"
    k_compra = f"{contexto}_compra"
    k_venda = f"{contexto}_venda"
    k_qtd = f"{contexto}_qtd"
    
    if k_compra not in st.session_state: st.session_state[k_compra] = 100.0
    if k_venda not in st.session_state: st.session_state[k_venda] = 200.0
    
    # Inputs
    col1, col2 = st.columns([3, 1])
    nome = col1.text_input("Produto / Oferta", key=k_nome)
    qtd = col2.number_input("Qtd Volume", min_value=1, value=1, key=k_qtd)
    
    if st.button(f"🔍 Pesquisar Dados ({label_tab})", key=f"btn_{contexto}"):
        if nome:
            with st.spinner("Varrendo a web..."):
                valor, msg = buscar_dados_web(nome, contexto)
                if valor > 0:
                    st.session_state[k_venda] = valor # Assume que o valor encontrado é o preço de venda/mercado
                    if contexto != 'brasil':
                        st.session_state[k_venda] = valor * 0.60 # Estima 60% comissão para afiliados
                    st.toast(f"Atualizado: {msg}", icon="✅")
                else:
                    st.toast("Nada encontrado.", icon="⚠️")

    c1, c2 = st.columns(2)
    with c1:
        st.info("📉 Seus Custos")
        p_compra = st.number_input("Custo Unitário / CPA (R$)", key=k_compra)
        frete = st.number_input("Outros Custos / Ads (R$)", value=0.0, key=f"{contexto}_frete")
        
    with c2:
        st.info("📈 Sua Receita")
        p_venda = st.number_input("Venda Unitária / Comissão (R$)", key=k_venda)
        taxa = st.number_input("Taxas (%)", value=10.0, key=f"{contexto}_taxa")
        
    # Engine de Cálculo
    total_receita = p_venda * qtd
    impostos_taxas = total_receita * (taxa / 100)
    total_custos = (p_compra * qtd) + frete + impostos_taxas
    
    lucro = total_receita - total_custos
    roi = (lucro / total_custos * 100) if total_custos > 0 else 0
    margem = (lucro / total_receita * 100) if total_receita > 0 else 0
    
    st.divider()
    
    m1, m2, m3 = st.columns(3)
    m1.metric("💰 Lucro Líquido", f"R$ {lucro:,.2f}")
    m2.metric("🚀 ROI", f"{roi:.1f}%")
    m3.metric("📊 Margem", f"{margem:.1f}%")
    
    veredito, descricao = analisar_viabilidade(roi, margem)
    st.success(f"{veredito} - {descricao}")
    
    
    
    # --- MODULE: PROFIT PLANNING (CLICKBANK ONLY) ---
    if contexto == 'clickbank':
        with st.expander("📊 Planejamento de Lucro", expanded=True):
            pc1, pc2 = st.columns(2)
            meta_inv = pc1.number_input("Investimento em Tráfego (R$)", value=1000.0, step=100.0, key=f"plan_inv_{contexto}")
            meta_lucro = pc2.number_input("Meta de Lucro Mensal (R$)", value=5000.0, step=500.0, key=f"plan_meta_{contexto}")
            
            # Smart Feedback
            comissao_atual = st.session_state.get(k_venda, 0.0)
            nome_atual = st.session_state.get(k_nome, "Produto")
            
            if comissao_atual > 0:
                vendas_necessarias = (meta_lucro + meta_inv) / comissao_atual
                st.info(f"💡 Com base na sua meta de **R$ {meta_lucro:,.2f}**, você precisaria de aproximadamente **{int(vendas_necessarias)+1} vendas** do produto **{nome_atual}** (Comissão: R$ {comissao_atual:.2f}).")
            else:
                st.warning("⚠️ Selecione um produto no **Radar de Tendências** abaixo para calcular sua meta.")

    # --- INTELLIGENCE MODULE: TRENDING PRODUCTS ---
    if contexto != 'brasil':
        with st.expander("🔥 Top Trending Products (Live Search)", expanded=False):
            st.caption("Intelligence Module: Rastreando produtos de alta gravidade em tempo real.")
            
            if st.button(f"Rastrear Tendências Agora ({label_tab})", key=f"btn_trend_{contexto}"):
                trends = []
                if contexto == 'clickbank':
                    trends = ["Alpilean", "Live Pure", "ProDentim"]
                elif contexto == 'digistore':
                    trends = ["Metabo Flex", "Tube Mastery", "Keto Meal Plan"]
                
                cols = st.columns(3)
                for i, prod in enumerate(trends):
                    with cols[i]:
                        with st.container(border=True): # Card Style
                            st.markdown(f"### {prod}")
                            with st.spinner(f"Analisando..."):
                                val, msg = buscar_dados_web(prod, contexto)
                                
                                # Score Calculation (Simulated ROI check)
                                score_color = "red"
                                score_text = "BAIXO"
                                est_comm = 0.0
                                
                                if val > 0:
                                    # Estimate simple ROI: (Commision - Cost) / Cost
                                    # Cost assumed ~100 BRL (Ads) for calculation
                                    est_comm = val * 0.60
                                    est_cost = 100.0 # Custo fixo estimado de tráfego
                                    est_roi = ((est_comm - est_cost) / est_cost) * 100 if est_comm > est_cost else 0
                                    
                                    if est_roi > 50: 
                                        score_color = "green" 
                                        score_text = "ALTO"
                                    elif est_roi >= 20: 
                                        score_color = "orange"
                                        score_text = "MÉDIO"
                                
                                if val > 0:
                                    st.metric("Comissão Est.", f"R$ {est_comm:.2f}")
                                    st.markdown(f"**Viabilidade:** :{score_color}[{score_text}]")
                                    st.progress(min(int(est_roi), 100) if est_roi > 0 else 0)
                                    
                                    if st.button(f"🚀 Carregar Dados", key=f"load_{prod}_{contexto}", use_container_width=True):
                                        st.session_state[k_nome] = prod
                                        st.session_state[k_venda] = est_comm
                                        st.rerun()
                                else:
                                    st.warning(f"Dados indisponíveis no momento.")

    if st.button("💾 Salvar Análise", key=f"save_{contexto}"):
        salvar_no_historico({
            "Data": datetime.now().strftime("%Y-%m-%d"),
            "Plataforma": label_tab,
            "Produto": nome,
            "Lucro": float(f"{lucro:.2f}"),
            "ROI": float(f"{roi:.2f}")
        })
        st.balloons()

def main():
    # --- UI: HEADER & LOGO ---
    col_centered = st.columns([1, 8, 1])
    with col_centered[1]:
        try:
            if os.path.exists("logo.png"):
                st.image("logo.png", width=100) # Centrado (via column trick or clean CSS, Streamlit handles images as block)
            else:
                st.markdown("<h1 style='text-align: center;'>🚀</h1>", unsafe_allow_html=True)
        except: pass
        
        st.markdown("<h1 class='main-header' style='text-align: center;'>Agente Arbitragem Pro</h1>", unsafe_allow_html=True)
    
    # --- UI: SIDEBAR ---
    with st.sidebar:
        try:
            if os.path.exists("logo.png"):
                st.image("logo.png", use_column_width=True)
        except: pass
        
        st.header("🆘 Suporte e Dúvidas")
        st.markdown("Precisa de ajuda para lucrar em Dólar ou Euro?")
        st.link_button("💬 Falar com Suporte (WhatsApp)", "https://wa.me/5583991183123?text=Olá%20Sérgio!%20Vi%20sua%20Calculadora%20de%20Arbitragem%20e%20quero%20saber%20mais.") 
        st.divider()
        st.info("💡 **Dica:** Use as abas para alternar entre mercados.")

    # --- TABS ---
    tabs = st.tabs(["🇧🇷 Brasil (Marketplaces)", "🇺🇸 ClickBank (Dólar)", "🇪🇺 Digistore24 (Euro)", "📚 Histórico"])
    
    with tabs[0]:
        render_aba("brasil", "Brasil - ML/Shopee/Amazon")
    with tabs[1]:
        render_aba("clickbank", "ClickBank Affiliate")
    with tabs[2]:
        render_aba("digistore", "Digistore24 Affiliate")
    with tabs[3]:
        st.markdown("### Histórico de Operações")
        if os.path.exists('historico_arbitragem.csv'):
            df = pd.read_csv('historico_arbitragem.csv', sep=';')
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("Nenhum dado salvo.")
            
    # --- UI: FOOTER ---
    st.markdown("""
    <div class='content-spacer'></div>
    <div class='footer'>
        <p>© 2026 Arbitrage Pro - Desenvolvido por Sérgio | Todos os direitos reservados.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()