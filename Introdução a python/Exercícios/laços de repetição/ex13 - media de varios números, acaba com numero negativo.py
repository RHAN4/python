import os
os.system ("cls || clear")

soma: int = 0
QuantidadeNum = 0

while True:
    numero = int(input("Digite o número desejado: "))

    if numero < 0:
        break

    soma += numero
    QuantidadeNum += 1

media = soma / QuantidadeNum

print(f"Média: {media}")



