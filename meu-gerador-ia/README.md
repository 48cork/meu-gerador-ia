# AIOS | Hub de Arbitragem

Sistema inteligente de análise financeira para arbitragem de produtos, com IA integrada (Gemini) para insights estratégicos.

## 🚀 Funcionalidades

- **Calculadora Manual**: Análise rápida de viabilidade de produtos individuais
- **Scanner de Lote**: Processamento em massa de planilhas CSV
- **Análise com IA**: Insights estratégicos gerados pelo Gemini AI
- **Métricas Financeiras**: Cálculo automático de Lucro, ROI e Veredito

## 📋 Requisitos

- Python 3.8+
- Google API Key (Gemini)

## 🛠️ Instalação Local

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd meu-gerador-ia
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
# Copie o template
cp env.template .env

# Edite o .env e adicione sua GOOGLE_API_KEY
GOOGLE_API_KEY=sua_chave_aqui
```

4. Execute a aplicação:
```bash
streamlit run app.py
```

## 🌐 Deploy Online (Streamlit Cloud)

### Opção 1: Streamlit Cloud (Recomendado - Gratuito)

1. **Faça push do código para GitHub**:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <seu-repositorio-github>
git push -u origin main
```

2. **Acesse [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Conecte seu repositório GitHub**

4. **Configure as Secrets**:
   - Vá em Settings → Secrets
   - Adicione:
   ```
   GOOGLE_API_KEY=sua_chave_aqui
   ```

5. **Deploy automático**: O Streamlit Cloud detecta automaticamente o `app.py` e faz o deploy

### Opção 2: Outros Serviços

- **Heroku**: Use `Procfile` com `web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
- **AWS/GCP/Azure**: Use containers Docker ou serviços de aplicação
- **Railway/Render**: Similar ao Heroku

## 📁 Estrutura do Projeto

```
meu-gerador-ia/
├── app.py                      # Interface Streamlit
├── agents/
│   └── analista_financeiro.py  # Agente de análise financeira
├── .aios/
│   └── logs/                    # Logs do sistema
├── requirements.txt             # Dependências Python
└── env.template                 # Template de variáveis de ambiente
```

## 🔑 Variáveis de Ambiente

- `GOOGLE_API_KEY`: Chave da API do Google AI Studio (Gemini)
- `AIOS_DEBUG`: (Opcional) Ativa modo debug

## 📊 Formato CSV para Scanner

O CSV deve conter as colunas:
- `nome`: Nome do produto
- `custo`: Custo de aquisição
- `preco_venda`: Preço de venda

Exemplo:
```csv
nome,custo,preco_venda
Produto A,100,200
Produto B,150,180
```

## 🎯 Vereditos

- **💎 MISSÃO OURO**: ROI > 40% - Oportunidade excelente
- **✅ VIÁVEL**: ROI entre 15% e 40% - Viável com cuidado
- **⚠️ ALTO RISCO**: ROI < 15% - Alto risco ou inviável

## 📝 Logs

Os logs do sistema são salvos em `.aios/logs/agent.log` e incluem:
- Início de cada análise
- Cálculos realizados
- Consultas à IA
- Erros e avisos

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto é de uso pessoal/comercial.

## 🆘 Suporte

Para problemas ou dúvidas, verifique os logs em `.aios/logs/agent.log`
