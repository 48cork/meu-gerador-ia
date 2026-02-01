# DESIGN_TOKENS.md - Sistema de Tokenização
## Metodologia Alan Nicolas | Baseado em Tailwind/Shadcn Dark Mode

---

## 📊 MAPEAMENTO DE CORES HEXADECIMAIS ATUAIS

### Cores Identificadas no DESIGN_SYSTEM.md:

| Token Atual | Valor HEX | Uso Semântico | Status |
|------------|-----------|---------------|--------|
| `primary` | `#2ECC71` | Verde Sucesso (Lucro) | ✅ Definido |
| `secondary` | `#3498DB` | Azul Ação (Botões/Links) | ✅ Definido |
| `danger` | `#E74C3C` | Vermelho Alerta (Prejuízo) | ✅ Definido |
| `background-dark` | `#121212` | Background Principal | ✅ Definido |
| `surface` | `#1E1E1E` | Cards/Superfícies | ✅ Definido |
| `text-primary` | `#FFFFFF` | Texto Principal | ✅ Definido |
| `text-secondary` | `#B3B3B3` | Texto Secundário | ✅ Definido |

### Cores Implícitas do Streamlit (Identificadas no app.py):

| Componente Streamlit | Cor Padrão | Uso no App | Necessita Token |
|----------------------|------------|------------|-----------------|
| `st.success()` | Verde claro | Oportunidades válidas, Lucro | ✅ Sim |
| `st.error()` | Vermelho claro | Prejuízo, Erros | ✅ Sim |
| `st.warning()` | Amarelo/Laranja | Avisos, Riscos | ✅ Sim |
| `st.info()` | Azul claro | Informações, Dicas | ✅ Sim |
| `st.button()` (primary) | Azul padrão | Botão calcular | ✅ Sim |
| `st.expander()` | Cinza claro | Seção explicativa | ✅ Sim |

---

## 🎨 PALETA DE TOKENS - TAILWIND/SHADCN DARK MODE

### Estrutura Hierárquica (Seguindo Shadcn/Tailwind):

```
colors/
├── semantic/          (Cores semânticas - uso direto)
├── neutral/           (Escala de cinzas)
├── accent/            (Cores de destaque)
└── state/             (Estados: hover, focus, disabled)
```

---

## 1. TOKENS SEMÂNTICOS (Semantic Colors)

### 1.1 Success (Lucro/Oportunidades)
```yaml
success:
  base: "#22C55E"        # Tailwind green-500 (mais moderno que #2ECC71)
  light: "#4ADE80"       # green-400 (hover states)
  dark: "#16A34A"        # green-600 (pressed/active)
  foreground: "#FFFFFF"  # Texto sobre success
  muted: "#15803D"       # green-700 (backgrounds suaves)
```

### 1.2 Danger (Prejuízo/Erros)
```yaml
danger:
  base: "#EF4444"        # Tailwind red-500 (mais moderno que #E74C3C)
  light: "#F87171"       # red-400
  dark: "#DC2626"        # red-600
  foreground: "#FFFFFF"
  muted: "#B91C1C"       # red-700
```

### 1.3 Warning (Avisos/Riscos)
```yaml
warning:
  base: "#F59E0B"        # Tailwind amber-500
  light: "#FBBF24"       # amber-400
  dark: "#D97706"        # amber-600
  foreground: "#FFFFFF"
  muted: "#B45309"       # amber-700
```

### 1.4 Info (Informações/Dicas)
```yaml
info:
  base: "#3B82F6"        # Tailwind blue-500 (mais moderno que #3498DB)
  light: "#60A5FA"       # blue-400
  dark: "#2563EB"        # blue-600
  foreground: "#FFFFFF"
  muted: "#1D4ED8"       # blue-700
```

### 1.5 Primary (Ação Principal)
```yaml
primary:
  base: "#22C55E"        # Alinhado com success (verde)
  light: "#4ADE80"       # green-400
  dark: "#16A34A"        # green-600
  foreground: "#FFFFFF"
  muted: "#15803D"       # green-700
```

### 1.6 Secondary (Ação Secundária)
```yaml
secondary:
  base: "#6366F1"        # Tailwind indigo-500 (mais sofisticado)
  light: "#818CF8"       # indigo-400
  dark: "#4F46E5"        # indigo-600
  foreground: "#FFFFFF"
  muted: "#4338CA"       # indigo-700
```

---

## 2. TOKENS NEUTROS (Neutral Scale)

