import plotly.express as px
import streamlit as st

def violin_chart(df):
  df = df['rating']
  fig = px.violin(df, y="rating")
  st.write(fig)