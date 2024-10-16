
'''Digite um número: 
Quer continuar?[S/N] 

Você digitou {} números e a média foi {}
O maior valor foi {} e o menor foi {}'''

'''n = cont = soma = 0
n = int(input('Digite um número: '))

while n != 'Nn':
    soma += n
    cont += 1
    p = str(input('Quer continuar?[S/N] '))
    if p in 'Ss':
        n = int(input('Digite um número: '))
    else:
        print(f'Você digitou {cont} números e a média foi {soma / cont:.2f}')
        break'''
        
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: ').strip().upper())
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
           maior = num
        if num < menor:
            menor = num 
    resp = str(input('Que continuar? [S/N] ').strip().upper()[0])
media = soma / quant
print(f'Você digitou {quant} números e a mpedia foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
    