import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

def edfc_function(df):
  def edcf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n+1)/n

    return x, y

  x_vers, y_vers = edcf(df['rating'])

  plt.xlabel('Rating')
  plt.ylabel('EDCF')

  plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')
  st.pyplot(plt)
