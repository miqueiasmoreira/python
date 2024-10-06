'''from math import factorial

n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O Fatorial de {n} é {f}')'''

numero = int(input('Digite um número para calcular seu Fatorial: ').strip())
print(f'Calculando {numero}! = ', end='')
contador = numero
fatorial = 1
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador -= 1
print(f'{fatorial}')
