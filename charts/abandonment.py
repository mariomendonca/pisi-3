import matplotlib.pyplot as plt
import streamlit as st
import numpy as np


def abandonment(df): 
  abandonos = [0,0,0]
  labels = ['0-100', '100-300', '300-600']
  for i in range(len(df.paginas)):
    if df.paginas[i] < 100:
      abandonos[0] += df.abandonos[i]
    elif df.paginas[i] >= 100 and i < 300:
      abandonos[1] += df.abandonos[i]
    elif df.paginas[i] >= 300 and i < 600:
      abandonos[2] += df.abandonos[i]


  x = np.arange(len(labels))

  plt.bar(labels[0], abandonos[0], align='center', width=-0.2)
  plt.bar(labels[1], abandonos[1], align='center', width=-0.2)
  plt.bar(labels[2], abandonos[2], align='center', width=-0.2)
  plt.xlabel('Quantidade de páginas')
  plt.ylabel('Quantidade de abandonos')
  plt.title('Quantidade de abandono por páginas')
  st.pyplot(plt)
