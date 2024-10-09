n = int(input('Quantos termos você quer mostrar? ').strip())
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
mais = 3
total = n
while mais != 0:
    total = total + mais
    while cont < total:
        t3 = t1 + t2
        print(f' -> {t3}', end='')
        t1 = t2
        t2 = t3
        cont += 1
    print(' -> PAUSA')
    mais = int(input('Quantos mais você quer? ').strip())
print(' -> FIM')
