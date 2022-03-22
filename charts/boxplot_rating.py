import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def boxplot(df):
  f, axes = plt.subplots(2, figsize=(7, 7), sharex=True)
  sns.despine(left=True)
  plt.xlabel('rating')

  sns.boxplot(x=df.rating, data=df.rating, ax=axes[0])
  st.pyplot(plt)
