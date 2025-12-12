# Projeto: Análise do Dólar (PTAX) - Banco Central do Brasil

Este projeto é um estudo de engenharia de dados usando Python e Jupyter Notebook para consumir a API pública do Banco Central (PTAX) e organizar os dados em camadas:

- **Bronze**: dados crus vindos da API, salvos em `data/bronze`.
- **Silver**: dados limpos e tipados, salvos em `data/silver`.
- **Gold**: dados agregados por dia (médias, mínimas, máximas), salvos em `data/gold`.

## Tecnologias usadas

- Python
- Jupyter Notebook
- Pandas
- Requests
- Matplotlib

## Fluxo de dados

1. Consumo da API de cotações do dólar (PTAX) do Banco Central.
2. Armazenamento dos dados crus em CSV (camada Bronze).
3. Limpeza e criação de coluna de data (camada Silver).
4. Agregação por dia e cálculo de métricas (camada Gold).
5. Geração de gráfico de série temporal com a média diária de venda.

## Objetivo

Este projeto foi feito para fins de aprendizado e portfólio, simulando um fluxo de engenharia de dados semelhante a pipelines em nuvem (como Azure + Databricks), usando camadas Bronze, Silver e Gold.