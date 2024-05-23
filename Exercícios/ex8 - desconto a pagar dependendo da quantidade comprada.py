import os

os.system("cls || clear")

print("-- Solicitando informações --")
nome = str(input("Informe o nome do produto comprado: "))
quantidade = int(input("Informe a quantidade comprada: "))
precoUni = float(input("Informe o preço unitário do produto: "))

if quantidade <= 5:
    desconto = 0.02

elif quantidade <= 10:
    desconto = 0.03

else:
    desconto = 0.05

subTotal = precoUni * quantidade
totalPagar = subTotal - (subTotal * desconto)

print("\n -- Exibindo resultados --")
print(f"Nome do produto: {nome}")
print(f"Preço do produto: {precoUni}")
print(f"Quantidade do produto: {quantidade}")
print(f"Total a pagar: {totalPagar}")