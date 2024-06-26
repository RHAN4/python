# EXIBIR OS DADOS

import os
from dataclasses import dataclass

os.system("cls || clear")

# Constante.
QUANTIDADE_ALUNOS = 2

# Classe.
@dataclass
class Aluno:
    nome: str
    idade: int

alunos = []

# Solicitando dados
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome  = input("Digite o seu nome: "),
        idade = int(input("Digite a sua idade: "))
    )
    alunos.append(aluno)

# Nome do arquivo
arquivo = 'aluno.txt'

# Grava os dados no arquivo
with open(arquivo, 'w') as arquivo:
    for aluno in alunos:
        arquivo.write(f"{aluno.nome}, {aluno.idade}")

print(f"Dados gravados com sucesso.") 