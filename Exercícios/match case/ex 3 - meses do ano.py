import os

os.system ("cls || clear")

print(" - Meses do ano - ")
print("""
1 - Janeiro \t 2 - Fevereiro
3 - Março \t 4 - Abril
5 - Maio \t 6 - Junho
7 - Julho \t 8 - Agosto
9 - Setembro \t 10 - Outubro
11 - Novembro \t 12 - Dezembro 
""")

while True:
    mes = int(input("Digite o número do mês desejado:  "))

    match(mes):
        case 1 :
            print("Janeiro.")
            break
        case 2 :
            print("Fevereiro.")
            break
        case 3 :
            print("Março.")
            break
        case 4 :
            print("Abril.")
            break
        case 5 :
            print("Maio.")
            break
        case 6 :
            print("Junho.")
            break
        case 7 :
            print("Julho.")
            break
        case 8 :
            print("Agosto.")
            break
        case 9 :
            print("Setembro.")
            break
        case 10 :
            print("Outubro.")
            break
        case 11 :
            print("Novembro.")
            break
        case 12 :
            print("Dezembro.")
            break
        case _ :
            print("Mês inválido.")

print(f"Mês escolhido: {mes}")
         
    