### 2.1 Background (Fundo)
```yaml
background:
  base: "#0A0A0A"        # Shadcn dark (mais escuro que #121212)
  elevated: "#1A1A1A"    # Cards/Surfaces (mais escuro que #1E1E1E)
  overlay: "#000000"     # Overlays/Modals (com opacity)
  muted: "#141414"       # Backgrounds secundários
```

### 2.2 Border (Bordas)
```yaml
border:
  base: "#262626"        # Tailwind neutral-800
  light: "#404040"       # neutral-700 (hover)
  dark: "#171717"        # neutral-900
  muted: "#1F1F1F"       # Bordas sutis
```

### 2.3 Text (Texto)
```yaml
text:
  primary: "#FAFAFA"     # Tailwind neutral-50 (mais suave que #FFFFFF)
  secondary: "#A3A3A3"   # neutral-400 (mais legível que #B3B3B3)
  tertiary: "#737373"    # neutral-500 (texto desabilitado)
  inverse: "#0A0A0A"    # Texto sobre backgrounds claros
  muted: "#525252"       # neutral-600 (texto muito sutil)
```

### 2.4 Surface (Superfícies/Cards)
```yaml
surface:
  base: "#1A1A1A"        # Cards principais
  elevated: "#262626"    # Cards hover/active
  pressed: "#0F0F0F"     # Cards pressed
  muted: "#141414"       # Backgrounds de seções
```

---

## 3. TOKENS DE ESTADO (State Colors)

### 3.1 Interactive States
```yaml
interactive:
  hover:
    background: "#262626"  # neutral-800
    border: "#404040"      # neutral-700
  focus:
    ring: "#3B82F6"        # blue-500
    ring-offset: "#0A0A0A" # background base
  active:
    background: "#0F0F0F" # neutral-950
  disabled:
    background: "#171717"  # neutral-900
    text: "#525252"        # neutral-600
    border: "#262626"      # neutral-800
```

### 3.2 Input States
```yaml
input:
  background: "#1A1A1A"    # surface base
  border: "#262626"        # border base
  border-hover: "#404040"  # border light
  border-focus: "#3B82F6"  # info base
  placeholder: "#737373"   # text tertiary
  text: "#FAFAFA"          # text primary
```

---

## 4. TOKENS DE ESPAÇAMENTO (Spacing)

### Baseado em escala 4px (Tailwind padrão):
```yaml
spacing:
  xs: "4px"      # 0.25rem
  sm: "8px"      # 0.5rem
  md: "16px"     # 1rem
  lg: "24px"     # 1.5rem
  xl: "32px"     # 2rem
  "2xl": "48px"  # 3rem
  "3xl": "64px"  # 4rem
```

---

## 5. TOKENS DE TIPOGRAFIA (Typography)

### Font Family
```yaml
font:
  family:
    sans: "Inter, system-ui, -apple-system, sans-serif"
    mono: "JetBrains Mono, 'Courier New', monospace"
```

### Font Sizes (Baseado em escala rem)
```yaml
font-size:
  xs: "0.75rem"    # 12px
  sm: "0.875rem"   # 14px
  base: "1rem"     # 16px
  lg: "1.125rem"   # 18px
  xl: "1.25rem"    # 20px
  "2xl": "1.5rem"  # 24px
  "3xl": "1.875rem" # 30px
  "4xl": "2rem"    # 32px (Display)
```

### Font Weights
```yaml
font-weight:
  light: 300
  regular: 400
  medium: 500
  semibold: 600
  bold: 700
```

### Line Heights
```yaml
line-height:
  tight: 1.25
  normal: 1.5
  relaxed: 1.75
```

---

## 6. TOKENS DE BORDAS (Border Radius)

```yaml
radius:
  none: "0px"
  sm: "4px"
  md: "8px"        # Padrão para inputs (conforme DESIGN_SYSTEM.md)
  lg: "12px"
  xl: "16px"
  full: "9999px"
```

---

## 7. TOKENS DE SOMBRA (Shadows)

### Dark Mode Shadows (sutis, para profundidade)
```yaml
shadow:
  sm: "0 1px 2px 0 rgba(0, 0, 0, 0.5)"
  md: "0 4px 6px -1px rgba(0, 0, 0, 0.5)"
  lg: "0 10px 15px -3px rgba(0, 0, 0, 0.5)"
  xl: "0 20px 25px -5px rgba(0, 0, 0, 0.5)"
  inner: "inset 0 2px 4px 0 rgba(0, 0, 0, 0.5)"
```

---

## 8. MAPEAMENTO DE COMPONENTES STREAMLIT

### 8.1 Componentes Identificados no app.py:

