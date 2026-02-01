# PLANO DE IMPLEMENTAÇÃO - TOKENIZAÇÃO DO SISTEMA
## @aios-master | Metodologia Alan Nicolas

---

## 📋 RESUMO EXECUTIVO

Este documento detalha o plano para aplicar os Design Tokens no projeto **Calculadora de Arbitragem de Produtos** sem quebrar a lógica de cálculo existente.

**Objetivo**: Aplicar sistema de tokens baseado em Tailwind/Shadcn Dark Mode mantendo 100% da funcionalidade atual.

**Status**: ✅ Fase 1 Concluída (Configuração Base)

---

## 🎯 PRINCÍPIOS DE IMPLEMENTAÇÃO

### 1. **Não Quebrar a Lógica**
- ✅ Nenhuma modificação no código Python de cálculo
- ✅ Apenas estilos CSS e configurações visuais
- ✅ Testes de validação após cada fase

### 2. **Aplicação Incremental**
- Fase por fase, testando cada mudança
- Rollback fácil se necessário
- Documentação de cada alteração

### 3. **Compatibilidade Streamlit**
- Respeitar limitações do Streamlit
- Usar CSS customizado quando necessário
- Fallback para estilos padrão

---

## 📊 FASES DE IMPLEMENTAÇÃO

### ✅ FASE 1: CONFIGURAÇÃO BASE (CONCLUÍDA)

**Objetivo**: Criar estrutura de tokens sem afetar visual atual

**Tarefas Realizadas**:
- [x] Criar pasta `.streamlit/`
- [x] Criar `config.toml` com tokens base
- [x] Criar `custom.css` com variáveis CSS
- [x] Criar `DESIGN_TOKENS.md` com mapeamento completo
- [x] Criar `PLANO_IMPLEMENTACAO_TOKENS.md` (este documento)

**Arquivos Criados**:
```
.streamlit/
├── config.toml          # Configuração tema Streamlit
└── custom.css           # CSS customizado com tokens
```

**Validação**:
- [ ] Testar aplicação com `streamlit run app.py`
- [ ] Verificar que cálculos funcionam normalmente
- [ ] Verificar que inputs respondem corretamente
- [ ] Verificar que botão de cálculo funciona

**Próximo Passo**: Validar Fase 1 antes de prosseguir

---

### 🔄 FASE 2: APLICAÇÃO DE TOKENS EM COMPONENTES DE FEEDBACK

**Objetivo**: Aplicar cores semânticas em mensagens (success/error/warning/info)

**Tarefas**:
- [ ] Verificar se `custom.css` está sendo carregado
- [ ] Testar `st.success()` com tokens de success
- [ ] Testar `st.error()` com tokens de danger
- [ ] Testar `st.warning()` com tokens de warning
- [ ] Testar `st.info()` com tokens de info

**Componentes Afetados**:
- Linha 295: `st.success()` - Oportunidade encontrada
- Linha 297: `st.error()` - Não é viável
- Linha 354-358: `st.success()` - Resultados positivos
- Linha 360-362: `st.error()` - Resultados negativos
- Linha 373-379: `st.info()` - Passos de ação
- Linha 382-388: `st.info()` - Passos de ação
- Linha 390-396: `st.success()` - Resultado final
- Linha 398-405: `st.warning()` - Não recomendado
- Linha 213-220: `st.warning()` - Riscos
- Linha 223-230: `st.info()` - Dicas

**Validação**:
- [ ] Mensagens exibem cores corretas
- [ ] Contraste WCAG AA mantido
- [ ] Legibilidade preservada
- [ ] Cálculos não afetados

**Rollback**: Remover seções de `.streamlit/custom.css` relacionadas

---

### 🔄 FASE 3: APLICAÇÃO DE TOKENS EM INPUTS

**Objetivo**: Aplicar tokens em campos de entrada (text_input, number_input, selectbox)

