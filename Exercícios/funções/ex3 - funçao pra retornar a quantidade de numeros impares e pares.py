import os

# Função sem retorno
def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def verPares (numeros):
    pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
    return pares

def verImpares (numeros):
    impares = 0
    for numero in numeros:
        if numero % 2 != 0:
            impares += 1
    return impares

lista_numeros = []
QUANTIDADE_NUM = 6

logoSenai()
for i in range (QUANTIDADE_NUM):
    num = int(input("Informe o {i+1}º número: "))
    lista_numeros.append(num)

quantidade_pares = verPares(lista_numeros)
quantidade_impares = verImpares(lista_numeros)

logoSenai()
print(f"Quantidade de números pares digitados: {quantidade_pares}")
print(f"Quantidade de números impares digitados: {quantidade_impares}")
