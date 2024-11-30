valores = list()
for cont in range(0, 5):
    valores.append(input(f'Digite um valor para posição {cont}: '))
    maior = menor = 0
    if cont == 1:
        maior = enumerate(valores)
        menor = enumerate(valores)
    else:
        if maior < enumerate(valores):
            maior = enumerate(valores)
        if menor > enumerate(valores):
            menor = enumerate(valores)
print(f'O menor valor é {min(valores)} na posicão {menor}')
print(f'O maior valor é {max(valores)} na posição {maior}')















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