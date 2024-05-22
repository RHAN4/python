import os

os.system ("cls || clear")

QUANTIDADE_NUMEROS = 6

numeros = []
pares = 0
impares = 0

for i in range (QUANTIDADE_NUMEROS):
    numero = int(input("Digite o número desejado: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

for i in range (QUANTIDADE_NUMEROS):
    print(f"Números informados: {numeros[i]}")

print(f"Números pares informados: {pares}")
print(f"Números impares informados: {impares}")