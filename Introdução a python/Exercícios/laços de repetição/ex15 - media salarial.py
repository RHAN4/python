import os
import sys

os.system ("cls || clear")

somaSalario = 0
QtdMulheresSa = 0
maiorIdade = 0
menorIdade = sys.maxsize

while True: 
    print("\n Código | Descrição \n")
    print("1  |  Adicionar pessoa\n")
    print("2  |  Exibir resultados e sair\n")
    codigo = input((f"Digite o código desejado: "))

    if codigo == 1:
        idade = int(input("Digite a sua idade: "))
        if idade > maiorIdade:
            maiorIdade = idade
        if idade < menorIdade:
            menorIdade = idade
    
    sexo = input("Digite o seu gênero: ")
    salario = float(input("Digite o seu salário: "))

    if sexo == "F":
        if salario >= 5000:
            QtdMulheresSa += 1

    somaSalario += salario

    if codigo != 2:
        break

mediaSalarial = somaSalario / QtdMulheresSa

print(f"\nMédia de salário do grupo: R${mediaSalarial}")
print(f"\nMaior idade do grupo: {maiorIdade}")
print(f"\nMenor idade do grupo: {menorIdade}")
print(f"\nQuantidade de mulheres com salário a partir de R$ 5.000,00: {QtdMulheresSa}")