**Tarefas**:
- [ ] Verificar estilos de `st.text_input()`
- [ ] Verificar estilos de `st.number_input()`
- [ ] Verificar estilos de `st.selectbox()`
- [ ] Testar estados hover e focus
- [ ] Validar acessibilidade

**Componentes Afetados**:
- Linha 46-50: `st.text_input()` - Nome do produto
- Linha 52-56: `st.selectbox()` - Categoria
- Linha 59-62: `st.text_input()` - Código/Modelo
- Linha 64-70: `st.number_input()` - Quantidade
- Linha 81-86: `st.selectbox()` - Plataforma compra
- Linha 91-97: `st.number_input()` - Preço compra
- Linha 99-105: `st.number_input()` - Frete compra
- Linha 109-114: `st.selectbox()` - Plataforma venda
- Linha 119-125: `st.number_input()` - Preço venda
- Linha 127-133: `st.number_input()` - Frete venda
- Linha 143-150: `st.number_input()` - Comissão
- Linha 152-157: `st.number_input()` - Embalagem
- Linha 160-167: `st.number_input()` - Impostos
- Linha 169-175: `st.number_input()` - Anúncios
- Linha 178-184: `st.number_input()` - Mão de obra
- Linha 186-191: `st.number_input()` - Outros custos

**Validação**:
- [ ] Inputs exibem estilos corretos
- [ ] Estados hover/focus funcionam
- [ ] Valores podem ser inseridos normalmente
- [ ] Cálculos funcionam com novos valores

**Rollback**: Remover seções de inputs do `custom.css`

---

### 🔄 FASE 4: APLICAÇÃO DE TOKENS EM BOTÕES

**Objetivo**: Aplicar tokens no botão principal de cálculo

**Tarefas**:
- [ ] Verificar estilo do botão "CALCULAR LUCRO DA ARBITRAGEM"
- [ ] Testar estados hover e active
- [ ] Validar acessibilidade (contraste)

**Componentes Afetados**:
- Linha 196: `st.button()` - Botão calcular

**Validação**:
- [ ] Botão exibe cor primary (verde)
- [ ] Hover funciona corretamente
- [ ] Click funciona normalmente
- [ ] Cálculo é executado corretamente

**Rollback**: Remover seção de botões do `custom.css`

---

### 🔄 FASE 5: APLICAÇÃO DE TOKENS EM EXPANDERS E CARDS

**Objetivo**: Aplicar tokens em componentes de conteúdo expansível

**Tarefas**:
- [ ] Verificar estilo do `st.expander()` explicativo
- [ ] Testar interação (abrir/fechar)
- [ ] Validar legibilidade do conteúdo

**Componentes Afetados**:
- Linha 18-36: `st.expander()` - O que é arbitragem

**Validação**:
- [ ] Expander exibe estilos corretos
- [ ] Interação funciona normalmente
- [ ] Conteúdo legível

**Rollback**: Remover seção de expanders do `custom.css`

---

### 🔄 FASE 6: APLICAÇÃO DE TOKENS EM TIPOGRAFIA

**Objetivo**: Aplicar tokens de tipografia em títulos e textos

**Tarefas**:
- [ ] Verificar `st.title()` - Título principal
- [ ] Verificar `st.subheader()` - Seções
- [ ] Verificar `st.markdown()` - Textos gerais
- [ ] Verificar `st.caption()` - Rodapé

**Componentes Afetados**:
- Linha 14: `st.title()` - Título principal
- Linha 15: `st.markdown()` - Subtítulo
- Linha 41: `st.subheader()` - Dados do produto
- Linha 75: `st.subheader()` - Plataformas
- Linha 138: `st.subheader()` - Custos operacionais
- Linha 208: `st.subheader()` - Análise de risco
- Linha 302: `st.subheader()` - Resumo da operação
- Linha 327: `st.subheader()` - Detalhamento financeiro
- Linha 367: `st.subheader()` - Próximos passos
- Linha 409: `st.subheader()` - Análise de sensibilidade
- Linha 232: `st.caption()` - Aviso legal

