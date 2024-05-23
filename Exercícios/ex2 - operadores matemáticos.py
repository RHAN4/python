import os

os.system("cls || clear")

PriNumero: int
SegNumero: int

PriNumero = int(input("Digite o primeiro número: "))
SegNumero = int(input("Digite o segundo número: "))

soma = PriNumero + SegNumero
subtracao = PriNumero - SegNumero
multiplicacao = PriNumero * SegNumero
divisao = PriNumero / SegNumero

print(f"Primeiro número: {PriNumero}")
print(f"Segundo número: {SegNumero}")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")