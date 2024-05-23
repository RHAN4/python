import os

# Função sem retorno
def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def inflacao(valor):
    if valor < 100:
        preco = (valor * 0.1) + valor
    elif valor >= 100:
        preco = (valor * 0.2) + valor
    return preco

logoSenai()
custo = int(input("Digite o valor pago: "))