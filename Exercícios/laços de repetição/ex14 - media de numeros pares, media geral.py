import os

os.system ("cls || clear")

soma: int = 0
QuantidadeNum = 0
pares = 0
impares = 0
somaPares = 0
somaGeral = 0

while True:
    numero = int(input("Digite o número desejado: "))

    if numero > 0:
        somaGeral += numero
        QuantidadeNum +=1

        if numero % 2 == 0:
            somaPares += numero
            pares += 1
        else:
            impares += 1 

    if numero == 0:
        break

mediaGeral = somaGeral / QuantidadeNum

if pares != 0:
    mediaPares = somaPares / pares

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")

if pares != 0:
    print(f"Média de pares: {mediaPares}")

print(f"Média geral: {mediaGeral}")


