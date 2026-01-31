# DESIGN_SYSTEM.md - Calculadora de Arbitragem

## 1. Design Tokens (Quarks)

### Cores (Paleta Semântica)

* **Primary (Brand):** #2ECC71 (Verde Sucesso - Para áreas de lucro)
* **Secondary:** #3498DB (Azul Ação - Para botões e links)
* **Danger:** #E74C3C (Vermelho Alerta - Para prejuízo/arbitragem negativa)
* **Neutral:**
* #121212 (Background Dark)
* #1E1E1E (Surface/Cards)
* #FFFFFF (Texto Primário)
* #B3B3B3 (Texto Secundário)

### Tipografia

* **Family:** Inter, system-ui, sans-serif
* **Sizes:**
* Display: 32px (Bold)
* Heading: 24px (Semi-bold)
* Body: 16px (Regular)
* Caption: 12px (Light)

---

## 2. Atoms (Átomos)

* **Inputs:** Campos numéricos com bordas arredondadas (8px) e foco em #3498DB.
* **Labels:** Texto em #B3B3B3 acima de cada input.
* **Buttons:** 
* Primary: Background verde, texto branco.
* Ghost: Borda azul, sem preenchimento.

* **Badges:** Etiquetas pequenas para indicar 'Lucro' ou 'Prejuízo'.

---

## 3. Molecules (Moléculas)

* **Input Group:** Label + Input + Mensagem de erro (se houver).
* **Odd Card:** Um container pequeno exibindo a Odd e o nome da Casa de Aposta.
* **Profit Indicator:** Valor do lucro em destaque com cor condicional (Verde se positivo, Vermelho se negativo).

---

## 4. Organisms (Organismos)

* **Calculator Form:** O agrupamento de todos os inputs de Odds e Stake no pp.py.
* **Result Panel:** Painel lateral ou inferior que resume a distribuição da aposta e a margem de arbitragem.
* **History Table:** Tabela Streamlit formatada para listar cálculos anteriores.

---

## 5. Templates (Modelos)

* **Single View:** Layout de coluna única focado em dispositivos móveis (Mobile First).
* **Dashboard View:** Layout em duas colunas (Inputs à esquerda, Resultados e Gráficos à direita).

---

## 6. Implementation (Streamlit Config)

Para aplicar esses tokens no pp.py, utilizaremos o arquivo .streamlit/config.toml:

\\\	oml
[theme]
primaryColor = '#2ECC71'
backgroundColor = '#121212'
secondaryBackgroundColor = '#1E1E1E'
textColor = '#FFFFFF'
font = 'sans serif'
\\\

---

### Próximas Tarefas:

* [ ] Criar a pasta .streamlit e o arquivo config.toml.
* [ ] Refatorar os componentes de pp.py para seguir a hierarquia de cores do Design System.
* [ ] Implementar a lógica de cores condicionais nos resultados (Verde/Vermelho).
