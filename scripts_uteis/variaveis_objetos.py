# cria variável int
x = 10
print(x)

# cria variável float
y = 3.14
print(y)

# cria variável string
nome = "Python"
print(nome)

# cria variável booleana
verdadeiro = True
falso = False
print(verdadeiro)
print(falso)

# calculadora
a = 5
b = 2
c = (a + b) * 3
print("Resultado:", c)

# exibir texto no console
mensagem = "Olá, Mundo!"
print(mensagem)

# verificar tipo da variável
print(type(x))          # int
print(type(y))          # float
print(type(nome))       # str
print(type(verdadeiro)) # bool
print(type(falso))      # bool

# entrada de dados
idade = input("Digite sua idade: ")
print("Sua idade é:", idade, 'anos')
type(idade)  # str

# converter string para int
var = input("Digite um número: ")
print(type(var))  # str
var = int(var)
print(type(var))  # int