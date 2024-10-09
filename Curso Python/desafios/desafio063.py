
'''qtdTermo = int(input('Quantos termos você quer mostrar? ').strip())

contador = 0

anterior = 0
proximo = 1

while contador < qtdTermo:
    print(anterior, end=' --> ')
    proximo += anterior
    anterior = proximo - anterior
    contador += 1
print('FIM')'''

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? ').strip())

t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')