while True:
    question = 'S'
    while question in 'Ss':
        number = int(input('Digite um número: '))
        print('Valor adicionado com sucesso...')
        question = str(input('Quer continuar? [S/N] ')[0])
        if question in 'Ss':
            number = int(input('Digite um número: '))
            print('Valor adicionado com sucesso...')
            question = str(input('Quer continuar? [S/N] ')[0])
        if question in 'Nn':
            break
    break
print('END')