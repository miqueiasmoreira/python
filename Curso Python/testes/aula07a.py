n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d_i = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o Produto é {}, a \n Divisão é {:.3f}'.format(s, m, d), end=' ')
print('A Divisão Inteira é {}, e a Potência é {}'.format(d_i, e))