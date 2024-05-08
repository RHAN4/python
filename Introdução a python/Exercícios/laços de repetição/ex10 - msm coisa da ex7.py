import os

os.system ("cls | clear")

soma = 0

for i in range (3):
    while True:
        nota = float(input(f"Digite a {i + 1}ª nota (entre 0 e 10): "))

        if nota < 0 or nota > 10:
            print("Nota inválida. Por favor, tente novamente. \n")
        else:
            soma += nota
            break

media = soma / i

print(f"Média: {media}")

if media >= 7:
    resultado = "Aprovado."
elif media >= 5 and media >= 6.9:
    resultado = "Recuperação."
else:
    resultado = "Reprovado."

print(f"Situação do aluno: {resultado}")