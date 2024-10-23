import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime

def obter_cotacoes(data_referencia, codigos_acoes):
    # lista para armazenar os DataFrames
    lista_dfs=[]
    for codigo in codigos_acoes:
        # baixar cotações usando yfinance
        df = yf.download(codigo, start=data_referencia).reset_index()
        df['codigo_acao'] = codigo
        df=df[['Date','codigo_acao','Adj Close']]
        lista_dfs.append(df)
    df = pd.concat(lista_dfs,ignore_index=True)
    return df.sort_values(by='codigo_acao', ascending=True).reset_index(drop=True)

def obter_indicadores_fundamentalistas(codigos_acoes):
  # lista para armazenar os indicadores fundamentalistas de cada ação
  lista_indicadores = []

  for codigo in codigos_acoes:
    # baixar dados fundamentalistas usando yfinance
    acao = yf.Ticker(codigo)
    info = acao.info

    # Obter lucros históricos para calcular o CAGR
    lucros_historicos = acao.history(period='5y')['Close']
    
    # Verificar se lucros_historicos não está vazio
    if len(lucros_historicos) > 1:
      cagr = (lucros_historicos.iloc[-1] / lucros_historicos.iloc[0])**(1/5) - 1
    else:
      cagr = None

    # criar dicionário com os principais indicadores
    indicadores = {
      'codigo_acao': codigo,
      'setor': info.get('sector'),
      'Indústria': info.get('industry'),
      'Beta': info.get('beta'),
      'Valor De Mercado': info.get('marketCap'),
      'P/L': info.get('trailingPE'),
      'P/VP': info.get('priceToBook'),
      'Dividend Yield (%)': info.get('dividendYield') * 100 if info.get('dividendYield') else None,
      'Margem Bruta (%)': info.get('grossMargins') * 100 if info.get('grossMargins') else None,
      'Margem Operacional (%)': info.get('operatingMargins') * 100 if info.get('operatingMargins') else None,
      'Margem Líquida (%)': info.get('profitMargins') * 100 if info.get('profitMargins') else None,
      'ROE (%)': info.get('returnOnEquity') * 100 if info.get('returnOnEquity') else None,
      'ROA (%)': info.get('returnOnAssets') * 100 if info.get('returnOnAssets') else None,
      'Divida Bruta/ Patrimonio': info.get('debtToEquity'),
      'Crescimento Receita (%)': info.get('revenueGrowth') * 100 if info.get('revenueGrowth') else None,
      'CAGR do Lucro (%)': cagr * 100 if cagr else None,
    }

    lista_indicadores.append(indicadores)

  # converter lista de dicionários em DataFrame
  df_indicadores = pd.DataFrame(lista_indicadores)
  return df_indicadores.sort_values(by='codigo_acao', ascending=True).reset_index(drop=True)

