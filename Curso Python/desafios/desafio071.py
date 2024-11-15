'''print('---' * 10)
print('BANCO CEV')
print('---' * 10)

valor = int(input('Que valor você quer sacar? R$').strip())

while True:
    if valor >= 50:
        print(f'Total de {valor // 50:.0f} cédulas de R$50')
    valor = valor % 50
    if valor >= 20 and valor % 20 != 0:
        print(f'Total de {valor // 20:.0f} cédulas de R$20')
    valor = valor % 20
    if valor >= 10 and valor % 10 != 0:
        print(f'Total de {valor // 10:.0f} cédulas de R$10')
    valor = valor % 10
    if valor >= 1:
        print(f'Total de {valor // 1:.0f} cédulas de R$1')
    valor = valor % 1
    if valor == 0:
        break'''
        
valor = int(input('Que valor você quer sacar? R$').strip())
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

    