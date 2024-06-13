import os

from dataclasses import dataclass

os.system("cls || clear")

# Constante.
QUANTIDADE_ALUNOS = 2

#Classe.
@dataclass
class Aluno:
    nome: str
    idade: int
    altura: float
    peso: float
# Outro tipo: 
# class Aluno:
# def __init__(self, nome, idade):
    # self.nome = nome
    # self.idade = idade

alunos = []

#Solicitando dados para o usurário.
for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    altura = float(input("Digite a sua altura: "))
    peso = float(input("Digite o seu peso: "))

    aluno = Aluno(nome = nome, idade = idade, altura = altura, peso = peso)
    # Outro tipo: 
    # aluno = Aluno (
    # nome = input("Digite o seu nome: "),
    # idade = int(input("Digite a sua idade: "))
    # altura = float(input("Digite a sua altura: "))
    # peso = float(input("Digite o seu peso: "))
    # )
    alunos.append(aluno)

# Exibindo dados para o usuário.
for aluno in alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Altura: {aluno.altura}")
    print(f"Peso: {aluno.peso}")
    print("\n")

# Outro tipo:
# for i in alunos:
    # print(f"Nome: {i.nome}")
    # print(f"Idade: {i.idade}")
    # print(f"Altura: {i.altura}")
    # print(f"Peso: {i.peso}")
    # print("\n")