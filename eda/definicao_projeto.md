# Projeto de Análise Exploratória de Dados (EDA)

## 1. Introdução

A Análise Exploratória de Dados (EDA) é uma etapa fundamental no processo de Ciência de Dados, pois permite compreender a estrutura, os padrões e as relações presentes em um conjunto de dados antes da construção de modelos ou da geração de conclusões mais profundas.

Neste projeto, será utilizado o **Brazilian Cities Dataset**, uma base de dados que reúne informações socioeconômicas, demográficas e estruturais dos municípios brasileiros.

O objetivo desta etapa é definir o problema, compreender o contexto dos dados e estabelecer perguntas que orientarão as análises futuras.

---

## 2. Dataset escolhido

O dataset utilizado neste projeto é o **Brazilian Cities Dataset**, que contém informações sobre milhares de municípios do Brasil.

### Principais características do dataset:

- Dados populacionais (ex: `IBGE_RES_POP`, `ESTIMATED_POP`);
- Indicadores econômicos (ex: `GDP`, `GDP_CAPITA`);
- Indicadores de desenvolvimento humano (ex: `IDHM`, `IDHM_Educacao`, `IDHM_Renda`);
- Informações de infraestrutura (ex: `HOTELS`, `BEDS`, `Cars`, `Motorcycles`);
- Informações territoriais (ex: `AREA`);
- Classificação territorial (`RURAL_URBAN`);
- Serviços disponíveis (ex: `POST_OFFICES`, `UBER`, `WAL-MART`).

### Justificativa da escolha

A escolha desse dataset se justifica por:

- ser uma base real e pública;
- possuir grande variedade de variáveis;
- permitir análises multidimensionais (econômicas, sociais e estruturais);
- ser adequada para fins didáticos e introdutórios em Ciência de Dados.

---

## 3. Problema de análise

O problema central deste projeto é:

> **Como características socioeconômicas e estruturais influenciam o desenvolvimento dos municípios brasileiros?**

Essa questão permite explorar relações entre variáveis como:

- população;
- PIB;
- renda per capita;
- infraestrutura;
- desenvolvimento humano.

---

## 4. Objetivo geral

Investigar padrões e relações entre indicadores socioeconômicos dos municípios brasileiros, com foco na compreensão dos fatores associados ao desenvolvimento humano.

---

## 5. Objetivos específicos

- Analisar a distribuição de indicadores como IDHM, GDP e população;
- Verificar diferenças entre municípios de diferentes portes populacionais;
- Identificar padrões regionais (por estado);
- Avaliar possíveis relações entre renda (GDP_CAPITA) e desenvolvimento humano (IDHM);
- Explorar a influência da infraestrutura (ex: hotéis, veículos) no desenvolvimento.

---

## 6. Perguntas norteadoras

As seguintes perguntas orientarão a análise exploratória:

### Sobre desenvolvimento humano
- Municípios com maior GDP_CAPITA possuem maior IDHM?
- Existe variação significativa de IDHM entre estados?

### Sobre economia
- Quais estados apresentam maior PIB médio?
- Municípios mais populosos possuem maior GDP?

### Sobre infraestrutura
- Municípios com mais infraestrutura (ex: hotéis, veículos) apresentam melhores indicadores socioeconômicos?
- Existe relação entre número de veículos e desenvolvimento econômico?

### Sobre distribuição populacional
- Como a população está distribuída entre os municípios?
- Municípios maiores apresentam padrões diferentes dos menores?

---

## 7. Hipóteses iniciais

Com base no conhecimento prévio, algumas hipóteses podem ser formuladas:

- Municípios com maior renda per capita tendem a apresentar maior IDHM;
- Capitais tendem a ter melhores indicadores socioeconômicos;
- Estados mais desenvolvidos economicamente apresentam melhores médias de IDHM;
- Municípios mais populosos possuem maior PIB absoluto.

Essas hipóteses serão verificadas ao longo da análise.

---

## 8. Importância da análise

A análise desses dados é relevante porque permite compreender desigualdades regionais, padrões de desenvolvimento e possíveis relações entre fatores econômicos e sociais.

Além disso, o projeto contribui para o desenvolvimento de habilidades fundamentais em Ciência de Dados, como:

- interpretação de dados;
- formulação de hipóteses;
- análise crítica;
- comunicação de resultados.

---

## 9. Próximos passos

Na próxima etapa do projeto, será realizada a análise exploratória de dados (EDA), incluindo:

- limpeza aprofundada dos dados;
- criação de visualizações;
- identificação de padrões e correlações;
- geração de insights.

Essa etapa permitirá responder às perguntas norteadoras definidas neste documento.