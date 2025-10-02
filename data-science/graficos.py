# visualização de dados com gráfico de linhas

import matplotlib.pyplot as plt
import seaborn as sns

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)

# Título do gráfico
sns.lineplot(x=x, y=y)
plt.title("Gráfico de Linhas")

# Rótulos dos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Exibir o gráfico
plt.show()

# visualização de dados com gráfico de barras
eixo_x = ['A', 'B', 'C', 'D', 'E']
eixo_y = [5, 7, 3, 8, 2]

sns.barplot(x=eixo_x, y=eixo_y)

# Título do gráfico
plt.title("Gráfico de Barras")

# Rótulos dos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Exibir o gráfico
plt.show()