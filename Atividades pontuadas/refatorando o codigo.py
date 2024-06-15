import os
import math
from dataclasses import dataclass

# Funções:
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def calcular_imc(peso, altura):
    return peso / math.pow(altura, 2)

def resultado_imc(imc):
    if imc < 18.5:
        resultado = "Muito magro"
    elif imc < 25:
        resultado = "Peso normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    elif imc < 35:
        resultado = "Obesidade grau I"
    elif imc < 40:
        resultado = "Obesidade grau II"
    else:
        resultado = "Obesidade grau III (mórbida)"

    return resultado

# Classes:
class Dados:
    def __init__(self, nomes, sobrenomes, nomes_completos, idades, alturas, pesos):
        self.nomes = nomes
        self.sobrenomes = sobrenomes
        self.nomes_completos = nomes_completos
        self.idades = idades
        self.alturas = alturas
        self.pesos = pesos

# Vetores:
imcs = []
resultados_imcs = []
recolhidos = []

while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    nomes_completos = (nome + " " + sobrenome)
    
    recolhidos.append(Dados(nome, sobrenome, nomes_completos, idade, altura, peso))

    imc = calcular_imc(peso, altura)

    imcs.append(imc)
    resultados_imcs.append(resultado_imc(imc))

logoSenai()
print("\nDados dos usuários: \n")
for i, coletados in enumerate(recolhidos):
    print(f"Usuário {i+1}: ")
    print("Nome: ", coletados.nomes)
    print("Sobrenome: ", coletados.sobrenomes)
    print("Nome completo: ", coletados.nomes_completos)
    print("Idade: ", coletados.idades)
    print("Altura: ", coletados.alturas, "metros")
    print("Peso: ", coletados.pesos, "quilogramas")
    print("IMC: ", round(imcs[i], 2))
    print("Resultado: ", resultados_imcs[i])
    print("\n")
