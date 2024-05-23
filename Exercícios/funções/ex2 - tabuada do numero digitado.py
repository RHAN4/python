import os

# Função sem retorno
def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def tabuada(numero, limite = 10):
    for i in range (1, limite + 1):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Digite o número desejado: "))

logoSenai()
tabuada(num)

