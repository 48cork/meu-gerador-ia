import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Calculadora de Arbitragem de Produtos",
    page_icon="🛒",
    layout="wide"
)

def main():
    st.title("🛒 CALCULADORA DE ARBITRAGEM DE PRODUTOS")
    st.markdown("### Compare preços entre diferentes plataformas e encontre oportunidades de lucro")
    
    # Explicação
    with st.expander("📚 O QUE É ARBITRAGEM DE PRODUTOS?", expanded=True):
        st.markdown("""
        ### **Como funciona a arbitragem de produtos:**
        1. **Encontre um produto** com preço mais baixo em uma plataforma (ex: Amazon)
        2. **Venda o mesmo produto** por preço mais alto em outra plataforma (ex: Mercado Livre)
        3. **Lucro** = (Preço de venda) - (Preço de compra + custos)
        
        ### **Plataformas comuns:**
        - **🛍️ Marketplaces:** Amazon, Mercado Livre, Shopee, AliExpress
        - **🏪 Varejistas:** Magazine Luiza, Casas Bahia, Americanas
        - **📦 Atacadistas:** Atacadão, Assaí, Makro
        - **🌐 Internacionais:** eBay, Walmart, Best Buy
        
        ### **Exemplo Prático:**
        - Compra: iPhone na Amazon por R$ 3.000
        - Venda: iPhone no Mercado Livre por R$ 3.500
        - Custos: R$ 200 (frete, comissão, embalagem)
        - **Lucro: R$ 300 (10% de retorno)**
        """)
    
    st.markdown("---")
    
    # DADOS DO PRODUTO
    st.subheader("📦 DADOS DO PRODUTO")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        produto = st.text_input(
            "Nome do Produto",
            value="iPhone 15 128GB",
            placeholder="Ex: Smartphone Samsung Galaxy S23"
        )
        
        categoria = st.selectbox(
            "Categoria do Produto",
            ["Eletrônicos", "Eletrodomésticos", "Informática", "Moda", 
             "Beleza", "Livros", "Esportes", "Automotivo", "Outros"]
        )
    
    with col2:
        codigo = st.text_input(
            "Código/Modelo (opcional)",
            placeholder="Ex: ML-123456789"
        )
        
        quantidade = st.number_input(
            "Quantidade para comprar",
            min_value=1,
            max_value=100,
            value=1,
            step=1
        )
    
    st.markdown("---")
    
    # PLATAFORMAS DE COMPRA E VENDA
    st.subheader("🏪 PLATAFORMAS DE COMPRA E VENDA")
    
    col_compra, col_venda = st.columns(2)
    
    with col_compra:
        st.markdown("### **📍 PLATAFORMA DE COMPRA**")
        plataforma_compra = st.selectbox(
            "Onde você vai COMPRAR o produto:",
            ["Amazon", "Mercado Livre", "Shopee", "AliExpress", 
             "Magazine Luiza", "Casas Bahia", "Americanas", "eBay", "Outro"],
            key="compra"
        )
        
        if plataforma_compra == "Outro":
            plataforma_compra = st.text_input("Especifique a plataforma de compra:", key="compra_outro")
        
        preco_compra = st.number_input(
            "💰 Preço de COMPRA por unidade (R$)",
            min_value=0.01,
            value=3000.0,
            step=10.0
        )
        
        frete_compra = st.number_input(
            "🚚 Frete de COMPRA (R$)",
            min_value=0.0,
            value=50.0,
            step=5.0
        )
    
    with col_venda:
        st.markdown("### **📍 PLATAFORMA DE VENDA**")
        plataforma_venda = st.selectbox(
            "Onde você vai VENDER o produto:",
            ["Mercado Livre", "Shopee", "Amazon", "OLX", 
             "Facebook Marketplace", "Site próprio", "eBay", "Outro"],
            key="venda"
        )
        
        if plataforma_venda == "Outro":
            plataforma_venda = st.text_input("Especifique a plataforma de venda:", key="venda_outro")
        
        preco_venda = st.number_input(
            "💰 Preço de VENDA por unidade (R$)",
            min_value=0.01,
            value=3500.0,
            step=10.0
        )
        
        frete_venda = st.number_input(
            "🚚 Frete de VENDA (R$)",
            min_value=0.0,
            value=0.0,
            step=5.0,
            help="Frete que o cliente pagará (pode ser 0 se frete grátis)"
        )
    
    st.markdown("---")
    
    # CUSTOS ADICIONAIS
    st.subheader("📊 CUSTOS OPERACIONAIS")
    
    col_custos1, col_custos2, col_custos3 = st.columns(3)
    
    with col_custos1:
        comissao_percent = st.number_input(
            "📉 Comissão da plataforma de VENDA (%)",
            min_value=0.0,
            max_value=50.0,
            value=12.0,
            step=0.5,
            help="Porcentagem que a plataforma cobra sobre a venda"
        )
        
        custo_embalagem = st.number_input(
            "📦 Custo com embalagem (R$)",
            min_value=0.0,
            value=15.0,
            step=5.0
        )
    
    with col_custos2:
        imposto = st.number_input(
            "🏛️ Impostos sobre o lucro (%)",
            min_value=0.0,
            max_value=50.0,
            value=15.0,
            step=1.0,
            help="IRPF, Simples Nacional, etc."
        )
        
        custo_anuncio = st.number_input(
            "📢 Custo com anúncios (R$)",
            min_value=0.0,
            value=20.0,
            step=5.0,
            help="Investimento em propaganda"
        )
    
    with col_custos3:
        mao_obra = st.number_input(
            "👷 Mão de obra/ tempo (R$)",
            min_value=0.0,
            value=30.0,
            step=5.0,
            help="Seu tempo para gerenciar a operação"
        )
        
        outros_custos = st.number_input(
            "🔧 Outros custos (R$)",
            min_value=0.0,
            value=10.0,
            step=5.0
        )
    
    st.markdown("---")
    
    # BOTÃO DE CÁLCULO - CORRIGIDO: use_container_width -> width='stretch'
    if st.button("🧮 CALCULAR LUCRO DA ARBITRAGEM", type="primary", width='stretch'):
        calcular_arbitragem_produto(
            produto, categoria, codigo, quantidade,
            plataforma_compra, preco_compra, frete_compra,
            plataforma_venda, preco_venda, frete_venda,
            comissao_percent, custo_embalagem, imposto,
            custo_anuncio, mao_obra, outros_custos
        )
    
    st.markdown("---")
    
    # SEÇÃO DE HISTÓRICO (simulação)
    st.subheader("📈 ANÁLISE DE RISCO E DICAS")
    
    col_risco1, col_risco2 = st.columns(2)
    
    with col_risco1:
        st.warning("""
        **⚠️ RISCOS A CONSIDERAR:**
        1. **Variação de preços:** O produto pode baixar de preço
        2. **Estoque esgotado:** Pode não conseguir mais comprar
        3. **Problemas com frete:** Atrasos ou extravios
        4. **Devoluções:** Cliente pode devolver o produto
        5. **Concorrência:** Outros vendedores podem baixar preços
        """)
    
    with col_risco2:
        st.info("""
        **💡 DICAS PARA SUCESSO:**
        1. **Comece com produtos pequenos** para testar
        2. **Calcule TODOS os custos** antes de comprar
        3. **Verifique políticas de devolução**
            4. **Mantenha margem de segurança** de pelo menos 10%
        5. **Diversifique** entre diferentes produtos
        """)
    
    st.caption("🛡️ Esta ferramenta é para análise educacional. Consulte um contador para decisões fiscais.")

