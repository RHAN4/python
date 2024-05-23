import os

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def media (n1, n2):
    return (n1 + n2) / 2

logoSenai()
primeiroNum = int(input("Digite o primeiro número: "))
logoSenai()
segundoNum = int(input("Digite o segundo número: "))

resultado =  media(primeiroNum, segundoNum)

logoSenai()
print(f"Média: {resultado}")