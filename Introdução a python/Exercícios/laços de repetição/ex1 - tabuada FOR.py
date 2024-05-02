import os

os.system ("cls || clear")

numero = int(input("Informe o número desejado: "))

for i in range (1, 11):
    print(f"{numero} x {i} = {numero * i}")