def calcular_notas(valor):
    # Lista de valores das notas disponíveis
    notas = [100, 50, 20, 10, 5, 2, 1]
    resultado = []

    for nota in notas:
        quantidade = valor // nota  # Calcula quantas notas são necessárias
        resultado.append(quantidade)  # Armazena o resultado
        valor %= nota  # Atualiza o valor restante

    return resultado

def exibir_resultado(valor, notas):
    print(valor)
    valores_notas = [100, 50, 20, 10, 5, 2, 1]

    for quantidade, nota in zip(notas, valores_notas):
        print(f"{quantidade} nota(s) de R$ {nota},00")

# Leitura do valor de entrada
valor = int(input())
notas_calculadas = calcular_notas(valor)
exibir_resultado(valor, notas_calculadas)