| Componente | Uso Atual | Token Aplicável | Customização Necessária |
|------------|-----------|-----------------|-------------------------|
| `st.title()` | Título principal | `text.primary` + `font-size.4xl` | ✅ CSS customizado |
| `st.subheader()` | Seções | `text.primary` + `font-size.2xl` | ✅ CSS customizado |
| `st.markdown()` | Texto geral | `text.primary/secondary` | ✅ CSS customizado |
| `st.text_input()` | Inputs de texto | `input.*` | ✅ Via config.toml + CSS |
| `st.number_input()` | Inputs numéricos | `input.*` | ✅ Via config.toml + CSS |
| `st.selectbox()` | Seletores | `input.*` | ✅ Via config.toml + CSS |
| `st.button()` | Botão calcular | `primary.*` | ✅ Via config.toml |
| `st.success()` | Lucro/Oportunidade | `success.*` | ✅ CSS customizado |
| `st.error()` | Prejuízo/Erro | `danger.*` | ✅ CSS customizado |
| `st.warning()` | Avisos | `warning.*` | ✅ CSS customizado |
| `st.info()` | Informações | `info.*` | ✅ CSS customizado |
| `st.expander()` | Seção explicativa | `surface.*` + `border.*` | ✅ CSS customizado |
| `st.dataframe()` | Tabela análise | `surface.*` + `border.*` | ✅ CSS customizado |
| `st.columns()` | Layout | `background.*` | ✅ CSS customizado |

---

## 9. CONFIGURAÇÃO STREAMLIT (config.toml)

### Arquivo: `.streamlit/config.toml`

```toml
[theme]
# Cores Base
primaryColor = "#22C55E"              # success.base
backgroundColor = "#0A0A0A"           # background.base
secondaryBackgroundColor = "#1A1A1A"  # surface.base
textColor = "#FAFAFA"                 # text.primary
font = "sans serif"

# Configurações adicionais
[server]
headless = true

[browser]
gatherUsageStats = false
```

---

## 10. CSS CUSTOMIZADO (custom.css)

### Arquivo: `.streamlit/custom.css`

```css
/* Importar fonte Inter */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Root Variables (Design Tokens) */
:root {
  /* Success */
  --color-success-base: #22C55E;
  --color-success-light: #4ADE80;
  --color-success-dark: #16A34A;
  
  /* Danger */
  --color-danger-base: #EF4444;
  --color-danger-light: #F87171;
  --color-danger-dark: #DC2626;
  
  /* Warning */
  --color-warning-base: #F59E0B;
  --color-warning-light: #FBBF24;
  --color-warning-dark: #D97706;
  
  /* Info */
  --color-info-base: #3B82F6;
  --color-info-light: #60A5FA;
  --color-info-dark: #2563EB;
  
  /* Primary */
  --color-primary-base: #22C55E;
  --color-primary-light: #4ADE80;
  --color-primary-dark: #16A34A;
  
  /* Secondary */
  --color-secondary-base: #6366F1;
  --color-secondary-light: #818CF8;
  --color-secondary-dark: #4F46E5;
  
  /* Background */
  --color-bg-base: #0A0A0A;
  --color-bg-elevated: #1A1A1A;
  --color-bg-overlay: #000000;
  --color-bg-muted: #141414;
  
  /* Border */
  --color-border-base: #262626;
  --color-border-light: #404040;
  --color-border-dark: #171717;
  
  /* Text */
  --color-text-primary: #FAFAFA;
  --color-text-secondary: #A3A3A3;
  --color-text-tertiary: #737373;
  
  /* Surface */
  --color-surface-base: #1A1A1A;
  --color-surface-elevated: #262626;
  --color-surface-pressed: #0F0F0F;
  
  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  
  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  
  /* Typography */
  --font-family-sans: 'Inter', system-ui, sans-serif;
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-4xl: 2rem;
}

/* Aplicar fonte global */
* {
  font-family: var(--font-family-sans);
}

/* Customizar st.success */
.stSuccess {
  background-color: rgba(34, 197, 94, 0.1);
  border-left: 4px solid var(--color-success-base);
  color: var(--color-success-light);
  border-radius: var(--radius-md);
  padding: var(--spacing-md);
}

/* Customizar st.error */
.stError {
  background-color: rgba(239, 68, 68, 0.1);
  border-left: 4px solid var(--color-danger-base);
  color: var(--color-danger-light);
  border-radius: var(--radius-md);
  padding: var(--spacing-md);
}

/* Customizar st.warning */
.stWarning {
  background-color: rgba(245, 158, 11, 0.1);
  border-left: 4px solid var(--color-warning-base);
  color: var(--color-warning-light);
  border-radius: var(--radius-md);
  padding: var(--spacing-md);
}

/* Customizar st.info */
.stInfo {
  background-color: rgba(59, 130, 246, 0.1);
  border-left: 4px solid var(--color-info-base);
  color: var(--color-info-light);
  border-radius: var(--radius-md);
  padding: var(--spacing-md);
}

/* Customizar inputs */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox > div > div > select {
  background-color: var(--color-surface-base);
  border: 1px solid var(--color-border-base);
  border-radius: var(--radius-md);
  color: var(--color-text-primary);
  padding: var(--spacing-sm) var(--spacing-md);
}

.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus,
.stSelectbox > div > div > select:focus {
  border-color: var(--color-info-base);
  outline: 2px solid var(--color-info-base);
  outline-offset: 2px;
}

/* Customizar botões */
.stButton > button {
  background-color: var(--color-primary-base);
  color: var(--color-text-primary);
  border-radius: var(--radius-md);
  border: none;
  padding: var(--spacing-sm) var(--spacing-lg);
  font-weight: 600;
  transition: all 0.2s;
}

.stButton > button:hover {
  background-color: var(--color-primary-light);
  transform: translateY(-1px);
}

.stButton > button:active {
  background-color: var(--color-primary-dark);
}

/* Customizar expander */
.streamlit-expanderHeader {
  background-color: var(--color-surface-base);
  border: 1px solid var(--color-border-base);
  border-radius: var(--radius-md);
  color: var(--color-text-primary);
}

.streamlit-expanderContent {
  background-color: var(--color-bg-muted);
  border-radius: var(--radius-md);
  padding: var(--spacing-md);
}

/* Customizar tabelas */
.dataframe {
  background-color: var(--color-surface-base);
  border: 1px solid var(--color-border-base);
  border-radius: var(--radius-md);
}

/* Customizar separadores */
hr {
  border-color: var(--color-border-base);
  margin: var(--spacing-lg) 0;
}
```

