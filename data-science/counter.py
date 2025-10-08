from collections import Counter

cores = ['azul', 'vermelho', 'verde', 'amarelo', 'azul', 'verde', 'verde']
contagem = Counter(cores)
contagem

# Exemplo com strings
frase = "um tigre, dois tigres, três tigres"
contagem_frase = Counter(frase.split())
contagem_frase