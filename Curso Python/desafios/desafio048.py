
for c in range(1, 500, 2):
    if c % 3 == 0:
        print(c)
print('---FIM---')

soma = 0
cont = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        cont += 1
        soma += x
print(f'A soma de todos os {cont} valores solicitados é {soma}')