def ranking(df):
  colunas_selecionadas = ['codigo_acao', 'setor', 'P/L', 'P/VP', 'Divida Bruta/ Patrimonio','ROE (%)','CAGR do Lucro (%)','Dividend Yield (%)']
  df_selecionado = df[colunas_selecionadas]

  # Ordenar por P/L
  pl_ranking = df_selecionado[['codigo_acao', 'P/L']].sort_values(by='P/L', ascending=True).reset_index(drop=True)
  pl_ranking['rank_pl'] = pl_ranking['P/L'].rank(ascending=True, method='min', na_option='bottom')

  # Ordenar por P/VP
  pvp_ranking = df_selecionado[['codigo_acao', 'P/VP']].sort_values(by='P/VP', ascending=True).reset_index(drop=True)
  pvp_ranking['rank_pvp'] = pvp_ranking['P/VP'].rank(ascending=True, method='min', na_option='bottom')

  # Ordenar por Divida Bruta/ Patrimonio
  divida_ranking = df_selecionado[['codigo_acao', 'Divida Bruta/ Patrimonio']].sort_values(by='Divida Bruta/ Patrimonio', ascending=True).reset_index(drop=True)
  divida_ranking['rank_divida'] = divida_ranking['Divida Bruta/ Patrimonio'].rank(ascending=True, method='min', na_option='bottom')

  # Ordenar por ROE (%)
  roe_ranking = df_selecionado[['codigo_acao', 'ROE (%)']].sort_values(by='ROE (%)', ascending=False).reset_index(drop=True)  # Maior ROE é melhor, então ascending=False
  roe_ranking['rank_roe'] = roe_ranking['ROE (%)'].rank(ascending=False, method='min', na_option='bottom')

  # Ordenar por CAGR do Lucro (%)
  cagr_ranking = df_selecionado[['codigo_acao', 'CAGR do Lucro (%)']].sort_values(by='CAGR do Lucro (%)', ascending=False).reset_index(drop=True)  # Maior CAGR é melhor
  cagr_ranking['rank_cagr'] = cagr_ranking['CAGR do Lucro (%)'].rank(ascending=False, method='min', na_option='bottom')

  # Ordenar por Dividend Yield (%)
  dividend_ranking = df_selecionado[['codigo_acao', 'Dividend Yield (%)']].sort_values(by='Dividend Yield (%)', ascending=False).reset_index(drop=True)  # Maior Dividend Yield é melhor
  dividend_ranking['rank_dividend'] = dividend_ranking['Dividend Yield (%)'].rank(ascending=False, method='min', na_option='bottom')

  # Agora fazemos o merge para juntar os rankings corretamente com base na 'codigo_acao'
  df_ranking_geral = pl_ranking[['codigo_acao', 'rank_pl']].merge(
      pvp_ranking[['codigo_acao', 'rank_pvp']], on='codigo_acao').merge(
      divida_ranking[['codigo_acao', 'rank_divida']], on='codigo_acao').merge(
      roe_ranking[['codigo_acao', 'rank_roe']], on='codigo_acao').merge(
      cagr_ranking[['codigo_acao', 'rank_cagr']], on='codigo_acao').merge(
      dividend_ranking[['codigo_acao', 'rank_dividend']], on='codigo_acao')

  # Somar todas as pontuações de ranking para obter uma pontuação geral
  df_ranking_geral['pontuacao_total'] = df_ranking_geral[['rank_pl', 'rank_pvp', 'rank_divida', 'rank_roe', 'rank_cagr','rank_dividend']].sum(axis=1)

  # Ordenar as ações com base na pontuação total (quanto menor a pontuação, melhor a classificação geral)
  df_ranking_final = df_ranking_geral.sort_values(by='codigo_acao', ascending=True).reset_index(drop=True)

  # Exibir o ranking final
  return df_ranking_final


# título do dashboard
st.title('Ranqueamento de Ações')

# Lendo o arquivo resultado.txt
with open('resultado.txt', 'r') as file:
    options = eval(file.read())

# input para seleção dos dados
codigos_acoes = st.multiselect(
    'Selecione as ações:',
    options=options,
    default=['MSFT34.SA']
)

# input para seleção do período
ano_inicio = st.selectbox('Ano de início:', options = range(2000,datetime.now().year+1), index=22)
mes_inicio = st.selectbox('Mês de início:', options = range(1,13), index=0)
ano_fim = st.selectbox('Ano de fim:', options = range(2000,datetime.now().year+1), index=datetime.now().year-2000)
mes_fim = st.selectbox('Mês de fim:', options = range(1,13), index=datetime.now().month-1)

#criar as datas de início e fim a partir dos inputs do usuário
data_inicio = datetime(ano_inicio, mes_inicio, 1).strftime('%Y-%m-%d')
data_fim = datetime(ano_fim, mes_fim, 1).strftime('%Y-%m-%d')

# Botão para carregar os dados
bt_carregar = st.button('Carregar Dados')
if bt_carregar:
    # Baixar cotações das ações
    st.header('Tabelas:')
    st.subheader('Cotações diárias')
    cotacoes = obter_cotacoes(data_inicio, codigos_acoes)
    st.dataframe(cotacoes)

    # Obter indicadores fundamentalistas
    st.subheader('Indicadores Fundamentalistas')
    indicadores = obter_indicadores_fundamentalistas(codigos_acoes)
    st.dataframe(indicadores)

    # Ranking final
    st.subheader('Ranking Fundamentalista')
    ranking_final = ranking(indicadores)
    st.dataframe(ranking_final)

    st.header('Gráficos:')
    # Exibir gráfico de cotações
    fig_line = px.line(cotacoes.pivot(index='Date', columns='codigo_acao', values='Adj Close'),
                       labels={"value": "Preço de Fechamento", "Date": "Data", "codigo_acao": "Código da Ação"},
                       color='codigo_acao',
                       title='Variação das Ações')
    st.plotly_chart(fig_line)

    # Exibir gráfico de ranking
    fig_bar = px.bar(ranking_final, 
                     x='codigo_acao', 
                     y='pontuacao_total', 
                     color='codigo_acao',
                     labels={"pontuacao_total": "Pontuação Total", "codigo_acao": "Código da Ação"},
                     title='Ranking das Ações')
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar)
    st.caption('(quanto menor a pontuação, melhor o ranking)')

st.markdown("---")
st.markdown(
    """
    <div style='text-align: center;'>
        © Copyright 2025 | Developed by 
        <a href='https://github.com/EduAugustoM' target='_blank'>
            Eduardo Augusto
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)