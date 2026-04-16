# Curso Introdutório de Python para Ciência de Dados

## Equipe C

| Nome | Matrícula |
|------|-----------|
| Camila Martins | 2310286 |
| Ricardo Temporal | 2310292 |
| Alvaro Araujo | 2510552 |

**Disciplina:** Ciência de Dados  
**Professor:** Rilder de Sousa Pires  
**Instituição:** Universidade de Fortaleza (UNIFOR)  
**Semestre:** 2026.1

---

## Sobre o projeto

Este repositório é o material completo do curso introdutório de Python para Ciência de Dados, desenvolvido como **atividade extensionista** da disciplina T326.

O curso foi planejado para democratizar o acesso ao conhecimento em programação e análise de dados, voltado a estudantes do ensino médio, técnico ou superior, profissionais em transição de carreira e qualquer pessoa interessada em começar na área.

---

## Objetivo do curso

Ao final do curso, o participante será capaz de:

- Escrever programas simples em Python
- Carregar, limpar e manipular dados com Pandas
- Criar visualizações informativas com Matplotlib e Seaborn
- Conduzir uma análise exploratória de dados (EDA) do início ao fim
- Gerar insights a partir de dados reais e comunicá-los com clareza

---

## Público-alvo

- Estudantes do ensino médio, técnico ou superior
- Profissionais em transição de carreira
- Pessoas que desejam iniciar na área de Ciência de Dados
- Nenhum conhecimento prévio de programação é necessário

---

## Estrutura do repositório

```
ciencia-dados-extensao/
│
├── README.md                    ← Este arquivo
│
├── datasets/
│   ├── README.md                ← Dicionário de dados do Brazilian Cities
│   └── brazilian_cities.csv     ← Dataset principal (módulos 1-3)
│
├── eda/
│   ├── README.md                ← Descrição do dataset ADH e perguntas norteadoras
│   ├── indices_adh_municipio.csv       ← Indicadores ADH por município e ano
│   └── identificador_municipios.csv   ← Nomes e estados dos municípios
│
├── ementa/
│   └── Escopo e pré-requisitos.pdf    ← Ementa detalhada do curso
│
├── modulo-1/
│   ├── slides/
│   │   └── Módulo 1 - Introdução e Conceitos Fundamentais de Python.pdf
│   ├── notebooks/
│   │   └── Módulo 1 - Introdução e Conceitos Fundamentais de Python.ipynb
│   └── exercicios/
│       └── Exercícios - Módulo 1 - Gabarito.ipynb
│
├── modulo-2/
│   ├── slides/
│   │   └── Módulo 2 - Manipulação de Dados com Pandas.pdf
│   ├── notebooks/
│   │   └── Módulo 2 - Manipulação de Dados com Pandas.ipynb
│   └── exercicios/
│       └── Exercícios - Módulo 2 - Gabarito.ipynb
│
├── modulo-3/
│   ├── notebooks/
│   │   └── Módulo 3 - Visualização de Dados e Storytelling.ipynb
│   └── exercicios/
│       └── Exercícios - Módulo 3 - Gabarito.ipynb
│
├── modulo-4/
│   ├── notebooks/
│   │   └── Módulo 4 - Análise Exploratória de Dados (EDA).ipynb
│   └── exercicios/
│       └── Exercícios - Módulo 4 - Gabarito.ipynb
│
└── projeto-final/
    └── notebooks/
        └── Projeto Final - Análise do Desenvolvimento Humano nos Municípios Brasileiros.ipynb
```

---

## Conteúdo dos módulos

### Módulo 1 — Fundamentos de Python
- Primeiro contato com Python: `print()`, variáveis e tipos de dados
- Estruturas condicionais: `if`, `elif`, `else`
- Estruturas de repetição: `for`, `while`
- Estruturas de dados: listas, dicionários, tuplas
- Funções: definição, parâmetros e retorno
- Boas práticas de programação
- **Dataset de exemplo:** dados simples para prática

### Módulo 2 — Manipulação de Dados com Pandas
- Estruturas fundamentais: Series e DataFrame
- Leitura de dados: CSV, Excel, JSON
- Exploração inicial: `head()`, `info()`, `describe()`
- Identificação e tratamento de valores ausentes
- Remoção de duplicatas
- Filtros e seleção de dados com `.loc` e `.iloc`
- Agrupamentos com `groupby()`
- Criação e transformação de colunas
- Estatística descritiva básica
- **Dataset:** Brazilian Cities (municípios brasileiros)

