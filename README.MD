# Projeto de Ranqueamento de Ações

Este projeto é uma aplicação desenvolvida em Python que utiliza o **Streamlit** para criar uma interface interativa de ranqueamento de ações. A aplicação permite que os usuários escolham ações, definam um período de tempo e visualizem uma comparação entre essas ações, gerando gráficos e tabelas que facilitam a análise de desempenho.

## Obtenção dos Dados

As ações analisadas foram obtidas manualmente a partir do site **InfoMoney**, utilizando a ferramenta de **Altas e Baixas** disponível em:

[https://www.infomoney.com.br/ferramentas/altas-e-baixas/](https://www.infomoney.com.br/ferramentas/altas-e-baixas/)

Essas ações foram coletadas do site conforme o arquivo `altas_e_baixas.csv` e registradas em um outro arquivo chamado `resultados.txt`, que é utilizado pela aplicação para realizar o comparativo entre elas.

## Funcionalidades

- **Seleção de Ações**: O usuário pode selecionar múltiplas ações para análise.
- **Período Personalizável**: O usuário define o ano e o mês de início e fim da análise.
- **Carregar Dados**: Após escolher as ações e o período, o usuário pode carregar os dados para gerar as análises.
- **Visualização de Tabelas**: Tabelas com os dados das variações de preços das ações selecionadas.
- **Gráfico de Linhas**: Mostra a variação do valor das ações ao longo do tempo.
- **Gráfico de Barras**: Exibe a pontuação que ranqueia as ações com base na melhor performance durante o período selecionado (quanto menor a pontuação, melhor o ranking).

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento do projeto.
- **Streamlit**: Framework para criação de aplicativos web interativos.
- **Bibliotecas**: 
  - `pandas` para manipulação de dados.
  - `yfinance` para obtenção dos dados financeiros.
  - `plotly.express` para criação dos gráficos.
  - `datetime` para manipulação de datas.

## Funcionalidades Futuras

- Implementação de novos indicadores financeiros.
- Integração com outras APIs de dados financeiros.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou fazer um pull request.