def calcular_arbitragem_produto(
    produto, categoria, codigo, quantidade,
    plataforma_compra, preco_compra, frete_compra,
    plataforma_venda, preco_venda, frete_venda,
    comissao_percent, custo_embalagem, imposto_percent,
    custo_anuncio, mao_obra, outros_custos
):
    """Calcula o lucro de arbitragem entre plataformas"""
    
    try:
        # CÁLCULOS BÁSICOS
        custo_total_compra = (preco_compra * quantidade) + frete_compra
        receita_bruta_venda = (preco_venda * quantidade) + (frete_venda * quantidade)
        
        # CUSTOS DE VENDA
        comissao_valor = receita_bruta_venda * (comissao_percent / 100)
        custos_totais = (custo_embalagem + custo_anuncio + mao_obra + outros_custos) * quantidade
        
        # LUCRO BRUTO E LÍQUIDO
        lucro_bruto = receita_bruta_venda - custo_total_compra - comissao_valor - custos_totais
        
        # IMPOSTO SOBRE O LUCRO
        imposto_valor = max(0, lucro_bruto * (imposto_percent / 100))
        lucro_liquido = lucro_bruto - imposto_valor
        
        # CÁLCULO DE MARGEM
        margem_bruta_percent = (lucro_bruto / custo_total_compra) * 100 if custo_total_compra > 0 else 0
        margem_liquida_percent = (lucro_liquido / custo_total_compra) * 100 if custo_total_compra > 0 else 0
        roi_percent = (lucro_liquido / custo_total_compra) * 100 if custo_total_compra > 0 else 0
        
        # VALIDAÇÃO DE OPORTUNIDADE
        oportunidade_valida = lucro_liquido > 0
        
        # EXIBIÇÃO DE RESULTADOS
        if oportunidade_valida:
            st.success(f"🎉 **OPORTUNIDADE ENCONTRADA!** Lucro garantido de R$ {lucro_liquido:.2f}")
        else:
            st.error(f"🚫 **NÃO É VIÁVEL** - Prejuízo de R$ {abs(lucro_liquido):.2f}")
        
        st.markdown("---")
        
        # RESUMO DA OPERAÇÃO
        st.subheader("📋 RESUMO DA OPERAÇÃO")
        
        col_res1, col_res2 = st.columns(2)
        
        with col_res1:
            st.markdown(f"""
            **📦 PRODUTO:** {produto}
            **🏷️ CATEGORIA:** {categoria}
            **🔢 QUANTIDADE:** {quantidade} unidade(s)
            """)
            
            if codigo:
                st.markdown(f"**🔗 CÓDIGO:** {codigo}")
        
        with col_res2:
            st.markdown(f"""
            **🛒 COMPRA EM:** {plataforma_compra}
            **💰 PREÇO COMPRA:** R$ {preco_compra:.2f}/un
            **💵 VENDA EM:** {plataforma_venda}
            **💰 PREÇO VENDA:** R$ {preco_venda:.2f}/un
            """)
        
        st.markdown("---")
        
        # DETALHAMENTO FINANCEIRO
        st.subheader("💵 DETALHAMENTO FINANCEIRO")
        
        col_fin1, col_fin2, col_fin3 = st.columns(3)
        
        with col_fin1:
            st.markdown("#### **SAÍDAS (CUSTOS)**")
            st.write(f"**Custo produtos:** R$ {preco_compra * quantidade:.2f}")
            st.write(f"**Frete compra:** R$ {frete_compra:.2f}")
            st.write(f"**Comissão ({comissao_percent}%):** R$ {comissao_valor:.2f}")
            st.write(f"**Embalagem:** R$ {custo_embalagem * quantidade:.2f}")
            st.write(f"**Anúncios:** R$ {custo_anuncio * quantidade:.2f}")
            st.write(f"**Mão de obra:** R$ {mao_obra * quantidade:.2f}")
            st.write(f"**Outros custos:** R$ {outros_custos * quantidade:.2f}")
            st.write(f"**Impostos ({imposto_percent}%):** R$ {imposto_valor:.2f}")
            st.markdown(f"**📍 TOTAL SAÍDAS:** R$ {custo_total_compra + comissao_valor + custos_totais + imposto_valor:.2f}")
        
        with col_fin2:
            st.markdown("#### **ENTRADAS (RECEITAS)**")
            st.write(f"**Venda produtos:** R$ {preco_venda * quantidade:.2f}")
            st.write(f"**Frete recebido:** R$ {frete_venda * quantidade:.2f}")
            st.markdown(f"**📍 TOTAL ENTRADAS:** R$ {receita_bruta_venda:.2f}")
        
        with col_fin3:
            st.markdown("#### **RESULTADO FINAL**")
            
            if oportunidade_valida:
                st.success(f"**💰 LUCRO BRUTO:** R$ {lucro_bruto:.2f}")
                st.success(f"**💵 LUCRO LÍQUIDO:** R$ {lucro_liquido:.2f}")
                st.success(f"**📈 MARGEM BRUTA:** {margem_bruta_percent:.1f}%")
                st.success(f"**📊 MARGEM LÍQUIDA:** {margem_liquida_percent:.1f}%")
                st.success(f"**🚀 ROI:** {roi_percent:.1f}%")
            else:
                st.error(f"**📉 PREJUÍZO BRUTO:** R$ {abs(lucro_bruto):.2f}")
                st.error(f"**📊 PREJUÍZO LÍQUIDO:** R$ {abs(lucro_liquido):.2f}")
                st.error(f"**⚠️ NEGATIVO:** {margem_liquida_percent:.1f}%")
        
        st.markdown("---")
        
        # INSTRUÇÕES DE AÇÃO
        st.subheader("🎯 PRÓXIMOS PASSOS")
        
        if oportunidade_valida:
            col_passos1, col_passos2 = st.columns(2)
            
            with col_passos1:
                st.info(f"""
                **✅ PASSO 1 - COMPRAR:**
                1. Acesse **{plataforma_compra}**
                2. Busque por: **"{produto}"**
                3. Compre por: **R$ {preco_compra:.2f}** cada
                4. Total a pagar: **R$ {custo_total_compra:.2f}**
                """)
            
            with col_passos2:
                st.info(f"""
                **✅ PASSO 2 - VENDER:**
                1. Acesse **{plataforma_venda}**
                2. Anuncie por: **R$ {preco_venda:.2f}** cada
                3. Ofereça: {"Frete grátis" if frete_venda == 0 else f"Frete: R$ {frete_venda:.2f}"}
                4. Receita esperada: **R$ {receita_bruta_venda:.2f}**
                """)
            
            st.success(f"""
            **🎊 RESULTADO FINAL ESPERADO:**
            Investindo **R$ {custo_total_compra:.2f}**, você terá um **lucro líquido de R$ {lucro_liquido:.2f}**
            em aproximadamente **{quantidade * 2} dias úteis** (compra + venda).
            
            **Retorno sobre investimento: {roi_percent:.1f}%**
            """)
        else:
            st.warning("""
            **⚠️ NÃO RECOMENDADO:**
            Esta operação resultaria em prejuízo. Considere:
            1. Buscar preços de compra mais baixos
            2. Aumentar o preço de venda
            3. Reduzir custos operacionais
            4. Escolher outro produto
            """)
        
        # TABELA DE ANÁLISE
        st.markdown("---")
        st.subheader("📊 ANÁLISE DE SENSIBILIDADE")
        
        # Simulação de variações de preço
        variacoes = [-10, -5, 0, +5, +10]
        dados_analise = []
        
        for variacao in variacoes:
            novo_preco_venda = preco_venda * (1 + variacao/100)
            nova_receita = (novo_preco_venda * quantidade) + (frete_venda * quantidade)
            novo_lucro = nova_receita - custo_total_compra - comissao_valor - custos_totais - imposto_valor
            dados_analise.append({
                "Variação Preço Venda": f"{variacao:+}%",
                "Novo Preço": f"R$ {novo_preco_venda:.2f}",
                "Lucro Líquido": f"R$ {novo_lucro:.2f}",
                "ROI": f"{(novo_lucro/custo_total_compra)*100:.1f}%" if custo_total_compra > 0 else "0%"
            })
        
        df_analise = pd.DataFrame(dados_analise)
        st.dataframe(df_analise, use_container_width=True)
        
    except Exception as e:
        st.error(f"❌ **Erro no cálculo:** {str(e)}")
        st.info("Verifique se todos os valores foram inseridos corretamente.")

if __name__ == "__main__":
    main()