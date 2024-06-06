import os

os.system("cls || clear")

print(""" - FORMAS DE PAGAMENTO - 
1 - Pagamento à vista.
2 - Pagamento à prazo.
""")

desconto = 0
totalFinal = 0
total = 0

while True:
    valor = float(input("Digite o valor pago: "))
    pagamento = float(input("Digite a forma do pagamento: "))

    match(pagamento):
        case 1 :
           desconto =  valor * 0.10
           totalFinal = valor - desconto
           print("\n")
           print(f"Valor original do produto: {valor}")
           print("Forma de pagamento: À vista.")
           print(f"Valor do desconto: {desconto}")
           print(f"Total a pagar: {totalFinal}")
           break
        
        case 2 :
            qtdParcela =  int(input("Digite a quantidade de parcelas desejadas: "))
            total = valor / qtdParcela
            print("\n")
            print(f"Valor original do produto: {valor}")
            print("Forma de pagamento: À prazo.")
            print(f"Quantidade de parcelas: {qtdParcela}")
            print(f"Valor por parcela: {total:.2f}")
            print(f"Total à prazo: {valor}")
        
        case _:
            print("Algo está errado. Tente novamente.")
