'''import random

num = int(input('Digite um valor de 0 a 5: '))
num_escolha = random.randint(0, 5)

while num != num_escolha:
    print('Não pensei nesse número...')
    num = int(input('Digite um valor de 0 a 5: '))
print('Parabens você advinhou o número que eu pensei!')'''

from random import randint
computador = randint(0, 3)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 3')
print('Será que você consegue advinhar qual foi?')

acertou = False
palpites = 0

while not acertou:
    print(acertou)
    jogador = int(input('Qual é seu palpite? ').strip())
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
    