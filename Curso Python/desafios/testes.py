n = int(input('Quantos termos você quer mostrar? ').strip())
t1 = 0
t2 = 1
print (f'{t1} -> {t2}', end='')
c = 3
while c <= n:
    t3 = t2 + t1
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1
print(' -> FIM')