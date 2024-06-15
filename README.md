arquivo = "projetos.csv" 
df = pd.read_csv(arquivo, sep=';') 
df.head(23)
df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
print(df.tail())


df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*')
plt.show()
df["Projeto1"].plot(kind = 'hist')
df["Projeto4"].plot(kind = 'hist')
plt.show()


ip.list_series('Selic')
selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
selic
ip.timeseries('BM12_TJOVER12', year=2021).plot("MONTH", "VALUE ((% a.m.))")
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))")
plt.show()

