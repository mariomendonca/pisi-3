import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer
import matplotlib.pyplot as plt
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import firestore

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

st.dataframe(df)

cred = credentials.Certificate('likeabook.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

for i in range(len(df)):
    existentIndex = df.index[i]
    if (type(df['titulo'][existentIndex]) == str):
        doc_ex = db.collection('books').document()
        doc_ex.set({
            'titulo': df['titulo'][existentIndex],
            'autor' : df['autor'][existentIndex],
            'genero': df['genero'][existentIndex],
            'rating': df['rating'][existentIndex], 
            'descrição': df['descricao'][existentIndex]
        })

