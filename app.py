import streamlit as st
import pandas as pd
import os
from datetime import datetime

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

def main():
    st.title("🤖 AGENTE DE ANÁLISE: ARBITRAGEM PRO")
    
    tab_task, tab_dash = st.tabs(["🎯 Missão: Analisar Produto", "📈 Workflow de Histórico"])

    with tab_task:
        # ENTRADA DE DADOS
        with st.expander("📦 Dados do Produto", expanded=True):
            col1, col2 = st.columns([3, 1])
            nome = col1.text_input("Nome da Missão / Produto", value="Scanner de Oportunidade")
            qtd = col2.number_input("Qtd", min_value=1, value=1)

        c1, c2 = st.columns(2)
        with c1:
            st.subheader("💰 Estrutura de Custos")
            p_compra = st.number_input("Preço Compra Un. (R$)", value=100.0)
            frete_entrada = st.number_input("Frete Entrada (Total R$)", value=0.0)
        
        with c2:
            st.subheader("📊 Parâmetros de Venda")
            p_venda = st.number_input("Preço Venda Un. (R$)", value=200.0)
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