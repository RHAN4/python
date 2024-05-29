import os

os.system("cls || clear")

print("-  MENU  -")
print("""
1 - Picanha - R$25,00
2 - Lasanha - R$20,00
3 - Strogonoff - R$18,00
4 - Bife Acebolado - R$15,00
5 - Pão com ovo - R$5,00
""")

while True: 
    codigo = int(input("Digite o código da comida desejada: "))

    match(codigo):
        case 1:
            print("Prato escolhido: Picanha.")
            print("Valor: R$25,00.")
            break
        case 2:
            print("Prato escolhido: Lasanha.")
            print("Valor: R$20,00.")
            break
        case 3:
            print("Prato escolhido: Strogonoff.")
            print("Valor: R$18,00.")
            break
        case 4:
            print("Prato escolhido: Bife Acebolado.")
            print("Valor: R$15,00.")
            break
        case 5:
            print("Prato escolhido: Pão com ovo.")
            print("Valor: R$5,00.")
            break