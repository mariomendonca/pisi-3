import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

def category_chart(df):
	homens = df.male
	mulheres = df.female

	plt.bar('Homens', np.mean(homens), align='center', width=-0.2)
	plt.bar('Mulheres', np.mean(mulheres), align='center', width=0.2)

	plt.title('Relação entre sexo e interesse em categorias',fontsize=18)
	plt.show()

	st.pyplot(plt)

