import os

os.system ("cls | clear")

soma = 0

for i in range (3):
    nota = int(input(f"Digite a sua {i+1}º nota: "))
    soma += nota

media = soma / i

print(f"Média: {media}")

if media >= 7:
    print("Aprovado.")
elif media >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")