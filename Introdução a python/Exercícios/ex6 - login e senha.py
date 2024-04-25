import os

os.system ("cls || clear")

print("- Solicitando dados -")
login = str(input("Insira o seu login: "))
senha = str(input("Insira a sua senha: "))

print("\n")
if login == "ricardo" and senha == "1234":
    print("Seja bem vindo!")
else: 
    print("Login ou senha inválidos.")