### Módulo 3 — Visualização de Dados
- Por que visualizar dados? Comunicação vs decoração
- Tipos de gráfico e quando usar cada um
- **Matplotlib:** estrutura de um gráfico, linha, barras, histograma
- **Seaborn:** boxplot, scatterplot, heatmap de correlação
- Boas práticas: títulos, eixos, cores com propósito
- Exemplos didáticos progressivos (simples → dataset real)
- **Dataset:** Brazilian Cities

### Módulo 4 — Análise Exploratória de Dados (EDA)
- O que é EDA e por que fazer antes de qualquer análise
- Formulação de problema e perguntas norteadoras
- Limpeza e preparação de dados
- Estatística descritiva e distribuições
- Correlações e heatmap
- Comparações entre grupos e regiões
- Storytelling com dados
- Conclusões e geração de insights
- **Dataset:** Atlas do Desenvolvimento Humano (ADH) — municípios brasileiros 1991-2010

### Projeto Final
- Análise completa do desenvolvimento humano nos municípios brasileiros
- 5 perguntas de negócio respondidas com dados e visualizações
- Insights acionáveis e narrativa estruturada
- **Dataset:** Atlas ADH (mesmos dados do Módulo 4)

---

## Como executar os notebooks

### Opção 1: Google Colab (recomendada para iniciantes)

1. Acesse [colab.research.google.com](https://colab.research.google.com)
2. Clique em **Arquivo → Abrir notebook → GitHub**
3. Cole o endereço deste repositório
4. Selecione o notebook desejado

> **Importante:** No Colab, você precisará fazer upload do dataset manualmente ou montar o Google Drive. Instruções estão no início de cada notebook.

### Opção 2: Jupyter Notebook local

**Passo 1:** Clone o repositório

```bash
git clone https://github.com/camilampinheiro/ciencia-dados-extensao
cd ciencia-dados-extensao
```

**Passo 2:** Instale as dependências

```bash
pip install pandas matplotlib seaborn numpy jupyter
```

**Passo 3:** Inicie o Jupyter

```bash
jupyter notebook
```

**Passo 4:** Navegue até o notebook desejado e execute as células em ordem (de cima para baixo)

> **Por que em ordem?** Os notebooks são progressivos: células posteriores dependem de variáveis criadas nas anteriores. Executar fora de ordem pode causar erros como `NameError`.

---

## Tecnologias utilizadas

| Tecnologia | Versão recomendada | Uso |
|---|---|---|
| Python | 3.10+ | Linguagem principal |
| Pandas | 2.0+ | Manipulação de dados |
| Matplotlib | 3.7+ | Gráficos base |
| Seaborn | 0.12+ | Gráficos estatísticos |
| NumPy | 1.24+ | Cálculos numéricos |
| Jupyter Notebook / Google Colab | — | Ambiente interativo |

---

## Datasets

### Brazilian Cities (`datasets/brazilian_cities.csv`)
- **Fonte:** [Kaggle — Cristiana Parada](https://www.kaggle.com/datasets/crisparada/brazilian-cities/data)
- **Conteúdo:** 5.570 municípios brasileiros com ~79 variáveis (economia, demografia, infraestrutura, turismo)
- **Uso:** Módulos 2 e 3

### Atlas do Desenvolvimento Humano (`eda/`)
- **Fonte:** [Atlas Brasil / Base dos Dados](https://basedosdados.org/dataset/cbfc7253-089b-44e2-8825-755e1419efc8)
- **Conteúdo:** Indicadores socioeconômicos de todos os municípios brasileiros em 1991, 2000 e 2010
- **Uso:** Módulo 4 e Projeto Final

Consulte os arquivos `README.md` dentro das pastas `datasets/` e `eda/` para ver o dicionário completo de variáveis.

---

## Ordem de estudo recomendada

```
Módulo 1 → Módulo 2 → Módulo 3 → Módulo 4 → Projeto Final
```

Cada módulo tem um notebook de conteúdo e um gabarito de exercícios. Sugerimos tentar os exercícios antes de consultar o gabarito.

---

Projeto educacional desenvolvido como atividade extensionista — UNIFOR 2026.1