---

## 11. PLANO DE IMPLEMENTAÇÃO

### Fase 1: Configuração Base (Sem quebrar lógica)
- [ ] Criar pasta `.streamlit/`
- [ ] Criar `config.toml` com tokens base
- [ ] Criar `custom.css` com variáveis CSS
- [ ] Testar aplicação (lógica deve funcionar igual)

### Fase 2: Aplicação Gradual de Tokens
- [ ] Aplicar tokens em componentes de feedback (success/error/warning/info)
- [ ] Aplicar tokens em inputs (text_input, number_input, selectbox)
- [ ] Aplicar tokens em botões
- [ ] Aplicar tokens em expanders e cards

### Fase 3: Refinamento Visual
- [ ] Ajustar espaçamentos conforme tokens
- [ ] Aplicar border-radius consistente
- [ ] Melhorar tipografia (tamanhos e pesos)
- [ ] Adicionar transições suaves

### Fase 4: Validação
- [ ] Testar todos os cálculos (não deve quebrar)
- [ ] Validar acessibilidade (contraste WCAG AA)
- [ ] Testar responsividade
- [ ] Documentar mudanças

---

## 12. CHECKLIST DE VALIDAÇÃO

### Antes de Aplicar Tokens:
- ✅ Lógica de cálculo intacta
- ✅ Validações funcionando
- ✅ Todos os inputs funcionais
- ✅ Botão de cálculo operacional

### Após Aplicar Tokens:
- ✅ Visual consistente com design system
- ✅ Cores semânticas aplicadas corretamente
- ✅ Tipografia legível e hierárquica
- ✅ Espaçamentos consistentes
- ✅ Estados interativos (hover/focus) funcionando

---

## 13. NOTAS IMPORTANTES

1. **Não modificar lógica de cálculo**: Apenas estilos visuais serão alterados
2. **Manter compatibilidade**: Streamlit pode ter limitações de customização
3. **Testar incrementalmente**: Aplicar tokens gradualmente e testar
4. **Fallback**: Manter valores padrão do Streamlit como fallback
5. **Performance**: CSS customizado não afeta performance de cálculos

---

## 14. REFERÊNCIAS

- **Tailwind CSS**: https://tailwindcss.com/docs/customizing-colors
- **Shadcn/ui**: https://ui.shadcn.com/docs/theming
- **Streamlit Theming**: https://docs.streamlit.io/library/advanced-features/theming
- **WCAG AA**: https://www.w3.org/WAI/WCAG21/quickref/?currentsidebar=%23col_customize&levels=aaa

---

**Documento criado por @aios-master seguindo metodologia Alan Nicolas**
**Data**: 2024
**Versão**: 1.0.0
