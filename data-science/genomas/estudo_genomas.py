entrada = open('data-science/genomas/bacteria.fasta').readlines()
saida = open('data-science/genomas/bacteria.html', 'w')

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

# Remover linhas de cabeçalho
entrada = [linha for linha in entrada if not linha.startswith('>')]
entrada = ''.join(entrada).replace("\n", "").replace("\r", "")

for k in range(len(entrada)-1):
    par = entrada[k] + entrada[k+1]
    if par in cont:
        cont[par] += 1

print(cont)