import random

num = int(input('Digite um valor de 0 a 5: '))
num_escolha = random.randint(0, 5)

while num != num_escolha:
    print('Não pensei nesse número...')
    num = int(input('Digite um valor de 0 a 5: '))
print('Parabens você advinhou o número que eu pensei!')