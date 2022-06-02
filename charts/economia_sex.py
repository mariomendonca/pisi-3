import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def economia_sex_percentage(df):
  dropList = []
  for i in range(df.shape[0]):
    existentIndex = df.index[i]
    if not ('economia' in df['genero'][existentIndex].lower()):
      dropList.append(existentIndex)

  print(dropList)
  df = df.drop(labels=dropList, axis=0)

  male = df.male
  female = df.female
  labels = ['Masculino', 'Feminino']
  plt.bar(labels[0], np.mean(male), align='center', width=-0.2)
  plt.bar(labels[1], np.mean(female), align='center', width=0.2)

  plt.xlabel('Gênero')
  plt.ylabel('% média')
  plt.title('Média do sexo de leitores de livros do gênero Economia')
  st.pyplot(plt)
