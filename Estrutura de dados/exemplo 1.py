import os

os.system("cls || clear")

# Constante.
QUANTIDADE_ALUNOS = 2

# Vetor.
nomes = []
idades = []


#Solicitando dados para o usurário.
for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))

    nomes.append(nome)
    idades.append(idade)

# Exibindo dados para o usuário.
for i in range (QUANTIDADE_ALUNOS):
    print(f"Nome: {nomes[i]}")
    print(f"Idade: {idades[i]}")