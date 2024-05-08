import os

os.system ("clear")

nota: float = -1
soma = 0

for i in range (2):    
    while True:
        nota = float(input(f"Digite a {i + 1}ª nota (entre 0 e 10): "))

        if nota < 0 or nota > 10:
            print("Nota inválida. Por favor, tente novamente. \n")
        else:
            soma += nota
            break

media = soma / 2

print(f"Média:  {media}")