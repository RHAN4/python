import os
from dataclasses import dataclass
os.system ("cls | clear")

class Pets:
    def __init__(self, nome, idade, raca, porte, alimentacao):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.alimentacao = alimentacao

pets = []

QUANTIDADE_PETS = 2

for i in range (QUANTIDADE_PETS):
    nomePet = input(f"Digite o nome do {i + 1}º animal: ")
    idadePet = input(f"Digite a idade de {nomePet}: ")
    racaPet = input(f"Digite a raça de {nomePet}: ")
    portePet = input(f"Digite o porte de {nomePet}: ")
    alimentacaoPet = input(f"Digite a alimentação de {nomePet}: ")
    print("\n")

    pets.append(Pets(nomePet, idadePet, racaPet, portePet, alimentacaoPet))

for i, bichos in enumerate(pets) :
    print(f"Nome do {i + 1}º pet: {bichos.nome}")
    print(f"Idade do {i + 1}º pet: {bichos.idade}")
    print(f"Raça do {i + 1}º pet: {bichos.raca}")
    print(f"Porte do {i + 1}º pet: {bichos.porte}")
    print(f"Alimentação do {i + 1}º pet: {bichos.alimentacao}")
    print("\n")


