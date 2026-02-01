# 🔧 Configuração do GitHub

## Comandos para Preparar o Repositório

### 1. Inicializar Git (se ainda não foi feito)
```bash
git init
git branch -M main
```

### 2. Adicionar Arquivos
```bash
# Ver o que será adicionado
git status

# Adicionar todos os arquivos (exceto os no .gitignore)
git add .
```

### 3. Primeiro Commit
```bash
git commit -m "feat: Sistema AIOS Hub de Arbitragem pronto para deploy

- Interface Streamlit completa
- Agente de análise financeira com IA
- Suporte para análise manual e em lote
- Integração com Gemini AI
- Logging completo
- Preparado para Streamlit Cloud"
```

### 4. Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Nome do repositório: `meu-gerador-ia` (ou outro nome)
3. Descrição: "Sistema inteligente de análise financeira para arbitragem"
4. Público ou Privado (sua escolha)
5. **NÃO** marque "Add README" (já temos)
6. Clique em "Create repository"

### 5. Conectar e Fazer Push
```bash
# Adicionar remote (substitua SEU_USUARIO)
git remote add origin https://github.com/SEU_USUARIO/meu-gerador-ia.git

# Verificar remote
git remote -v

# Push inicial
git push -u origin main
```

### 6. Verificar no GitHub
- [ ] Todos os arquivos aparecem
- [ ] `.env` NÃO está no repositório
- [ ] `README.md` aparece corretamente
- [ ] Código está visível

---

## 📁 Estrutura Esperada no GitHub

```
meu-gerador-ia/
├── .gitignore
├── .gitattributes
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml.example
├── agents/
│   ├── __init__.py
│   ├── analista_financeiro.py
│   └── workflows/
├── app.py
├── requirements.txt
├── README.md
├── DEPLOY.md
├── QUICK_START.md
├── CHECKLIST_DEPLOY.md
├── Procfile
├── setup.py
└── env.template
```

---

## ⚠️ Arquivos que NÃO devem estar no GitHub

- `.env` (contém chaves secretas)
- `.streamlit/secrets.toml` (secrets reais)
- `*.log` (logs)
- `__pycache__/` (cache Python)
- `.aios/logs/*.log` (logs do sistema)

Todos esses devem estar no `.gitignore` ✅

---

## 🔄 Atualizações Futuras

```bash
# Após fazer mudanças
git add .
git commit -m "descrição das mudanças"
git push origin main
```

O Streamlit Cloud atualiza automaticamente! 🚀
