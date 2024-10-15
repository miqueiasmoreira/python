
'''Digite um número: 
Quer continuar?[S/N] 

Você digitou {} números e a média foi {}
O maior valor foi {} e o menor foi {}'''
n = cont = soma = 0
n = int(input('Digite um número: '))

while n != 'Nn':
    soma += n
    cont += 1
    p = str(input('Quer continuar?[S/N] '))
    if p in 'Ss':
        n = int(input('Digite um número: '))
    else:
        print(f'Você digitou {cont} números e a média foi {soma / cont:.2f}')
        break