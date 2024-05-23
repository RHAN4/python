import os

os.system ("cls || clear")

print("- Solicitando dados -")
nome = str(input("Informe o seu nome: "))
sexo = str(input("Informe o seu gênero (M ou F): "))
estadoCivil = str(input("Informe o seu estado civil: "))

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if sexo == "F" and estadoCivil == "Casada":
    tempoCas = str(input("Informe o tempo de casada: "))

print("\n")
print("- Exibindo dados -")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estadoCivil}")
print(f"Tempo de casada: {tempoCas} anos")