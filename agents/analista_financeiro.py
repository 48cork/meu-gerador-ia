def calcular_missao(p_compra, p_venda, qtd, taxa_marketplace, ads_percent):
    """
    Simula o comportamento de um Agente Analista
    Baseado no AIOS Framework
    """
    faturamento = p_venda * qtd
    investimento = p_compra * qtd
    
    # Lógica de taxas (Imposto 6% + Taxa Fixa R$ 6)
    imposto = faturamento * 0.06
    comissao = faturamento * (taxa_marketplace / 100)
    marketing = faturamento * (ads_percent / 100)
    taxa_fixa = 6.0 * qtd
    
    lucro = faturamento - investimento - (imposto + comissao + marketing + taxa_fixa)
    roi = (lucro / investimento) * 100 if investimento > 0 else 0
    
    # Veredito do Agente
    if roi > 40:
        veredito = "💎 MISSÃO OURO"
        status_cor = "green"
    elif roi > 15:
        veredito = "✅ VIÁVEL"
        status_cor = "blue"
    else:
        veredito = "⚠️ ALTO RISCO"
        status_cor = "red"
        
    return {
        "lucro": lucro,
        "roi": roi,
        "veredito": veredito,
        "cor": status_cor
    }