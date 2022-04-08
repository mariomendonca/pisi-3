import streamlit as st
import pandas as pd

from charts.histogram import histogram
from charts.percentage_chart import percentage_chart
from charts.edfc import edfc_function
from charts.boxplot_rating import boxplot
from charts.abandonment import abandonment

df = pd.read_csv('data/dados.csv')
df.drop('ISBN_13', inplace=True, axis=1)
df.drop('ISBN_10', inplace=True, axis=1)
df.drop('editora', inplace=True, axis=1)

option = st.sidebar.selectbox(
  'Escolha o grafico que deseja ver!',
  ('histograma', '% do sexo', 'edfc', 'boxplot', 'abandonos', 'dataset')
)

if (option == 'histograma'):
  st.write('Função para obter histograma de avaliações')
  histogram(df)
elif option == '% do sexo':
  st.write('Gráfico de % do sexo dos leitores')
  percentage_chart(df)
elif option == 'edfc':
  st.write('função de distribuição cumulativa empírica das avaliações')
  edfc_function(df)
elif option == 'boxplot':
  st.write('boxplot das avaliações')
  boxplot(df)
elif option == 'abandonos':
  st.write('Gráfico de quantidade de abandono de acordo com a quantidade de páginas')
  abandonment(df)
elif option == 'dataset':
  st.write('Dataset')
  st.dataframe(df)
