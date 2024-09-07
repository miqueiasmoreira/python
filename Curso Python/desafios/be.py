def pesquisa_binaria(lista, item):
    esquerda = 0  # Começa no primeiro número
    direita = len(lista) - 1  # Começa no último número

    while esquerda <= direita:  # Enquanto houver números para verificar
        meio = (esquerda + direita) // 2  # Calcula o meio da lista
        chute = lista[meio]  # Pega o número no meio

        if chute == item:  # Se o meio é o número que queremos, achamos!
            return meio
        elif chute < item:  # Se o número do meio é menor que o que queremos
            esquerda = meio + 1  # Foco só na parte direita (números maiores)
        else:  # Se o número do meio é maior que o que queremos
            direita = meio - 1  # Foco só na parte esquerda (números menores)

    return -1  # Se não achou o número

lista = [1, 3, 5, 7, 9]
item = 10

resultado = pesquisa_binaria(lista, item)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}")
else:
    print("Elemento não encontrado")