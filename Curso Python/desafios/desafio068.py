'''from random import randint
computador = randint(1, 10)
par = 'PAR'
impar = 'ÍMPAR'
resultado = ''
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
valor = int(input('Diga um valor: ').strip())
parOuImpar = str(input('Par ou ímpar? [P/I] ').strip().upper())
total = valor + computador

if total % 2 == 0:
    resultado = par
else:
    resultado = impar
    
print(f'Você jogou {valor} e o computador {computador}. Total de {total} DEU {resultado}')

if resultado == par:
    resultado = 'P'
else:
    resultado = 'I'
    
if resultado == parOuImpar:
    print('Parabéns, você ganhou! Vamos jogar de novo!')
else:
    print('Você perdeu!')'''

'''from random import randint
computador = cont = 0
par = 'PAR'
impar = 'ÍMPAR'
resultado = ''
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
while True:
    computador = randint(1, 10)
    valor = int(input('Diga um valor: ').strip())
    parOuImpar = str(input('Par ou ímpar? [P/I] ').strip().upper())
    print('--' * 20)
    total = valor + computador
    
    if total % 2 == 0:
        resultado = par
    else:
        resultado = impar
        
    print(f'Você jogou {valor} e o computador {computador}. Total de {total} DEU {resultado}')

    if resultado == par:
        resultado = 'P'
    else:
        resultado = 'I'
        
    if resultado == parOuImpar:
        print('--' * 20)
        print('Parabéns, você ganhou! Vamos jogar de novo!')
        cont += 1
    else:
        print('=-=' * 20)
        print(f'Você perdeu! Após ganhar {cont} vezes!')
        break'''
        
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: ').strip())
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            prit('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
if v > 1:
    print(f'Game OVER! Você venceu {v} vezes.')
elif v == 0:
    print('GAME OVER! Você não venceu nenhuma.')
else:
    print(f'Game OVER! Você venceu {v} vez.')