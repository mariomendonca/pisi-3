from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
#
# Load IRIS dataset
#
iris = datasets.load_iris()
X = iris.data
y = iris.target

st.dataframe(iris.data)
print(len(iris.target))
print(len(iris.data))

df = pd.read_csv('data/dados.csv')
to_drop = ['ISBN_13', 'ISBN_10', 'ano', 'resenha', 'editora', 'autor', 'genero', 'descricao', 'male', 'female', 'titulo', 'idioma', 'leram', 'lendo', 'relendo', 'avaliacao', 'querem_ler', 'abandonos']
df.drop(to_drop, inplace=True, axis=1)
df = df.drop_duplicates()
df = df.dropna()

# print(df['paginas'])
st.dataframe(df)

#
# Instantiate the KMeans models
#
km = KMeans(n_clusters=3, random_state=42)
#
# Fit the KMeans model
#
# km.fit_predict(X)
km.fit_predict(df)
#
# Calculate Silhoutte Score
#
score = silhouette_score(df, km.labels_, metric='euclidean')
#
# Print the score
#
print('Silhouetter Score: %.3f' % score)



# Descubrindo numeros ideais de clusters
# fig, ax = plt.subplots(2, 2, figsize=(15,8))
# for i in [2, 3, 4, 5]:
# for i in [2, 3, 4, 5]:
#     '''
#     Create KMeans instance for different number of clusters
#     '''
#     km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=42)
#     q, mod = divmod(i, 2)
#     '''
#     Create SilhouetteVisualizer instance with KMeans instance
#     Fit the visualizer
#     '''
#     visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q-1][mod])
#     # visualizer.fit(X)
#     visualizer.fit(df)

fig, ax = plt.subplots(2, 2, figsize=(15,8))
km = KMeans(n_clusters=5, init='k-means++', n_init=10, max_iter=100, random_state=42)
q, mod = divmod(5, 2)

visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q-1][mod])
# visualizer.fit(X)
visualizer.fit(df)
print(km.labels_)


st.write('labels')
st.write(km.labels_)
st.write('target')
st.write(iris.target)
st.pyplot(plt)
# st.(visualizer.fit(df))



plt.scatter(df['paginas'], df['rating'])
plt.xlim(0, 3000) #range do eixo x
plt.ylim(0, 10) #range do eixo y
st.pyplot(plt)

kmeans = KMeans(n_clusters = 5, #numero de clusters
init = 'k-means++', n_init = 10, #algoritmo que define a posição dos clusters de maneira mais assertiva
max_iter = 300) #numero máximo de iterações
pred_y = kmeans.fit_predict(df)
plt.scatter(df['paginas'], df['rating'], c = pred_y) #posicionamento dos eixos x e y
plt.xlim(0, 3000) #range do eixo x
plt.ylim(0, 10) 
plt.scatter(kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,0], s = 70, c = 'red') #posição de cada centroide no gráfico
st.pyplot(plt)
# plt.show()
# plt.scatter(dataset[:,1], dataset[:,0]) #posicionamento dos eixos x e y
# print(plt.grid) #função que desenha a grade no nosso gráfico)