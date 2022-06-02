import streamlit as st
import pandas as pd

from charts.histogram import histogram
from charts.percentage_chart import percentage_chart
from charts.intersted_people import intersted_people
from charts.category_chart import category_chart
from charts.edfc import edfc_function
from charts.abandonment import abandonment
from charts.abandono_lendo import new_chart
from charts.leram_querem import new_chart2
from charts.romance_sex import romance_sex_percentage
from charts.economia_sex import economia_sex_percentage
from charts.box import box_chart
from charts.violin import violin_chart
from charts.strip_genre import strip_chart
from charts.strip_rating import strip_rating

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

df_without_genre_columns = df.copy()

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
    (
      'Dataset', 'Histograma de avaliações', 'box - rating', 'violin - rating', 'Porcentagem do Sexo', 'Sexo - Romance', 'Sexo - Economia', 'Abandono - querem ler', 
      'Querem ler - leram', 'Strip chart genero - querem ler', 'Strip chart genero - rating'
    )
)

if option == 'Histograma de avaliações':
  st.write('**O histograma é um gráfico que demonstra uma distribuição de frequências.**')
  st.write('Neste exemplo, temos um histograma de avaliações, onde é possivel notar que o maior número de avaliações é nota 4')
  histogram(df)
elif option == 'box - rating':
  st.write('Box - Rating')
  box_chart(df)
elif option == 'violin - rating':
  st.write('Violino - Rating')
  violin_chart(df)
elif option == 'Porcentagem do Sexo':
  st.write('**Gráfico de porcentagem do Sexo dos leitores.**')
  st.write('Neste gráfico é possivel notar que a quantidade de mulheres leitoras é bem maior que de homens')
  percentage_chart(df)
elif option == 'Sexo - Romance':
  st.write('**Gráfico de porcentagem do Sexo dos leitores do genero romance.**')
  st.write('Neste gráfico é possivel notar que a diferença entre homens e mulheres é ainda maior no gênero romance')
  romance_sex_percentage(df)
elif option == 'Sexo - Economia':
  st.write('**Gráfico de porcentagem do Sexo dos leitores do genero romance.**')
  st.write('Já no gênero de economia está quase igualado')
  economia_sex_percentage(df)
elif option == 'Abandono - querem ler':
  st.write('**Gráfico de relação entre abandonos x lendo.**')
  st.write('Neste gráfico é possivel notar que quanto mais abandonos em um livre, menos pessoas querem ler')
  new_chart(df)
elif option == 'Querem ler - leram':
  st.write('**Gráfico de relação entre Pessoas que querem ler x Pessoas que estão lendo.**')
  st.write('Neste gráfico mostra que a relação entre pessoas que querem ler e pessoas que já leram não tem interfere um no outro')
  new_chart2(df)
elif option == 'Dataset':
  st.write('Dataset')
  st.dataframe(df_without_genre_columns)
elif option == 'Strip chart genero - querem ler':
  st.write('Strip chart genero - querem ler')
  strip_chart(df)
elif option == 'Strip chart genero - rating':
  st.write('Strip chart genero - rating')
  strip_rating(df)
