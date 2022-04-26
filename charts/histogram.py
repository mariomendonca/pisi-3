import matplotlib.pyplot as plt
import streamlit as st

def histogram(df):
  plt.hist(df.rating)
  plt.xlabel('Rating')
  plt.ylabel('Quantidade')
  plt.title('Histograma de avaliações')
  st.pyplot(plt)