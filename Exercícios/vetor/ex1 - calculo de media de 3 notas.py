import os

os.system ("cls || clear")

# Criando uma lista / vetor.
notas = []
media : float = 0
soma : float = 0

# Solicitando 3 notas para o usuário.
for i in range (3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    soma += nota

media = soma / 3

# Exibindo as notas para o usuário.
for i in range(3):
    print(f"Nota: {notas[i]}")

print(f"A média é: {media}")