import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer
import matplotlib.pyplot as plt

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
st.dataframe(new_df)


# X = new_df['genero']
# y = new_df['rating']
# df.drop(to_drop, inplace=True, axis=1)

col = new_df.drop('titulo', axis=1)

# km = KMeans(n_clusters=3, random_state=42)
# km.fit_predict(col)
# score = silhouette_score(col, km.labels_, metric='euclidean')
# st.write('Silhouetter Score: %.3f' % score)
# print('Silhouetter Score: %.3f' % score)
# st.dataframe(col)
# fig, ax = plt.subplots(2, 2, figsize=(15,8))
# for i in [2, 3, 4, 5]:
#     km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=42)
#     q, mod = divmod(i, 2)
#     visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q-1][mod])
#     visualizer.fit(col)
#     st.pyplot(plt)
    

fig, ax = plt.subplots(2, 2, figsize=(15,8))
km = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=100, random_state=42)
# q, mod = divmod(4, 2)


plt.scatter(new_df['genero'], new_df['rating'])
plt.xlim(0, 50) #range do eixo x
plt.ylim(0, 5) #range do eixo y
st.pyplot(plt)

kmeans = KMeans(n_clusters = 4, #numero de clusters
init = 'k-means++', n_init = 10, #algoritmo que define a posição dos clusters de maneira mais assertiva
max_iter = 300) #numero máximo de iterações
pred_y = kmeans.fit_predict(col)
plt.scatter(new_df['genero'], new_df['rating'], c = pred_y) #posicionamento dos eixos x e y
plt.xlim(0, 60) #range do eixo x
plt.ylim(0, 5) 
plt.scatter(kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,0], s = 70, c = 'red') #posição de cada centroide no gráfico
st.pyplot(plt)