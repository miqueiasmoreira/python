
num = int(input('Digite um número: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[1;32m', end='')
        total += 1
    else:
        print('\033[1;31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO núemro {num} foi divisivel {total} vezes')
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')