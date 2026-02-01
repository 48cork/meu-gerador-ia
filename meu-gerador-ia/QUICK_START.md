# ⚡ Quick Start - Colocar Online em 5 Minutos

## 🚀 Deploy Rápido no Streamlit Cloud

### 1️⃣ Prepare o GitHub (2 min)
```bash
# Se ainda não tem repositório
git init
git add .
git commit -m "Sistema AIOS pronto para deploy"
git branch -M main

# Crie um repositório no GitHub, depois:
git remote add origin https://github.com/SEU_USUARIO/meu-gerador-ia.git
git push -u origin main
```

### 2️⃣ Deploy no Streamlit Cloud (3 min)

1. Acesse: **https://share.streamlit.io**
2. Faça login com GitHub
3. Clique em **"New app"**
4. Selecione seu repositório
5. **Main file**: `app.py`
6. Clique em **"Advanced settings"** → **"Secrets"**
7. Adicione:
   ```
   GOOGLE_API_KEY = "sua_chave_aqui"
   ```
8. Clique em **"Deploy"**

### 3️⃣ Pronto! 🎉

Seu app estará online em: `https://seu-app.streamlit.app`

---

## 🔑 Onde pegar a GOOGLE_API_KEY?

1. Acesse: **https://aistudio.google.com/apikey**
2. Faça login com sua conta Google
3. Clique em **"Create API Key"**
4. Copie a chave gerada
5. Cole nas Secrets do Streamlit Cloud

---

## ✅ Checklist

- [ ] Código no GitHub
- [ ] Conta no Streamlit Cloud
- [ ] GOOGLE_API_KEY configurada
- [ ] Deploy realizado

**Tempo total: ~5 minutos!**

---

## 🆘 Problemas?

- **Erro de módulo**: Verifique `requirements.txt`
- **Erro de API**: Confirme que a chave está nas Secrets
- **App não carrega**: Veja os logs no Streamlit Cloud

---

## 📱 Seu app estará acessível:

- ✅ 24/7 online
- ✅ Acesso público (ou privado, você escolhe)
- ✅ Atualização automática ao fazer push no GitHub
- ✅ Gratuito (com limites de uso)

**Pronto para usar! 🚀**
