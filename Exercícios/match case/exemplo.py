import os

os.system("cls || clear")

# Inicializando variável

resultado = 0

while True: 

# Solicitar dados para o usuário
    a = int(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    b = int(input("Digite o segundo número: "))

    match(operador):
        case "+":
            resultado = a + b
            break
        case "-":
            resultado = a - b
            break
        case "*":
            resultado = a * b
            break
        case "/":
            resultado = a / b
            break
        case _:
            print("Operador inválido.")

print(f"Resultado: {resultado}")