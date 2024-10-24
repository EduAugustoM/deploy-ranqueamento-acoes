![Gráfico das cotações](https://raw.githubusercontent.com/EduAugustoM/user-images/refs/heads/main/graficos-cotacoes.png?token=GHSAT0AAAAAACYJXAH62YPHMCM2ZOE6T75QZY2K45Q)

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

## Funcionamento do Ranking de Ações

Este sistema de ranking foi desenvolvido para ajudar na seleção das melhores ações com base em indicadores fundamentalistas. Os principais indicadores utilizados para a avaliação são:

- **P/L (Preço sobre Lucro)**
- **P/VP (Preço sobre Valor Patrimonial)**
- **Divida Bruta sobre Patrimônio**
- **ROE (Return on Equity)**
- **CAGR do Lucro (Taxa de Crescimento Anual Composta do Lucro)**
- **Dividend Yeld (Taxa de Rentabilidade dos Dividendos)**

### Como Funciona o Ranking

1. **Seleção dos Indicadores**
   - O sistema coleta os indicadores fundamentalistas das ações selecionadas pelo usuário.

2. **Ranking por Indicadores**
   - Cada indicador é avaliado separadamente. Para cada um deles, as ações são classificadas em ordem crescente, onde a ação com o menor valor recebe a melhor posição:
     - O menor P/L recebe a posição 1.
     - O menor P/VP recebe a posição 1.
     - A menor Divida Bruta sobre Patrimônio recebe a posição 1.
     - O maior ROE recebe a posição 1.
     - O maior CAGR recebe a posição 1.
     - O maior Dividend Yeld recebe a posição 1.

3. **Pontuação**
   - Para cada ação, a pontuação é atribuída com base na sua posição em cada um dos rankings. A ação que ocupa a 1ª posição em um indicador recebe 1 pontos, a 2ª posição recebe 2 pontos, e assim por diante, até a 6ª posição, que recebe 6 pontos.
   - A pontuação total de cada ação é a soma das pontuações obtidas em cada um dos rankings.

4. **Ranking Geral**
   - No ranking geral, as ações são classificadas com base na pontuação total.
   - A ação com a menor pontuação total é considerada a melhor escolha, pois indica que essa ação apresenta os melhores indicadores em relação às demais.

## Funcionalidades Futuras

- Implementação de novos indicadores financeiros.
- Integração com outras APIs de dados financeiros.

## Conclusão
Esse sistema de ranking fornece uma visão clara sobre as melhores opções de investimento com base em indicadores fundamentais, facilitando a tomada de decisão na escolha das ações mais promissoras. 

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou fazer um pull request.

---

<div style='text-align: center;'> 
        <a href='https://web-production-e47d0.up.railway.app/' target='_blank'>
            Ranqueamento de Ações
        </a>
  </div>
