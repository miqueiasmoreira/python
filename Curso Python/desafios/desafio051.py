print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

termo = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo, razao):
        print(c, end=' → ')
print('ACABOU')