n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')



n = cont = 0
while True:
    cont = 0
    n = int(input('Digite um valor para ver a tabuada: '))
    while cont < 11:
        if n < 0:
            break
        print(f'{n} x {cont} = {n * cont}')
        cont += 1
    if n < 0:
        break
print('Programa interrompido')