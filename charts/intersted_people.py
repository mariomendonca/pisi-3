import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def intersted_people(df):
	abandonos = df.abandonos
	querem_ler = df.querem_ler

	labels = ['Abandonos', 'Quantidade de Pessoas Interessadas']

	plt.bar(labels[0],np.mean(abandonos), color='blue')
	plt.bar(labels[1],np.mean(querem_ler), color='pink', bottom=abandonos)

	plt.xlabel('Abandonos', fontsize=16)
	plt.ylabel('Pessoas Interessadas', fontsize=16)
	plt.title('Relação entre abandonos e interesses',fontsize=18)
	plt.legend(labels,loc=2)
	plt.show()

	st.pyplot(plt)

