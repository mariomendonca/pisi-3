from cmath import nan
from numpy import append
import streamlit as st
import pandas as pd

from charts.histogram import histogram
from charts.percentage_chart import percentage_chart
from charts.edfc import edfc_function
from charts.boxplot_rating import boxplot
from charts.abandonment import abandonment

df = pd.read_csv('data/dados.csv')

# removing not used columns 
to_drop = ['ISBN_13', 'ISBN_10', 'ano', 'resenha', 'editora']
df.drop(to_drop, inplace=True, axis=1)

# removing outliers and missing values
def remove_outliers():
  outliers = []
  data = df.values
  for i in range(len(data)):
    # rating
    if data[i][4] > 5:
      outliers.append(i)
    
    # pages
    elif data[i][2] == 0:
      outliers.append(i)
    
    # sex
    elif data[i][13] + data[i][14] != 100:
      if data[i][7] != 0 and data[i][9] != 0 and data[i][10]:
        outliers.append(i) 
    
    # genre
    elif type(data[i][12]) == float or type(data[i][12]) == nan:
      outliers.append(i) 
  return outliers
  # return df.drop(labels=outliers, axis=0)

def remove_missing_values():
  outliers = []
  data = df.values
  for i in range(len(data)):
    if (type(data[i][12]) == str):
      genre = data[i][12].replace(' ', '')
      if (len(genre) == 0):
        outliers.append(i)
  # return df.drop(labels=outliers, axis=0)
  return outliers

# print(df.values[603][12])
# print(type(df.values[603][12]))

array1 = remove_outliers()
array2 = remove_missing_values()

print(len(array1) + len(array2))

array1 = array1 + array2
print(len(array1))

mylist = list(dict.fromkeys(array1))
print(len(mylist))


print(len(df))
df = df.drop(labels=mylist, axis=0)
print(len(df))

# print(len(df.values))
# df = remove_outliers()
# # df = remove_missing_values()
# remove_missing_values()
# df = remove_genre_missing_values()
# print(len(df.values))

option = st.sidebar.selectbox(
  'Escolha o grafico que deseja ver!',
  ('dataset', 'histograma', '% do sexo', 'edfc', 'boxplot', 'abandonos')
)

if (option == 'histograma'):
  st.write('Função para obter histograma de avaliações')
  histogram(df)
elif option == '% do sexo':
  st.write('Gráfico de % do sexo dos leitores')
  percentage_chart(df)
elif option == 'edfc':
  st.write('função de distribuição cumulativa empírica das avaliações')
  edfc_function(df)
elif option == 'boxplot':
  st.write('boxplot das avaliações')
  boxplot(df)
elif option == 'abandonos':
  st.write('Gráfico de quantidade de abandono de acordo com a quantidade de páginas')
  abandonment(df)
elif option == 'dataset':
  st.write('Dataset')
  st.dataframe(df)




# def testing():
#   for i in range(df.index[-1]):
#     if (not df['genero'][i]):
#       print(i)


# def remove_outliers():
#   outliers = []
#   for i in range(len(df.values)):
#     if df.values[i][4] > 5:
#       outliers.append(i)
#     elif df.values[i][] : 

#   return df.drop(labels=outliers, axis=0)

# def remove_pages_outliers():
#   df_count = df
#   outliers = []
#   for i in range(len(df)):
#     if df_count['paginas'][i] == 0:
#       outliers.append(i)
#   return df_count.drop(labels=outliers, axis=0)

# def remove_sex_outliers():
#   df_count = df
#   outliers = []
#   for i in range(len(df)):
#     if (df_count['male'][i] + df_count['female'][i] ) != 100:
#       if (df_count['lendo'][i] != 0) and (df_count['relendo'][i] != 0) and (df_count['leram'][i] != 0):
#         outliers.append(i)
#   return df_count.drop(labels=outliers, axis=0)

# def remove_genre_missing_values():
#   df_count = df
#   outliers = []
#   for i in range(len(df)):
#     if (type(df_count['genero'][i]) == str):
#       genre = df_count['genero'][i].replace(' ', '')
#       if (len(genre) == 0):
#         outliers.append(i)
#   return df_count.drop(labels=outliers, axis=0)


# def remove_values_outliers():
#   df_count = df
#   outliers = []
#   for i in range(len(df)):
#     if (type(df_count['genero'][i]) == float):
#       outliers.append(i)

#   return df_count.drop(labels=outliers, axis=0)

# def remove_genre_missing_values():
#   df_count = df
#   outliers = []
#   for i in range(len(df)):
#     if (type(df_count['genero'][i]) == str):
#       genre = df_count['genero'][i].replace(' ', '')
#       if (len(genre) == 0):
#         outliers.append(i)
#   return df_count.drop(labels=outliers, axis=0)

