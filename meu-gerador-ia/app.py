import streamlit as st
import pandas as pd
from datetime import datetime
from agents.analista_financeiro import calcular_missao

st.set_page_config(page_title="AIOS | Hub de Arbitragem", layout="wide")

# Criando as abas no topo da página
tab1, tab2 = st.tabs(["🧮 Calculadora Manual", "🔎 Scanner de Lista (CSV)"])

# --- ABA 1: CALCULADORA MANUAL ---
with tab1:
    st.header("Teste de Viabilidade Rápida")
    c1, c2 = st.columns(2)
    with c1:
        p_compra = st.number_input("Custo de Aquisição (R$)", value=100.0, key="manual_compra")
        p_venda = st.number_input("Preço de Venda (R$)", value=200.0, key="manual_venda")
    with c2:
        taxa_mkp = st.number_input("Taxa Marketplace (%)", value=12.0)
        ads = st.number_input("Investimento Ads (%)", value=5.0)

    if st.button("🚀 ANALISAR AGORA", use_container_width=True):
        with st.spinner("🤖 Analisando com IA..."):
            res = calcular_missao(p_compra, p_venda, 1, taxa_mkp, ads)
        
        st.divider()
        st.subheader(f"Veredito: {res['veredito']}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Lucro Estimado", f"R$ {res['lucro']:.2f}")
        with col2:
            st.metric("ROI", f"{res['roi']:.1f}%")
        
        # Exibe análise da IA se disponível
        if 'analise_ia' in res and res['analise_ia']:
            st.divider()
            with st.expander("💡 Análise Estratégica da IA", expanded=True):
                st.write(res['analise_ia'])

# --- ABA 2: SCANNER AUTOMÁTICO ---
with tab2:
    st.header("Scanner de Lote (Massa)")
    st.write("Suba sua planilha e deixe o Agente filtrar as oportunidades.")
    
    uploaded_file = st.file_uploader("Arraste seu arquivo CSV aqui", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        # Validação das colunas necessárias
        required_columns = ['nome', 'custo', 'preco_venda']
        if not all(col in df.columns for col in required_columns):
            st.error(f"❌ O CSV deve conter as colunas: {', '.join(required_columns)}")
            st.info("Exemplo de formato:\n```csv\nnome,custo,preco_venda\nProduto A,100,200\n```")
        else:
            # Barra de progresso
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # O Agente processa cada linha da sua planilha
            resultados = []
            total_rows = len(df)
            
            for idx, row in df.iterrows():
                res = calcular_missao(row['custo'], row['preco_venda'], 1, 12, 5)
                resultados.append({
                    "Produto": row['nome'],
                    "Lucro": res['lucro'],
                    "ROI %": res['roi'],
                    "Veredito": res['veredito']
                })
                # Atualiza progresso
                progress = (idx + 1) / total_rows
                progress_bar.progress(progress)
                status_text.text(f"Processando... {idx + 1}/{total_rows}")
            
            progress_bar.empty()
            status_text.empty()
            
            df_final = pd.DataFrame(resultados)
            
            # Estatísticas
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Analisado", len(df_final))
            with col2:
                ouro_count = len(df_final[df_final['Veredito'] == "💎 MISSÃO OURO"])
                st.metric("💎 Missões Ouro", ouro_count)
            with col3:
                viavel_count = len(df_final[df_final['Veredito'] == "✅ VIÁVEL"])
                st.metric("✅ Viáveis", viavel_count)
            
            # Filtro para mostrar só o que interessa
            so_ouro = st.checkbox("Mostrar apenas Missões Ouro", value=True)
            if so_ouro:
                df_exibir = df_final[df_final['Veredito'] == "💎 MISSÃO OURO"]
            else:
                df_exibir = df_final
                
            st.dataframe(df_exibir, use_container_width=True)
            
            # Botão para download
            if len(df_exibir) > 0:
                csv = df_exibir.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Baixar Resultados (CSV)",
                    data=csv,
                    file_name=f"analise_arbitragem_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
            
            st.success(f"✅ Análise concluída! Encontramos {len(df_exibir)} oportunidades.")