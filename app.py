import streamlit as st
import pandas as pd
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re

# CONFIGURAÇÃO DO AGENTE
st.set_page_config(page_title="Agente Arbitragem Pro", page_icon="🤖", layout="wide")

def salvar_no_historico(dados):
    arquivo = 'historico_arbitragem.csv'
    df_novo = pd.DataFrame([dados])
    df_novo.to_csv(arquivo, mode='a', header=not os.path.exists(arquivo), index=False, sep=';', encoding='utf-8-sig')

def analisar_viabilidade(roi, margem):
    """Lógica do Agente para dar o veredito final"""
    if roi >= 50 and margem >= 20:
        return "💎 OPERAÇÃO OURO", "Excelente! Margem e ROI acima da média do mercado."
    elif roi >= 20 and margem >= 10:
        return "✅ VIÁVEL", "Operação saudável. Pode prosseguir com cautela."
    else:
        return "⚠️ ALTO RISCO", "Cuidado! Margem muito apertada para imprevistos ou Ads alto."

def buscar_preco_online(termo):
    """Busca simples de preço médio (simulação com scraping básico)"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    try:
        # Busca no Google Shopping (HTML simples)
        url = f"https://www.google.com/search?q={termo}+preço&tbm=shop"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Tenta encontrar padrões de preço (R$ xx,xx)
        text = soup.get_text()
        precos = re.findall(r'R\$\s*([\d\.]+,\d{2})', text)
        
        if precos:
            # Converte o primeiro preço encontrado para float
            preco_str = precos[0].replace('.', '').replace(',', '.')
            return float(preco_str)
    except Exception as e:
        st.error(f"Erro na busca: {e}")
    return 0.0

def main():
    # Inicialização de Estado da Sessão
    if 'p_compra' not in st.session_state: st.session_state.p_compra = 100.0
    if 'p_venda' not in st.session_state: st.session_state.p_venda = 200.0
    if 'nome_produto' not in st.session_state: st.session_state.nome_produto = "Scanner de Oportunidade"

    # Callbacks
    def atualizar_precos():
        termo = st.session_state.nome_produto
        if termo:
            with st.spinner(f"Buscando preços para '{termo}'..."):
                preco_encontrado = buscar_preco_online(termo)
                if preco_encontrado > 0:
                    st.session_state.p_compra = preco_encontrado
                    st.session_state.p_venda = preco_encontrado * 2.0  # Sugestão de markup 100%
                    st.toast(f"Preço encontrado: R$ {preco_encontrado:.2f}", icon="✅")
                else:
                    st.toast("Não foi possível identificar um preço claro.", icon="⚠️")

    st.markdown("<h1 style='text-align: center;'>🤖 AGENTE DE ANÁLISE: ARBITRAGEM PRO</h1>", unsafe_allow_html=True)
    
    tab_task, tab_dash = st.tabs(["🎯 Missão: Analisar Produto", "📈 Workflow de Histórico"])

    with tab_task:
        # ENTRADA DE DADOS
        with st.expander("📦 Dados do Produto", expanded=True):
            col_search, col_btn = st.columns([3, 1])
            nome = col_search.text_input("Nome da Missão / Produto", key="nome_produto")
            col_btn.write("") # Espaçamento
            col_btn.write("") 
            if col_btn.button("🔍 Pesquisar Preço", use_container_width=True):
                 atualizar_precos()

            col1, col2 = st.columns([3, 1])
            # nome já capturado acima, apenas logicamente mantendo estrutura se necessario, mas simplifiquei
            qtd = col2.number_input("Qtd", min_value=1, value=1)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<h3 style='text-align: center;'>💰 Estrutura de Custos</h3>", unsafe_allow_html=True)
            p_compra = st.number_input("Preço Compra Un. (R$)", key="p_compra")
            frete_entrada = st.number_input("Frete Entrada (Total R$)", value=0.0)
        
        with c2:
            st.markdown("<h3 style='text-align: center;'>📊 Parâmetros de Venda</h3>", unsafe_allow_html=True)
            p_venda = st.number_input("Preço Venda Un. (R$)", key="p_venda")
            taxa_plataforma = st.number_input("Taxa Plataforma (%)", value=12.0)
            ads_percent = st.number_input("Publicidade/Ads (%)", value=5.0)

        # CÁLCULOS TÉCNICOS
        investimento_total = (p_compra * qtd) + frete_entrada
        faturamento_bruto = p_venda * qtd
        
        # Impostos e Taxas (Lógica Agentic)
        imposto = faturamento_bruto * 0.06 # Simulação de 6% fixo
        comissao = faturamento_bruto * (taxa_plataforma / 100)
        marketing = faturamento_bruto * (ads_percent / 100)
        custo_fixo = 6.0 * qtd # Taxa fixa ML/Amazon
        
        total_despesas = comissao + marketing + imposto + custo_fixo
        lucro_liquido = faturamento_bruto - investimento_total - total_despesas
        roi = (lucro_liquido / investimento_total) * 100 if investimento_total > 0 else 0
        margem = (lucro_liquido / faturamento_bruto) * 100 if faturamento_bruto > 0 else 0

        st.markdown("---")
        
        # VEREDITO DO AGENTE (Onde a mágica acontece)
        veredito, conselho = analisar_viabilidade(roi, margem)
        
        st.subheader(f"🤖 Veredito do Agente: {veredito}")
        st.info(conselho)

        res1, res2, res3, res4 = st.columns(4)
        res1.metric("Lucro Líquido", f"R$ {lucro_liquido:,.2f}")
        res2.metric("ROI", f"{roi:.1f}%")
        res3.metric("Margem", f"{margem:.1f}%")
        res4.metric("Ponto de Equilíbrio", f"R$ {(investimento_total + custo_fixo) / (1 - (taxa_plataforma+ads_percent+6)/100) / qtd:,.2f}")

        if st.button("💾 REGISTRAR MISSÃO NO HISTÓRICO", type="primary", use_container_width=True):
            salvar_no_historico({
                "Data": datetime.now().strftime("%d/%m/%Y"),
                "Produto": nome,
                "Status": veredito,
                "Lucro": round(lucro_liquido, 2),
                "ROI": round(roi, 2)
            })
            st.toast("Missão registrada com sucesso!")

    with tab_dash:
        if os.path.exists('historico_arbitragem.csv'):
            df = pd.read_csv('historico_arbitragem.csv', sep=';')
            st.dataframe(df.sort_index(ascending=False), use_container_width=True)
            st.bar_chart(df.groupby('Status').size())
        else:
            st.warning("Nenhuma missão registrada ainda.")

if __name__ == "__main__":
    main()