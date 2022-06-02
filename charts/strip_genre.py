import plotly.express as px
import streamlit as st

def strip_chart(df):
  querem_ler = []
  generos = []
  
  for i in range(df.shape[0]):
    existentIndex = df.index[i]
    if 'economia' in df['genero'][existentIndex].lower():
      querem_ler.append(df['querem_ler'][existentIndex])
      generos.append('economia')
    elif 'romance' in df['genero'][existentIndex].lower():
      querem_ler.append(df['querem_ler'][existentIndex])
      generos.append('romance')
    elif 'fantasia' in df['genero'][existentIndex].lower():
      querem_ler.append(df['querem_ler'][existentIndex])
      generos.append('fantasia')

  fig = px.strip(x=querem_ler, y=generos)
  st.write(fig)
