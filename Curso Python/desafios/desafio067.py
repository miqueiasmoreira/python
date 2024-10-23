'''num = int(input("Digite um número: ").strip())

for c in range(1, 10+1):
    print(f'{num} x {c} = {num * c}')
print('FIM')'''

n = cont = 0
while True:
    cont = 0
    n = int(input('Digite um valor para ver a tabuada: '))
    if n < 0:
        break
    while cont < 11:
        print(f'{n} x {cont} = {n * cont}')
        cont += 1
print('Programa interrompido')