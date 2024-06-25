# Define:

QUANTIDADE_NOTAS = 3

# Função para calcular a média:
def calcularMedia(notas):
    soma = 0
    for i in range (QUANTIDADE_NOTAS):
        soma += notas [i]
    return soma / QUANTIDADE_NOTAS
    
# Função para vefificar a situação do aluno:
def verificarSituacao(media):
    resultado : str
    if media >= 7:
        resultado = "Aprovado!"
    else:
        resultado = "Reprovado."
    return resultado
    
# Função para mostrar o resultado: 
def mostrarResultado(notas):
    media = calcularMedia(notas)
    print(f"\nMédia: {media:.2f}")
    print(f"Situação do aluno: {verificarSituacao(media)}")
    
# Vetor:
notas = []

# Pedir as notas ao usuário:
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

# Chamando a função para mostrar o resultado: 
mostrarResultado(notas)