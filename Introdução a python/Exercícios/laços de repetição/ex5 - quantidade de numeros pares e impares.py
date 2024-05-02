import os

os.system ("cls | clear")

pares = 0
impares = 0

for i in range (5):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n")
print(f"Quantidade de pares digitados: {pares}\n")
print(f"Quantidade de impares digitados: {impares}\n")