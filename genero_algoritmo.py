import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer
import matplotlib.pyplot as plt
import random

df = pd.read_csv('data/dados.csv')
to_drop = ['ISBN_13', 'ISBN_10', 'ano', 'resenha', 'editora']
df.drop(to_drop, inplace=True, axis=1)
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
for i in newColumnsList:
  df[i] = 0
def populateNewColumns():
  for j in range(len(df)):
    existentIndex = df.index[j]
    for column in newColumnsList:
      if column.upper() in df['genero'][existentIndex].upper():
        df[column][existentIndex] = 1
populateNewColumns()
def testing():
  new_df = pd.DataFrame([], columns = ['titulo', 'genero', 'rating'])
  for i in range(len(df)):
    existentIndex = df.index[i]
    if (type(df['titulo'][existentIndex]) == str):
        for x in newColumnsList:
          if df[x][existentIndex] == 1: 
            # new_df = new_df.append({'titulo': df['titulo'][existentIndex], "rating": df['rating'][existentIndex], "genero": newColumnsList.index(x) + 1}, ignore_index=True)
            new_df = new_df.append({'titulo': int(existentIndex + 1), "rating": df['rating'][existentIndex], "genero": newColumnsList.index(x) + 1}, ignore_index=True)
  return new_df
new_df = testing()

col = new_df.drop('titulo', axis=1)
kmeans = KMeans(n_clusters = 4, 
init = 'k-means++', n_init = 10, 
max_iter = 300) 
pred_y = kmeans.fit_predict(col)

new_df['cluster_id'] = kmeans.labels_

st.dataframe(new_df)
st.dataframe(df)
plt.scatter(new_df['genero'], new_df['rating'], c = pred_y) #posicionamento dos eixos x e y
plt.xlim(0, 50) #range do eixo x
plt.ylim(0, 5) 
plt.scatter(kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,0], s = 70, c = 'red') #posição de cada centroide no gráfico
st.pyplot(plt)

cluster_zero = []
cluster_one = []
cluster_two = []
cluster_three = []

for i in range(len(new_df.values)):
  if new_df.values[i][3] == 0:
    cluster_zero.append(i)
  elif new_df.values[i][3] == 1:
    cluster_one.append(i)
  elif new_df.values[i][3] == 2:
    cluster_two.append(i)
  elif new_df.values[i][3] == 3:
    cluster_three.append(i)

def recomendation_per_id(bookId):
  book = new_df.values[bookId]
  cluster_id = book[3]
  
  if cluster_id == 0:
    random_list1 = random.sample(cluster_zero, 30)
    random_list2 = random.sample(cluster_one, 20)
    return random_list1 + random_list2
  
  elif cluster_id == 1: 
    random_list1 = random.sample(cluster_one, 30)
    random_list2 = random.sample(cluster_zero, 10)
    random_list3 = random.sample(cluster_two, 10)
    return random_list1 + random_list2 + random_list3
  
  elif cluster_id == 2:
    random_list1 = random.sample(cluster_two, 30)
    random_list2 = random.sample(cluster_one, 10)
    random_list3 = random.sample(cluster_three, 10)
    return random_list1 + random_list2 + random_list3
  elif cluster_id == 3:
    random_list1 = random.sample(cluster_three, 30)
    random_list2 = random.sample(cluster_two, 20)
    return random_list1 + random_list2

def returning_recomend_books(books_array):
  list_books = []
  for i in books_array:
    list_books.append(new_df.values[int(i)])
  return list_books


zero = recomendation_per_id(0)
two = recomendation_per_id(18)
three = recomendation_per_id(21)
one = recomendation_per_id(37)

st.write(returning_recomend_books(zero))
st.write(returning_recomend_books(one))
st.write(returning_recomend_books(two))
st.write(returning_recomend_books(three))

def returning_random_books():
  return random.sample(new_df.values, 50)

def newDataset():
  dataSet = pd.DataFrame([], columns = ['titulo', 'autor', 'descricao', 
  'rating', 'book_id', 'cluster_id' ])
  for i in range(len(new_df)):
    existentIndex = int(new_df['titulo'][i]) - 1
    dataSet = dataSet.append({'titulo': df['titulo'][existentIndex], 'autor': df['autor'][existentIndex],
    'descricao': df['descricao'][existentIndex], 'rating': df['rating'][existentIndex],'book_id': int(i),
    'cluster_id': new_df['cluster_id'][i]}
    , ignore_index=True)
  return dataSet
dataset = newDataset()
dataset.to_csv('newDados.csv')
