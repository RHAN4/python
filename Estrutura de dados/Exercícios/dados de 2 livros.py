import os

from dataclasses import dataclass

os.system("cls || clear")

class Livro:
    def __init__ (self, titulo, autor, NumPag, preco):
        self.titulo = titulo
        self.autor = autor
        self.NumPag = NumPag
        self.preco = preco

#Constante:
QUANTIDADE_LIVROS = 2

#Vetor:
livros = []

for i in range (QUANTIDADE_LIVROS):
    nomeLivro = input(f"Digite o nome do {i + 1}º livro: ")
    autorLivro = input(f"Digite o nome do autor do {i + 1}º livro: ")
    PagLivro = int(input(f"Digite o número de páginas do {i + 1}º livro: "))
    PrecoLivro = float(input(f"Digite o preço do {i + 1}º livro: "))
    print("\n")
    livros.append(Livro(nomeLivro, autorLivro, PagLivro, PrecoLivro))

# for i in livros :
for i, livro in enumerate(livros) :
    print(f"Título do {i + 1}º livro: {livro.titulo}")
    print(f"Nome do autor do {i + 1}º livro: {livro.autor}")
    print(f"Número de páginas do {i + 1}º livro: {livro.NumPag}")
    print(f"Preço do {i + 1}º livro: {livro.preco}")
    print("\n")