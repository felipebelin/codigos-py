import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ipeadatapy as ip

# Título do aplicativo
st.title("Análise de Projetos e Taxa Selic")

# Leitura do arquivo CSV
arquivo = "projetos.csv"
df = pd.read_csv(arquivo, sep=';')
st.subheader("Dados dos Projetos")
st.dataframe(df.head(23))

# Criação de um novo DataFrame e concatenação com o existente
df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704]})
df = pd.concat([df, df1], ignore_index=True)
st.subheader("Dados dos Projetos Atualizados")
st.dataframe(df.tail())

# Plotagem de gráficos
# Gráfico de dispersão entre Projeto1 e Projeto2
st.subheader("Gráfico de Dispersão entre Projeto1 e Projeto2")
fig, ax = plt.subplots()
df.plot(kind='scatter', x='Projeto1', y='Projeto2', color='darkgreen', marker='*', ax=ax)
st.pyplot(fig)

# Histogramas de Projeto1 e Projeto4
st.subheader("Histograma de Projeto1")
fig, ax = plt.subplots()
df["Projeto1"].plot(kind='hist', title='Histograma de Projeto1', ax=ax)
st.pyplot(fig)

st.subheader("Histograma de Projeto4")
fig, ax = plt.subplots()
df["Projeto4"].plot(kind='hist', title='Histograma de Projeto4', ax=ax)
st.pyplot(fig)

# Utilização do ipeadatapy para obter dados da Selic
st.subheader("Dados da Selic")
selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
st.dataframe(selic)

# Plotagem dos dados da Selic
st.subheader("Selic 2021")
selic_2021 = ip.timeseries('BM12_TJOVER12', year=2021)
fig, ax = plt.subplots()
selic_2021.plot(x="MONTH", y="VALUE ((% a.m.))", title='Selic 2021', ax=ax)
st.pyplot(fig)

st.subheader("Selic 2022")
selic_2022 = ip.timeseries('BM12_TJOVER12', year=2022)
fig, ax = plt.subplots()
selic_2022.plot(x="MONTH", y="VALUE ((% a.m.))", title='Selic 2022', ax=ax)
st.pyplot(fig)
selic_2022.plot(x="MONTH", y="VALUE ((% a.m.))", title='Selic 2022')
plt.show()


