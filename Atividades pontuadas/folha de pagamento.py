import os

os.system("cls || clear")

from dataclasses import dataclass

# Funções: 

def CalculoINSS(salarioBase):
    if salarioBase <= 1100.10:
        INSSdesconto = salarioBase * 0.075
    elif salarioBase <= 2203.48:
        INSSdesconto = salarioBase * 0.9
    elif salarioBase <= 3305.22:
        INSSdesconto = salarioBase * 0.12
    elif salarioBase <= 6433.57:
        INSSdesconto = salarioBase * 0.14
    else:
        INSSdesconto = 854.36
    return INSSdesconto

def CalculoIRRF(salarioBase, NumDependentes):
    dependenteDeducao = NumDependentes * 189.59
    if salarioBase <= 2259.20:
        IRRFdesconto = 0
    elif salarioBase <= 2826.65:
        IRRFdesconto = salarioBase * 0.075
    elif salarioBase <= 3751.05:
        IRRFdesconto = salarioBase * 0.15
    elif salarioBase <= 4664.68:
        IRRFdesconto = salarioBase * 0.225
    elif salarioBase > 4664.68:
        IRRFdesconto = salarioBase * 0.275
    IRRFdesconto = IRRFdesconto - dependenteDeducao
    return IRRFdesconto
    
def valeTransporte(salarioBase, transporte):
    return salarioBase * 0.06 if transporte.lower() == "sim" else 0
    
def valeRefeicao(valeOfertado):
    RefeicaoDesconto = valeOfertado * 0.20
    return RefeicaoDesconto

def planoSaude(NumDependentes):
    descontoFixo = 150.0
    descontoDependente = 150.0
    return descontoFixo + (NumDependentes * descontoDependente)
    
# Classes
class Dados:
    def __init__(self, matriculas, senhas, salarioBrutos):
        self.matriculas = matriculas
        self.senhas = senhas
        self.salarioBrutos = salarioBrutos

# Funções:
recolhidos = []

matricula = input("Informe o seu número de matrícula: ")
senha = input("Informe a senha: ")
salario = float(input("Informe o valor do seu salário: "))
NumDependentes = int(input("Insira o número de dependentes: "))
ValeTransp = input("Deseja receber vale transporte? (Digite sim ou não): ")
ValeRefe = float(input("Informe o valor do vale refeição fornecido: "))

recolhidos.append(Dados(matricula, senha, salario))

# Chamando as funções: 

inss = CalculoINSS(salario)

irrf = CalculoIRRF(salario, NumDependentes)

valeT = valeTransporte(salario, ValeTransp)

valeR = valeRefeicao(ValeRefe)

planoS = planoSaude(NumDependentes)

descontoTotal = inss + irrf + valeT + valeR + planoS
salarioLiquido = salario - descontoTotal
    
# Exibindo dados: 
print("\n")
print("- Dados do usuário -")
for i in recolhidos:
    print(f"Número de matrícula: {i.matriculas}")
    print(f"Salário bruto: R$ {i.salarioBrutos}")
    print(f"Desconto do INSS: R$ {inss:.2f}")
    print(f"Desconto do IRRF: R$ {irrf:.2f}")
    print(f"Desconto do Vale Transporte: R$ {valeT:.2f}")
    print(f"Desconto do Vale Refeição: R$ {valeR:.2f}")
    print(f"Desconto do Plano de Saúde: R$ {planoS:.2f}")
    print(f"Total descontado: R$ {descontoTotal:.2f}")
    print(f"Salário liquido: R$ {salarioLiquido:.2f}")