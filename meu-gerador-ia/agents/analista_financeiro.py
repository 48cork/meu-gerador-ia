import google.generativeai as genai
import os
import logging
from datetime import datetime
from dotenv import load_dotenv

# Configuração de logging para AIOS (PRIMEIRO - antes de tudo)
LOG_DIR = ".aios/logs"
LOG_FILE = os.path.join(LOG_DIR, "agent.log")

# Garante que o diretório de logs existe
os.makedirs(LOG_DIR, exist_ok=True)

# Configura o logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('analista_financeiro')

# Carrega a chave do AI Studio
# Suporta tanto .env local quanto Streamlit Cloud Secrets
load_dotenv()

# Tenta obter a chave de diferentes fontes (compatível com Streamlit Cloud)
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    # Tenta obter do Streamlit secrets (se estiver rodando no Streamlit Cloud)
    try:
        import streamlit as st
        if hasattr(st, 'secrets') and 'GOOGLE_API_KEY' in st.secrets:
            api_key = st.secrets['GOOGLE_API_KEY']
    except:
        pass

if not api_key:
    logger.warning("⚠️ GOOGLE_API_KEY não encontrada! Configure no .env ou Streamlit Secrets")
else:
    genai.configure(api_key=api_key)

# Tenta inicializar o modelo - tenta gemini-1.5-flash primeiro, depois gemini-1.5-pro
def get_model():
    """Inicializa o modelo Gemini, tentando diferentes nomes de modelo"""
    # Primeiro, lista todos os modelos disponíveis para debug
    logger.info("Listando modelos disponíveis na API...")
    available_models = []
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
                logger.info(f"  ✓ {m.name} (suporta generateContent)")
    except Exception as e:
        logger.warning(f"Erro ao listar modelos: {str(e)}")
    
    # Tenta os modelos mais comuns (priorizando os mais recentes e disponíveis)
    model_names = [
        'models/gemini-2.5-flash',      # Mais recente e rápido
        'models/gemini-2.5-pro',        # Mais recente e poderoso
        'models/gemini-2.0-flash',      # Versão 2.0
        'models/gemini-flash-latest',   # Sempre a versão mais recente
        'models/gemini-pro-latest',     # Sempre a versão pro mais recente
        'gemini-1.5-flash',             # Fallback para versões antigas
        'gemini-1.5-pro',               # Fallback para versões antigas
        'gemini-pro'                    # Fallback para versões muito antigas
    ]
    
    for model_name in model_names:
        try:
            logger.info(f"Tentando inicializar modelo: {model_name}")
            model = genai.GenerativeModel(model_name)
            # Testa se realmente funciona fazendo uma chamada de teste
            test_response = model.generate_content("test")
            logger.info(f"✅ Modelo {model_name} inicializado e testado com sucesso!")
            return model
        except Exception as e:
            error_msg = str(e)
            logger.warning(f"❌ Modelo {model_name} falhou: {error_msg[:100]}")
            # Se o erro menciona modelos disponíveis, tenta usar um deles
            if available_models and 'not found' in error_msg.lower():
                logger.info(f"Tentando usar modelos da lista disponível...")
                for avail_model in available_models:
                    if 'gemini' in avail_model.lower():
                        try:
                            logger.info(f"Tentando: {avail_model}")
                            model = genai.GenerativeModel(avail_model)
                            test_response = model.generate_content("test")
                            logger.info(f"✅ Modelo {avail_model} funcionou!")
                            return model
                        except:
                            continue
            continue
    
    raise Exception("Nenhum modelo Gemini disponível. Verifique sua API key e os modelos disponíveis.")

# Tenta inicializar o modelo
try:
    model = get_model()
except Exception as e:
    logger.error(f"Erro crítico ao inicializar modelo: {str(e)}")
    model = None

def calcular_missao(p_compra, p_venda, qtd, taxa_marketplace, ads_percent):
    logger.info("=" * 60)
    logger.info(f"🚀 MISSÃO INICIADA | Custo: R${p_compra:.2f} | Venda: R${p_venda:.2f} | Qtd: {qtd}")
    
    # --- Sua Lógica Matemática (O que você já tem) ---
    faturamento = p_venda * qtd
    investimento = p_compra * qtd
    lucro = faturamento - investimento - (faturamento * 0.06) - (faturamento * (taxa_marketplace / 100)) - (faturamento * (ads_percent / 100)) - (6.0 * qtd)
    roi = (lucro / investimento) * 100 if investimento > 0 else 0
    
    veredito_matematico = "💎 MISSÃO OURO" if roi > 40 else "✅ VIÁVEL" if roi > 15 else "⚠️ ALTO RISCO"
    
    logger.info(f"📊 CÁLCULOS | Faturamento: R${faturamento:.2f} | Investimento: R${investimento:.2f}")
    logger.info(f"💰 RESULTADO | Lucro: R${lucro:.2f} | ROI: {roi:.1f}% | Veredito: {veredito_matematico}")

    # --- A MÁGICA DO ALAN: O INSIGHT DO AGENTE ---
    if model is None:
        logger.error("❌ Modelo Gemini não está disponível. Pulando análise IA.")
        insight_ia = "Análise IA indisponível - modelo não inicializado."
    else:
        logger.info("🤖 CONSULTANDO GEMINI AI para análise estratégica...")
        prompt = f"""
        Aja como um especialista em arbitragem. 
        Produto com Custo: R${p_compra} e Venda: R${p_venda}. 
        Lucro calculado: R${lucro:.2f} e ROI: {roi:.1f}%.
        O veredito matemático é {veredito_matematico}.
        Dê uma recomendação estratégica curta (2 frases) sobre este produto.
        """
        
        try:
            resposta = model.generate_content(prompt)
            insight_ia = resposta.text
            logger.info(f"✨ INSIGHT IA: {insight_ia[:100]}...")
            logger.info("✅ MISSÃO CONCLUÍDA COM SUCESSO")
        except Exception as e:
            logger.error(f"❌ ERRO ao consultar Gemini AI: {str(e)}")
            insight_ia = "Análise IA indisponível no momento."
    
    logger.info("=" * 60)

    return {
        "lucro": lucro, 
        "roi": roi, 
        "veredito": veredito_matematico,
        "analise_ia": insight_ia # O Agente agora pensa!
    }