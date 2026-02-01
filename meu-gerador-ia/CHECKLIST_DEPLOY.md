# ✅ Checklist de Deploy - AIOS Hub de Arbitragem

## 📋 Pré-Deploy

### 1. Arquivos Essenciais
- [x] `app.py` - Aplicação principal
- [x] `requirements.txt` - Dependências Python
- [x] `README.md` - Documentação
- [x] `.gitignore` - Protege arquivos sensíveis
- [x] `.streamlit/config.toml` - Configuração do Streamlit

### 2. Segurança
- [x] `.env` está no `.gitignore`
- [x] `env.template` criado (sem chaves reais)
- [x] Nenhuma chave API commitada
- [x] Logs sensíveis ignorados

### 3. Código
- [x] Código testado localmente
- [x] Imports corretos
- [x] Compatível com Streamlit Cloud
- [x] Suporta variáveis de ambiente e secrets

### 4. Documentação
- [x] README.md completo
- [x] DEPLOY.md com instruções
- [x] QUICK_START.md para iniciantes

---

## 🚀 Passos para Deploy

### Passo 1: GitHub
```bash
# Verificar status
git status

# Adicionar arquivos
git add .

# Commit
git commit -m "Preparado para deploy no Streamlit Cloud"

# Push (se já tem repositório)
git push origin main
```

### Passo 2: Streamlit Cloud
1. [ ] Acessar https://share.streamlit.io
2. [ ] Login com GitHub
3. [ ] Criar novo app
4. [ ] Selecionar repositório
5. [ ] Configurar `app.py` como main file
6. [ ] Adicionar `GOOGLE_API_KEY` nas Secrets
7. [ ] Fazer deploy

### Passo 3: Verificação
1. [ ] App carrega sem erros
2. [ ] API key funciona
3. [ ] Interface responsiva
4. [ ] Testar calculadora manual
5. [ ] Testar upload CSV

---

## 🔑 Secrets do Streamlit Cloud

Formato TOML:
```toml
GOOGLE_API_KEY = "sua_chave_aqui"
```

Onde adicionar:
- Streamlit Cloud → Seu App → Settings → Secrets

---

## 🐛 Troubleshooting

### Erro: "Module not found"
- Verificar `requirements.txt`
- Todas as dependências listadas?

### Erro: "API Key not found"
- Verificar Secrets no Streamlit Cloud
- Formato correto? (TOML)

### App não inicia
- Verificar logs no Streamlit Cloud
- `app.py` na raiz?
- Branch correto selecionado?

---

## 📝 Notas Finais

- ✅ Código está pronto
- ✅ Documentação completa
- ✅ Segurança verificada
- ✅ Compatível com Streamlit Cloud

**Próximo passo**: Fazer push para GitHub e deploy!
