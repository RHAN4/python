import os

os.system ("cls | clear")

soma = 0

for i in range (1, 6):
    numero = int(input("Digite o {i}º número: "))
    soma += numero

print(f"A soma de todos os números digitados é: {soma}")