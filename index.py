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
def remove_outliers():
  outliers = []
  data = df.values
  for i in range(len(data)):
    # rating
    if data[i][4] > 5:
      outliers.append(i)
    
    # pages
    elif data[i][2] == 0:
      outliers.append(i)
    
    # sex
    elif data[i][13] + data[i][14] != 100:
      if data[i][7] != 0 and data[i][9] != 0 and data[i][10]:
        outliers.append(i) 
    
    # genre
    elif type(data[i][12]) == float:
      outliers.append(i) 
    
    # description
    elif type(data[i][11]) == float:
      outliers.append(i) 
  return outliers

def remove_missing_values():
  missing_values = []
  data = df.values
  for i in range(len(data)):
    if (type(data[i][12]) == str):
      genre = data[i][12].replace(' ', '')
      if (len(genre) == 0):
        missing_values.append(i)
  return missing_values

outliersList = remove_outliers()
missing_valuesList = remove_missing_values()
dropList = outliersList + missing_valuesList
dropList = list(dict.fromkeys(dropList))
df = df.drop(labels=dropList, axis=0)

option = st.sidebar.selectbox(
  'Escolha o grafico que deseja ver!',
  ('dataset', 'histograma', '% do sexo', 'edfc', 'boxplot', 'abandonos')
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
