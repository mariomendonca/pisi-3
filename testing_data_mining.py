from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer

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



fig, ax = plt.subplots(2, 2, figsize=(15,8))
for i in [2, 3, 4, 5]:
    '''
    Create KMeans instance for different number of clusters
    '''
    km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=42)
    q, mod = divmod(i, 2)
    '''
    Create SilhouetteVisualizer instance with KMeans instance
    Fit the visualizer
    '''
    visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q-1][mod])
    # visualizer.fit(X)
    visualizer.fit(df)

st.pyplot(plt)
# st.(visualizer.fit(df))
