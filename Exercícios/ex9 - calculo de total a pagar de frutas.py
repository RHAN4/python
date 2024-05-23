import os

os.system("cls || clear")


pesoMorango = float(input("Informe a quantidade de morangos comprados: "))
pesoMaca = float(input("Informe a quantidade de maçãs compradas: "))

if pesoMorango < 5:
    precoMorango = 2.50
else: 
    precoMorango = 2.20

if pesoMaca < 5:
    precoMaca = 1.80
else:
    precoMaca = 1.50

pesoTotal = pesoMaca + pesoMorango
subTotal = (precoMorango * pesoMorango) + (precoMaca * pesoMaca)

if pesoTotal > 8 or subTotal > 25:
    desconto = subTotal * 0.10

totalPagar = subTotal - desconto

print("- Resultados -")
print(f"Peso em morangos (em KG): {pesoMorango:.2f}")
print(f"Peso em maçãs (em KG): {pesoMaca:.2f}")
print(f"Soma dos pesos: {pesoTotal:.2f}")
print(f"Subtotal: R${subTotal:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total a pagar: R${totalPagar:.2f}")