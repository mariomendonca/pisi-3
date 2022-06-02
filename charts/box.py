import plotly.express as px
import streamlit as st

def box_chart(df):
  df = df['rating']
  fig = px.box(df, y="rating")
  st.write(fig)