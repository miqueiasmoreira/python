from random import randint
cont = 0
print('Os valores sorteados foram:', end=' ')
while True:
    valores = randint(0, 9)
    cont += 1
    if cont < 6:
        print(f'{valores}', end=' ')
        if cont == 1:
            valorMaior = valores
            valorMenor = valores
        else:
            if valores > valorMaior:
                valorMaior = valores
            if valores < valorMenor:
                valorMenor = valores
    else:
        break
print()
print(f'O maior valor sorteado foi {valorMaior}')
print(f'O menor valor sorteado foi {valorMenor}')

valores = tuple(randint(1, 9) for i in range(5))
print(f'Os valores sorteados foram: {valores}')
print(f'O Maior valor é {max(valores)}')
print(f'O menor valor é {min(valores)}')