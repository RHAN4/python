import os

os.system("cls || clear")

print("-- Solicitando dados --")
PriNumero = int(input("Digite o primeiro número: "))
SegNumero = int(input("Digite o segundo número: "))

media = (PriNumero + SegNumero) / 2
soma = PriNumero + SegNumero
produto = PriNumero * SegNumero

if PriNumero > SegNumero:
      maValor = PriNumero
      menValor = SegNumero
else:
    maValor = SegNumero
    menValor = PriNumero

print("\n")
print("-- Exibindo resultados --")
print(f"Primeiro número: {PriNumero}")
print(f"Segundo número: {SegNumero}")
print(f"A média é: {media}")
print(f"A soma dos valores é: {soma}")
print(f"O produto dos valores é: {produto}")
print(f"Maior número: {maValor}")
print(f"Menor número: {menValor}")