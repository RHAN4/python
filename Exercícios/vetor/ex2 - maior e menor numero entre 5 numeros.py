import os

os.system ("cls || clear")

# Criando uma constante

QUANTIDADE_NUMEROS = 5

# Criando uma lista / vetor.
numeros = []
maiorNumero = 0
menorNumero = 999

# Solicitando 5 notas para o usuário.
for i in range (QUANTIDADE_NUMEROS):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    menorNumero = min (numeros)
    maiorNumero = max (numeros)

# Exibindo as notas para o usuário.
# ForEach
print("\n")

for i, numero in enumerate(numeros):
    print(f"{i + 1}º Número digitado: {numero}")

#Exibindo maior e menor número
print(f"\nMaior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
