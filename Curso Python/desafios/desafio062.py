'''termo = int(input('Primeiro termo: ').strip())
razao = int(input('Digite a razão: ').strip())
contador = 0
escolha = 0
termos = 0
while contador < 10:
    print(termo, end=' → ')
    termo += razao
    contador += 1
    termos += 1
print('PAUSA')
pergunta = int(input('Quantos termos você quer mostras a mais? ').strip())

while True:
    contador = 0
    termos += 1
    while contador < pergunta:
        print(termo, end=' → ')
        termo += razao
        contador += 1
    print('PAUSA')
    pergunta = int(input('Quantos termos você quer mostras a mais? ').strip())
    
    if pergunta <= 0:
        print(f'Progressão finalizada com {termos} termos mostrados')
        break'''
        
termo = int(input('Primeiro termo: ').strip())
razao = int(input('Digite a razão: ').strip())
contador = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador < total:
        print(termo, end=' → ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quanos termos você quer mostras a mais? ').strip())
print(f'Progressão finalizada com {total} termos mostrados')