**Validação**:
- [ ] Hierarquia tipográfica clara
- [ ] Legibilidade mantida
- [ ] Tamanhos apropriados

**Rollback**: Remover seção de tipografia do `custom.css`

---

### 🔄 FASE 7: APLICAÇÃO DE TOKENS EM TABELAS

**Objetivo**: Aplicar tokens na tabela de análise de sensibilidade

**Tarefas**:
- [ ] Verificar estilo do `st.dataframe()`
- [ ] Testar legibilidade dos dados
- [ ] Validar hover em linhas

**Componentes Afetados**:
- Linha 435: `st.dataframe()` - Análise de sensibilidade

**Validação**:
- [ ] Tabela exibe estilos corretos
- [ ] Dados legíveis
- [ ] Hover funciona

**Rollback**: Remover seção de tabelas do `custom.css`

---

### 🔄 FASE 8: REFINAMENTO E POLIMENTO

**Objetivo**: Ajustes finais e otimizações

**Tarefas**:
- [ ] Ajustar espaçamentos conforme tokens
- [ ] Aplicar border-radius consistente
- [ ] Melhorar transições
- [ ] Validar responsividade
- [ ] Testar em diferentes navegadores

**Validação**:
- [ ] Visual consistente
- [ ] Performance mantida
- [ ] Acessibilidade WCAG AA

---

## 🧪 TESTES DE VALIDAÇÃO

### Teste 1: Cálculo Básico
```
1. Abrir app.py
2. Preencher dados padrão (iPhone exemplo)
3. Clicar em "CALCULAR LUCRO DA ARBITRAGEM"
4. Verificar que cálculo funciona
5. Verificar que resultados exibem corretamente
```

### Teste 2: Validações
```
1. Tentar calcular com preço zero
2. Verificar mensagem de erro
3. Verificar que erro exibe cor danger
```

### Teste 3: Inputs
```
1. Preencher todos os campos
2. Verificar que valores são aceitos
3. Verificar estados hover/focus
4. Calcular e verificar resultado
```

### Teste 4: Responsividade
```
1. Testar em diferentes tamanhos de tela
2. Verificar que layout se adapta
3. Verificar legibilidade
```

---

## 🔄 PROCEDIMENTO DE ROLLBACK

Se algo quebrar, seguir estes passos:

1. **Backup**: Manter versão funcional do `app.py`
2. **Remover CSS**: Comentar seções problemáticas no `custom.css`
3. **Reset Config**: Voltar `config.toml` para valores padrão
4. **Testar**: Validar que tudo funciona novamente
5. **Documentar**: Registrar o que causou o problema

---

## 📝 CHECKLIST FINAL

Antes de considerar implementação completa:

- [ ] Todas as fases concluídas
- [ ] Todos os testes passando
- [ ] Cálculos funcionando 100%
- [ ] Visual consistente com design system
- [ ] Acessibilidade WCAG AA
- [ ] Performance mantida
- [ ] Documentação atualizada
- [ ] Sem erros no console do navegador

---

## 🚀 PRÓXIMOS PASSOS IMEDIATOS

1. **Validar Fase 1**: Testar aplicação com novos arquivos
2. **Documentar Resultados**: Registrar o que funciona e o que precisa ajuste
3. **Iterar**: Aplicar Fase 2 após validação da Fase 1

---

## 📚 REFERÊNCIAS

- `DESIGN_TOKENS.md` - Mapeamento completo de tokens
- `DESIGN_SYSTEM.md` - Design system original
- `.streamlit/config.toml` - Configuração tema
- `.streamlit/custom.css` - CSS customizado

---

**Documento criado por @aios-master**
**Data**: 2024
**Versão**: 1.0.0
