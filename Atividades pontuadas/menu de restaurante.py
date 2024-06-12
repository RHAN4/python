import os
import time

def cardapio():
    os.system ("cls || clear")
    print(" - CARDÁPIO - ")
    print("""
    1 - Picanha - R$ 25,00
    2 - Lasanha - R$ 20,00
    3 - Strogonoff - R$ 18,00
    4 - Macarrão - R$ 17,00
    5 - Bife Acebolado - R$ 15,00
    6 - Hambúrguer - R$ 10,00
    7 - Pão com ovo - R$ 5,00
    """)
def opcoes():
    print("Digite 0 caso queira parar de pedir.")
    
def TabPagamento():
    print("""
    1 - Pagamento à vista.
    2 - Pagamento com cartão de crédito.
    """)

pratos = []
soma = 0

while True:
    cardapio()
    opcoes()
    print("\n")
    opcao = int(input("Digite o código da comida desejada: "))
    
    match(opcao):
        case 1:
            pedido = "Prato escolhido: Picanha."
            pratos.append(pedido)
            print("Valor: R$ 25,00.")
            soma += 25
        case 2 :
            pedido = "Prato escolhido: Lasanha."
            pratos.append(pedido)
            print("Valor: R$ 20,00.")
            soma += 20
        case 3 :
            pedido = "Prato escolhido: Strogonoff."
            pratos.append(pedido)
            print("Valor: R$ 18,00.")
            soma += 18
        case 4 :
            pedido = "Prato escolhido: Macarrão."
            pratos.append(pedido)
            print("Valor: R$ 17,00.")
            soma += 17
        case 5 :    
            pedido = "Prato escolhido: Bife Acebolado."
            pratos.append(pedido)
            print("Valor: R$ 15,00.")
            soma += 15
        case 6 :    
            pedido = "Prato escolhido: Hambúrguer."
            pratos.append(pedido)
            print("Valor: R$ 10,00.")
            soma += 10
        case 7 :    
            pedido = "Prato escolhido: Pão com ovo."
            pratos.append(pedido)
            print("Valor: R$ 5,00.")
            soma += 5
        case 0 :
            break
        case _ :
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            os.system ("clear")
            
    
    opcao = input("Deseja pedir mais alguma coisa? ")
    opcao = opcao.upper()
    print("Digite SIM ou NÃO")
    if opcao != "SIM":
        break

while True: 
    TabPagamento()
    pagamento = int(input("Insira a forma de pagamento: "))
        
    match(pagamento):
        case 1 :
            pagamento = 'À vista'
            desconto = soma * 0.1
            total = soma - desconto
            break
        case 2:
            pagamento = 'No cartão'
            desconto = soma * 0.1
            total = soma + desconto
            break
        
print(f"{pratos}")
print(f"Forma de pagamento: {pagamento}")
print(f"Preço do produto: R$ {soma}")
print(f"Valor do desconto ou taxa: R$ {desconto}")
print(f"Valor final: R$ {total}")