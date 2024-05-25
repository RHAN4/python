#Crie um programa que leia 4 notas, armazenando em um vetor e calcule a média aritmética.
#Verifique a situação do aluno considerando:

#- Média maior ou igual a 7: Aprovado.

#- Média maior ou igual a 5: Recuperação.

#- Média menor que 5: Reprovado.

#Mostre as 4 notas informadas pelo usuário e informe a média.

import os

def logoSenai():
  os.system ("cls || clear")
  print("- SENAI -")

notas = []
QUANTIDADE_NOTAS = 4
media: float = 0
soma : float = 0

for i in range (QUANTIDADE_NOTAS):
  nota = float(input("Digite a nota: "))
  notas.append(nota)
  soma += nota

media = soma / QUANTIDADE_NOTAS

logoSenai()
print(f"Notas informadas: {notas}")
print(f"Média: {media}")

if media >= 7:
  print("Aprovado.")
elif media >= 5:
  print("Recuperação.")
else:
  print("Reprovado.")



