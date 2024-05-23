import os

os.system("cls || clear")

print("- Solicitando dados -")
idade = int(input("Digite a sua idade: "))

if idade < 18 and idade > 65:
    print("É obrigado a votar")
else:
    print("Não é obrigado a votar")