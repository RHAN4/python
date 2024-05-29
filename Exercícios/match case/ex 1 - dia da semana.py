import os

os.system ("cls || clear")

print("-  TABELA DE DIAS  -")
print("1 - Domingo")
print("2 - Segunda-feira")
print("3 - Terça-feira")
print("4 - Quarta-feira")
print("5 - Quinta-feira")
print("6 - Sexta-feira")
print("7 - Sábado")

while True:
    dia = int(input("Digite o número do dia da semana: "))
    match(dia):
        case 1:
            print("Final de semana.")
            break
        case 2:
            print("Dia útil.")
            break
        case 3:
            print("Dia útil.")
            break
        case 4:
            print("Dia útil.")
            break
        case 5:
            print("Dia útil.")
            break
        case 6:
            print("Dia útil.")
            break
        case 7:
            print("Final de semana.")
            break
        case _:
            print("Dia inválido.")
    