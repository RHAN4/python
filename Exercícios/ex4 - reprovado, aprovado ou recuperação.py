import os

os.system ("cls || clear")

print("-- Solicitando dados --\n")
nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))
PriNota = float(input("Digite a sua primeira nota: "))
SegNota = float(input("Digite a sua segunda nota: "))
TerNota = float(input("Digite a sua terceira nota: "))

# Calculando a média
media = (PriNota + SegNota + TerNota) / 3

print("-- Exibindo dados --")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {PriNota}")
print(f"Segunda nota: {SegNota}")
print(f"Terceira nota: {TerNota}")
print(f"Média: {media}")

# Verificando a situação do aluno
if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")