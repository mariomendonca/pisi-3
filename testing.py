import streamlit as st
import pandas as pd

df = pd.read_csv('data/dados.csv')


# st.dataframe(df.)
shape_before = df.shape[0]
shape_current = df.dropna().shape[0]

df = df.dropna()
df = df.drop_duplicates()
to_drop = [
    'ISBN_13', 'ISBN_10', 'ano',
    'resenha', 'editora', 'paginas', 'avaliacao', 'abandonos',
    'idioma', 'leram', 'relendo', 'querem_ler',
    'lendo', 'male', 'female', 'rating'
]
df.drop(to_drop, inplace=True, axis=1)

# newColumnsList = [
#   'Ação', 'Ficção', 'Romance', 'Finanças', 'Economia', 'Aventura', 'Fantasia',
#   'Crime', 'Drama', 'Literatura', 'Literatura estrangeira', 'Medicina', 'Saúde',
#   'Biografia', 'AutoBiografia', 'LGBT', 'GLS', 'InfantoJuvenil', 'Autoajuda',
#   'História'
# ]

newColumnsList = [
    'Economia', 'Finanças ', 'Literatura Brasileira', 'Não-ficção ', 'Drama ', 'Ficção',
    'Literatura Estrangeira', 'Suspense e Mistério', 'Ficção', 'Ficção científica',
    'Biografia', 'Autobiografia', 'Memórias', 'História', 'Política', 'HQ', 'comics', 'mangá',
    'Autoajuda', 'História Geral', 'Infantil', 'Literatura Estrangeira', 'Negócios', 'Empreendedorismo',
    'Jovem adulto', 'Fantasia', 'Horror', 'Terror', 'Aventura', 'Jogos',
    'Crime', 'Romance policial', 'Romance', 'Matemática', 'Medicina', 'Saúde', 'Romance', 'Infantojuvenil', 'Humor', 'Comédia', 'Autoajuda', 'Infantil ', 'Biologia', 'Fantasia',
    'Psicologia', 'Jovem adulto', 'LGBT', 'GLS', 'Biografia' 'Autobiografia', 'Memórias', 'Distopia ', 'História ', 'Chick-lit ', 'Literatura Brasileira',
    'Literatura Estrangeira', 'Religião', 'Espiritualidade', 'Jogos', 'Entretenimento ', 'Crime '
]

print(len(newColumnsList))
newColumnsList = list(dict.fromkeys(newColumnsList))
print(len(newColumnsList))

for i in newColumnsList:
    df[i] = 0


# def PopulateNewColumns():
#   for j in range(len(df.values)):
#     for i in range(len(newColumnsList)):
#       if newColumnsList[i].upper() in df.values[j][3].upper():
#         # df.values[j][i + 4] = 1
#         df[newColumnsList[i + 4]][j] = 1


def PopulateNewColumns():
  for j in range(len(df)):
    existentIndex = df.index[j]
    for column in newColumnsList:
      if column.upper() in df['genero'][existentIndex].upper():
        df[column][existentIndex] = 1
        # # df.values[j][i + 4] = 1
        # df[newColumnsList[i + 4]][j] = 1

PopulateNewColumns()
# for i in range(50):
#   a = df.index[i]
#   print(df['genero'][a])

# df[newColumnsList[i + 4]][j] = 1

# df


# print(df.value_counts)

# print(df.shape)
# print(df.values)
# for i in df['autor']:
#   print(i)
# df['autor'][14] = 'Hello world'
# print(df['autor'][0])
print(df.values[0])
st.dataframe(df)












# newList = list()
# for i in range(100):
#     a = df.values[i][3].split('/')
#     for i in a:
#         if not i in newList:
#             newList.append(i)