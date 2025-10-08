# boxplot - Diagrama de caixa
import matplotlib.pyplot as plt
import numpy as np
import random

vetor = []

for i in range(100):
    vetor.append(random.randint(1, 100))

plt.boxplot(vetor)
plt.title("Boxplot - Diagrama de Caixa")
plt.ylabel("Valores")
plt.show()