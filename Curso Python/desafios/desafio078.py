valores = []
maior = 0
menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'O menor valor é {min(valores)} na posicão', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ')
print(f'O maior valor é {max(valores)} na posição', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ')
print()












'''


if c == 1:
        maior = 0
        menor = 0
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
            
            print(f'O maior valor foi {max(valores)}')
print(f'O menor  valor foi {min(valores)}')
print(f'teste: {enumerate(max(valores))}')'''