import pandas as pd
import matplotlib.pyplot as plt
import ipeadatapy as ip


arquivo = "projetos.csv"
df = pd.read_csv(arquivo, sep=';')
print(df.head(23))

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704]})
df = pd.concat([df, df1], ignore_index=True)
print(df.tail())


df.plot(kind='scatter', x='Projeto1', y='Projeto2', color='darkgreen', marker='*')
plt.title('Scatter plot entre Projeto1 e Projeto2')
plt.show()

df["Projeto1"].plot(kind='hist', title='Histograma de Projeto1')
plt.show()
df["Projeto4"].plot(kind='hist', title='Histograma de Projeto4')
plt.show()

print(ip.list_series('Selic'))
selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
print(selic)

selic_2021 = ip.timeseries('BM12_TJOVER12', year=2021)
selic_2022 = ip.timeseries('BM12_TJOVER12', year=2022)

selic_2021.plot(x="MONTH", y="VALUE ((% a.m.))", title='Selic 2021')
plt.show()
selic_2022.plot(x="MONTH", y="VALUE ((% a.m.))", title='Selic 2022')
plt.show()


