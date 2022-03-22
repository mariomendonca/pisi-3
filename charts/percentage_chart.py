import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def percentage_chart(df):
  male = df.male
  female = df.female
  labels = ['Masculino', 'Feminino']
  plt.bar(labels[0], np.mean(male), align='center', width=-0.2)
  plt.bar(labels[1], np.mean(female), align='center', width=0.2)

  plt.xlabel('Gênero')
  plt.ylabel('% média')
  plt.title('Média do sexo de leitores')
  st.pyplot(plt)
