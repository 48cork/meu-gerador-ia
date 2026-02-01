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
def obter_cotacao_dolar():
    try:
        response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        dados = response.json()
        return float(dados['USDBRL']['bid'])
    except:
        return 5.0 # Fallback conservador

def buscar_dados_afiliado(termo):
    """
    Busca dados de produtos ClickBank/Digistore24 e converte para BRL
    Retorna: (preco_brl, comissao_estimada_brl)
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    dolar = obter_cotacao_dolar()
    
    # Termos de busca focados em plataformas de afiliados
    queries = [
        f'site:clickbank.com "{termo}" price',
        f'site:digistore24.com "{termo}" price',
        f'"{termo}" affiliate commission rate',
        f'"{termo}" review price'
    ]
    
    preco_encontrado_usd = 0.0
    
    try:
        # Tenta a primeira query principal
        url = f"https://www.google.com/search?q={queries[0]}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        
        # Regex para preços em USD ($ XX.XX)
        precos_usd = re.findall(r'\$\s?(\d+\.?\d{2})', text)
        
        if precos_usd:
            # Pega o maior valor encontrado que seja "razoável" (evita $0.00 ou anos)
            # Filtra valores < 1000 (evita anos 2023, 2024) e > 5
            valores = []
            for p in precos_usd:
                try:
                    v = float(p)
                    if 5 < v < 1000: valores.append(v)
                except: pass
            
            if valores:
                preco_encontrado_usd = max(valores) # Assume o maior preço como o "pacote completo"
                
    except Exception as e:
        st.error(f"Erro na busca: {e}")

    # Conversão e Estimativa
    if preco_encontrado_usd > 0:
        preco_brl = preco_encontrado_usd * dolar
        return preco_brl
    
    return 0.0

def main():
    # Inicialização de Estado da Sessão
    if 'p_compra' not in st.session_state: st.session_state.p_compra = 0.0 # Custo zero para afiliado
    if 'p_venda' not in st.session_state: st.session_state.p_venda = 200.0
    if 'nome_produto' not in st.session_state: st.session_state.nome_produto = "Alpilean"

    # Callbacks
    def atualizar_dados_afiliado():
        termo = st.session_state.nome_produto
        if termo:
            with st.spinner(f"Buscando dados de afiliado para '{termo}' em ClickBank/Digistore..."):
                preco_brl = buscar_dados_afiliado(termo)
                
                if preco_brl > 0:
                    # Lógica de Afiliado:
                    # Preço de Venda = Valor que o cliente paga (Ticket)
                    # Preço de Compra (Custo) = 0 (Produto Digital)
                    # Mas para "simular" o ganho, vamos ajustar:
                    # p_venda -> Comissão (vamos estimar 65% do ticket, média do mercado)
                    
                    comissao_estimada = preco_brl * 0.65
                    
                    st.session_state.p_venda = comissao_estimada # Receita esperada
                    st.session_state.p_compra = 0.0 # Custo produto digital é zero (apenas ads)
                    
                    st.toast(f"Produto Encontrado! Valor Estimado (BRL): R$ {preco_brl:.2f}", icon="🇺🇸")
                    st.info(f"Comissão estimada (65%): R$ {comissao_estimada:.2f}")
                else:
                    st.toast("Dados não encontrados. Tente outro termo.", icon="⚠️")

    st.markdown("<h1 style='text-align: center;'>🤖 AGENTE DE ANÁLISE: ARBITRAGEM PRO</h1>", unsafe_allow_html=True)
    
    tab_task, tab_dash = st.tabs(["🎯 Missão: Analisar Produto", "📈 Workflow de Histórico"])

    with tab_task:
        # ENTRADA DE DADOS
        with st.expander("📦 Dados do Produto", expanded=True):
            col_search, col_btn = st.columns([3, 1])
            nome = col_search.text_input("Nome da Missão / Produto", key="nome_produto")
            col_btn.write("") # Espaçamento
            col_btn.write("") 
            if col_btn.button("🌍 Fetch Affiliate Data", use_container_width=True):
                 atualizar_dados_afiliado()

            col1, col2 = st.columns([3, 1])
            # nome já capturado acima
            qtd = col2.number_input("Qtd", min_value=1, value=1)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<h3 style='text-align: center;'>💰 Custos (Ads/CPA)</h3>", unsafe_allow_html=True)
            p_compra = st.number_input("Custo por Venda/CPA (R$)", key="p_compra", help="Quanto você gasta em ADS para fazer uma venda?")
            frete_entrada = st.number_input("Outros Custos (R$)", value=0.0)
        
        with c2:
            st.markdown("<h3 style='text-align: center;'>📊 Ganhos (Comissão)</h3>", unsafe_allow_html=True)
            p_venda = st.number_input("Comissão por Venda (R$)", key="p_venda")
            taxa_plataforma = st.number_input("Taxa Plataforma (%)", value=0.0, help="Geralmente 0 para afiliado (já descontado)")
            ads_percent = st.number_input("Markup de Segurança (%)", value=0.0)

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