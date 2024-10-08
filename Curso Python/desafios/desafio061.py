'''print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

termo = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo, razao):
        print(c, end=' → ')
print('ACABOU')'''

print('-=' * 20)
print("TERMOS DE UMA PA")
print('-=' * 20)

termo = int(input('Primeiro termo: ').strip())
razao = int(input('Digite a razão: ').strip())
contador = 0

while contador < 10:
    print(termo, end=' → ')
    termo += razao
    contador += 1
print('ACABOU')

