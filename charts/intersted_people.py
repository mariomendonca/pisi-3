import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def intersted_people(df):
	abandonos = df.abandonos
	querem_ler = df.querem_ler

	# Plot a simple line chart
	plt.plot(querem_ler, abandonos)

	plt.xlabel('Pessoas interessadas')
	plt.ylabel('Abandonos')

	plt.title('Relação entre abandonos e interesses',fontsize=18)
	plt.show()

	st.pyplot(plt)

