# 🚀 Guia de Deploy - AIOS Hub de Arbitragem

## Opção 1: Streamlit Cloud (RECOMENDADO - Gratuito)

### Passo a Passo:

1. **Prepare seu repositório GitHub**
   ```bash
   git init
   git add .
   git commit -m "Preparado para deploy"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/meu-gerador-ia.git
   git push -u origin main
   ```

2. **Acesse [share.streamlit.io](https://share.streamlit.io)**

3. **Faça login com sua conta GitHub**

4. **Clique em "New app"**

5. **Configure o app**:
   - **Repository**: Selecione seu repositório
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL**: Escolha um nome único (ex: `meu-gerador-ia`)

6. **Configure as Secrets** (IMPORTANTE):
   - Clique em "Advanced settings"
   - Vá em "Secrets"
   - Adicione:
   ```toml
   GOOGLE_API_KEY = "sua_chave_api_aqui"
   ```

7. **Clique em "Deploy"**

8. **Aguarde o deploy** (2-3 minutos)

9. **Seu app estará online em**: `https://seu-app.streamlit.app`

---

## Opção 2: Railway (Alternativa)

1. **Acesse [railway.app](https://railway.app)**

2. **Conecte seu GitHub**

3. **Crie um novo projeto**

4. **Adicione as variáveis de ambiente**:
   - `GOOGLE_API_KEY`: Sua chave da API

5. **Deploy automático**

---

## Opção 3: Render (Alternativa)

1. **Acesse [render.com](https://render.com)**

2. **Crie um novo "Web Service"**

3. **Conecte seu GitHub**

4. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

5. **Adicione variáveis de ambiente**:
   - `GOOGLE_API_KEY`

---

## ✅ Checklist Pré-Deploy

- [ ] Código commitado no GitHub
- [ ] `requirements.txt` atualizado
- [ ] `.env` NÃO está no repositório (está no .gitignore)
- [ ] `GOOGLE_API_KEY` configurada nas Secrets do serviço
- [ ] Testado localmente com `streamlit run app.py`

---

## 🔧 Troubleshooting

### Erro: "Module not found"
- Verifique se todas as dependências estão em `requirements.txt`

### Erro: "API Key not found"
- Verifique se configurou `GOOGLE_API_KEY` nas Secrets do serviço

### App não inicia
- Verifique os logs do serviço
- Confirme que `app.py` está na raiz do repositório

---

## 📝 Notas Importantes

1. **Nunca commite o arquivo `.env`** - Ele contém suas chaves secretas
2. **Use Secrets/Variáveis de Ambiente** do serviço de deploy
3. **Logs**: Os logs do agente serão salvos em `.aios/logs/` (apenas localmente)
4. **Performance**: O Streamlit Cloud tem limites de uso gratuito

---

## 🎯 Após o Deploy

Seu sistema estará acessível publicamente e poderá:
- Processar análises financeiras
- Gerar insights com IA
- Processar planilhas CSV
- Funcionar 24/7 online

**URL do seu app**: Será fornecida pelo serviço escolhido
