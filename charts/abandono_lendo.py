import streamlit as st
import matplotlib.pyplot as plt
from operator import itemgetter


def new_chart(df):
    abandonos = []
    querem_ler = []
    new_list = []
    for i in range(df.shape[0]):
        new_list.append([df.values[i][8], df.values[i][6]])
    
    sorted_list = sorted(new_list, key=itemgetter(0))
    for i in sorted_list:
      abandonos.append(i[1])
      querem_ler.append(i[0])

    plt.plot(querem_ler, abandonos)
    st.pyplot(plt)
