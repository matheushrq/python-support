from br_nome_gen import pessoa_random

pessoa_random().nome

nomes = []
for i in range(0, 5):
    nomes.append(pessoa_random().nome.split()[0])

print(nomes)