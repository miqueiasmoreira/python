n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: ').strip())
    soma += n
    cont += 1
print(f'Você digitou {cont - 1} números e a soma entre eles foi {soma - 999}.')
print('FIM')
