import plotly.express as px
import streamlit as st

def strip_rating(df):
  rating = []
  generos = []
  
  for i in range(df.shape[0]):
    existentIndex = df.index[i]
    if 'economia' in df['genero'][existentIndex].lower():
      rating.append(df['rating'][existentIndex])
      generos.append('economia')
    elif 'romance' in df['genero'][existentIndex].lower():
      rating.append(df['rating'][existentIndex])
      generos.append('romance')
    elif 'fantasia' in df['genero'][existentIndex].lower():
      rating.append(df['rating'][existentIndex])
      generos.append('fantasia')

  fig = px.strip(x=rating, y=generos)
  st.write(fig)
