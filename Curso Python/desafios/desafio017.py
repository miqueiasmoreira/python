import math
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
#print(f'A Hipotenusa é {(ca**2 + co**2) ** (1/2):.2f}')
print(f'A Hipotenusa é {math.hypot(co, ca):.2f}')
