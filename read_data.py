import streamlit as st
import pandas as pd

df = pd.read_csv('newDados.csv')
st.dataframe(df)