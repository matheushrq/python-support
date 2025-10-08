# crescimento da população brasileira de 1980 a 2016
import pandas as pd
import matplotlib.pyplot as plt

dados = open('data-science/populacao_brasileira.csv').readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].strip().split(';')
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x, y, color='gray', alpha=0.3)
#plt.scatter(x, y, color='gray', alpha=0.3)
plt.plot(x, y, color='black', marker='_')
plt.title("Crescimento da População Brasileira (1980-2016)")
plt.xlabel("Ano")
plt.ylabel("População (x100.000.000)")
plt.show()