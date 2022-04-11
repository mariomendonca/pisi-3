from numpy import append
import streamlit as st
import pandas as pd

from charts.histogram import histogram
from charts.percentage_chart import percentage_chart
from charts.edfc import edfc_function
from charts.boxplot_rating import boxplot
from charts.abandonment import abandonment

df = pd.read_csv('data/dados.csv')

# removing not used columns 
to_drop = ['ISBN_13', 'ISBN_10', 'ano', 'resenha', 'editora']
df.drop(to_drop, inplace=True, axis=1)

# removing outliers and missing values
def remove_rating_outliers():
  df_count = df
  outliers = []
  for i in range(len(df)):
    if df_count['rating'][i] > 5:
      outliers.append(i)

  return df_count.drop(labels=outliers, axis=0)

def remove_pages_outliers():
  df_count = df
  outliers = []
  for i in range(len(df)):
    if df_count['paginas'][i] == 0:
      outliers.append(i)
  return df_count.drop(labels=outliers, axis=0)

def remove_sex_outliers():
  df_count = df
  outliers = []
  for i in range(len(df)):
    if (df_count['male'][i] + df_count['female'][i] ) != 100:
      if (df_count['lendo'][i] != 0) and (df_count['relendo'][i] != 0) and (df_count['leram'][i] != 0):
        outliers.append(i)
  return df_count.drop(labels=outliers, axis=0)

def remove_genre_missing_values():
  df_count = df
  outliers = []
  for i in range(len(df)):
    if (type(df_count['genero'][i]) == str):
      genre = df_count['genero'][i].replace(' ', '')
      if (len(genre) == 0):
        outliers.append(i)
  return df_count.drop(labels=outliers, axis=0)


def remove_values_outliers():
  df_count = df
  outliers = []
  for i in range(len(df)):
    if (type(df_count['genero'][i]) == float):
      outliers.append(i)

  return df_count.drop(labels=outliers, axis=0)

print(len(df['genero'][3194]))
df = remove_genre_missing_values()
print(len(df['genero'][3194]))
# print(len(df))

# df = remove_rating_outliers()
# df = remove_pages_outliers()

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
