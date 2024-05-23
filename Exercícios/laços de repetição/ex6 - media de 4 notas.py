import os

os.system ("cls | clear")

soma = 0

for i in range (4):
    nota = int(input(f"Digite a {i+1}º nota: "))

    soma += nota
    i += 1

media = soma / i

print(f"A média é: {media}")