import streamlit as st
import pandas as pd

df = pd.read_csv('data/dados.csv')

st.write("Dados.csv dataset!")
st.dataframe(df)
