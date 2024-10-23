from random import randint
computador = randint(1, 10)
par = 'PAR'
impar = 'ÍMPAR'
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
valor = int(input('Diga um valor: ').strip())
parOuImpar = str(input('Par ou ímpar? [P/I] ').strip().upper())
total = valor + computador
print(f'Você jogou {valor} e o computador {computador}. Total de {total} DEU {if total % 2 == 0: print(par) else: print(impar)}')
