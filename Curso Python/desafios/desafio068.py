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

from random import randint
computador = randint(1, 10)
par = 'PAR'
impar = 'ÍMPAR'
resultado = ''
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
while True:
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
        print('Você perdeu!')
        break