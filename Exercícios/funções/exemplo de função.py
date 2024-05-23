import os

# Função sem retorno
def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

# Função com retorno
def somar (n1, n2):
    resultado = n1 + n2
    return resultado

def subtrair (n1, n2):
    resultado = n1 - n2
    return resultado

def multiplicar (n1, n2):
    return n1 * n2

def dividir (n1, n2):
    return n1 / n2

# Solicitando dados para o usuário.
logoSenai()
primeiroNum = int(input("Digite o primeiro número: "))

logoSenai()
segundoNum = int(input("Digite o segundo número: "))

# Chamar a função para calcular

soma = somar(primeiroNum, segundoNum)
subtracao = subtrair(primeiroNum, segundoNum)
multiplicacao = multiplicar(primeiroNum, segundoNum)
divisao = dividir(primeiroNum, segundoNum)

#Exibindo dados para o usuário.
logoSenai()
print(f"Adição: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")