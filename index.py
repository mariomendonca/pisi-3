import streamlit as st
import pandas as pd

from charts.histogram import histogram
from charts.percentage_chart import percentage_chart
from charts.intersted_people import intersted_people
from charts.edfc import edfc_function
from charts.abandonment import abandonment

df = pd.read_csv('data/dados.csv')

# Removing not used columns
to_drop = ['ISBN_13', 'ISBN_10', 'ano', 'resenha', 'editora']
df.drop(to_drop, inplace=True, axis=1)

# Removing outliers and missing values
def remove_outliers():
  outliers = []
  data = df.values
  for i in range(len(data)):
    # Rating
    if data[i][4] > 5:
        outliers.append(i)
    # Pages
    elif data[i][2] == 0:
        outliers.append(i)
    # Sex
    elif data[i][13] + data[i][14] != 100:
      if data[i][7] != 0 and data[i][9] != 0 and data[i][10]:
        outliers.append(i)
        # Genre
    elif type(data[i][12]) == float:
      outliers.append(i)
        # Description
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
df = df.dropna()
df = df.drop_duplicates()

# Transformação
newColumnsList = [
    'Economia', 'Finanças ', 'Literatura Brasileira', 'Não-ficção ', 'Drama ', 'Ficção',
    'Literatura Estrangeira', 'Suspense e Mistério', 'Ficção', 'Ficção científica',
    'Biografia', 'Autobiografia', 'Memórias', 'História', 'Política', 'HQ', 'comics', 'mangá',
    'Autoajuda', 'História Geral', 'Infantil', 'Literatura Estrangeira', 'Negócios', 'Empreendedorismo',
    'Jovem adulto', 'Fantasia', 'Horror', 'Terror', 'Aventura', 'Jogos',
    'Crime', 'Romance policial', 'Romance', 'Matemática', 'Medicina', 'Saúde', 'Romance', 'Infantojuvenil', 'Humor', 'Comédia', 'Autoajuda', 'Infantil ', 'Biologia', 'Fantasia',
    'Psicologia', 'Jovem adulto', 'LGBT', 'GLS', 'Biografia' 'Autobiografia', 'Memórias', 'Distopia ', 'História ', 'Chick-lit ', 'Literatura Brasileira',
    'Literatura Estrangeira', 'Religião', 'Espiritualidade', 'Jogos', 'Entretenimento ', 'Crime '
]

newColumnsList = list(dict.fromkeys(newColumnsList))

# Creating new columns
for i in newColumnsList:
  df[i] = 0


def populateNewColumns():
  for j in range(len(df)):
    existentIndex = df.index[j]
    for column in newColumnsList:
      if column.upper() in df['genero'][existentIndex].upper():
        df[column][existentIndex] = 1

populateNewColumns()

option = st.sidebar.selectbox(
    'Escolha o grafico que deseja ver!',
    ('Dataset', 'Histograma', 'Porcentagem do Sexo', 'Gráfico EDFC', 'Abandonos', 'Índice de pessoas interessadas - Histograma')
)

if (option == 'Histograma'):
  st.write('Função para obter histograma de avaliações')
  histogram(df)
elif option == 'Porcentagem do Sexo':
  st.write('Gráfico de porcentagem do Sexo dos leitores')
  percentage_chart(df)
elif option == 'Gráfico EDFC':
  st.write('função de distribuição cumulativa empírica das avaliações')
  edfc_function(df)
elif option == 'Índice de pessoas interessadas - Histograma':
  st.write('Relação entre o índice de pessoas interessadas e pessoas que terminaram a leitura de um livro + as que o abandonaram.')
  intersted_people(df)
elif option == 'Abandonos':
  st.write('Gráfico de quantidade de abandono de acordo com a quantidade de páginas')
  abandonment(df)
elif option == 'Dataset':
  st.write('Dataset')
  st.dataframe(df)
