import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def IMC (peso, altura):
    calculo = peso / (altura **2)
    return calculo
    
def situacao(calculo):
    if calculo < 18.5:
        situ = "Abaixo do peso."
    elif calculo >= 18.5 and calculo < 25:
        situ = "Peso normal."
    elif calculo >= 25 and calculo < 30:
        situ = "Sobrepeso."
    elif calculo >= 30 and calculo < 35:
        situ = "Obesidade grau I."
    elif calculo >= 35 and calculo < 40:
        situ = "Obesidade grau II."
    elif calculo >= 40:
        situ = "Obesidade grau III."
    return situ
    
# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    
    # Verificando se o usuário quer sair
    sobrenome = input("Digite o sobrenome do usuário (ou digite sair para encerrar.): ")
    if sobrenome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    
    inMassa = IMC(peso, altura)  
    
# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print("IMC: ", round(inMassa, 2))
    print("Situação: ", situacao(inMassa))

