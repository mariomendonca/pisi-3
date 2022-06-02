from operator import itemgetter
import plotly.graph_objects as go
import streamlit as st

def bubble_chart(df):
  rating = []
  querem_ler = []
  abandonos = []
  new_list = []
  for i in range(df.shape[0]):
    new_list.append([df.values[i][4], df.values[i][8], df.values[i][6]])
  
  sorted_list = sorted(new_list, key=itemgetter(1))
  for i in sorted_list:
      rating.append(i[0])
      querem_ler.append(i[1])
      abandonos.append(i[2])
  
  fig = go.Figure(data=[go.Scatter(
      x=querem_ler, y=abandonos,
      mode='markers',
      marker_size=rating)
  ])

  st.write(fig)