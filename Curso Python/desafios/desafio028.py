import random
print("Olá tente descobrir qual número estou pensando de 0 a 5 =)")
num = int(input("Digite um valor de 0 a 5: "))
num_escolhido = random.randint(0, 5)
if (num_escolhido == num):
    print(f"Parabéns você acertou, o número que pensei foi o {num}")
else:
    print(f"Incorreto, o número que pensei foi o {num_escolhido} e você digitou o {num}")
print("---FIM---")

from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador escolher um número de 0 a 5
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente advinhar...")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? ")) #Jogador tenta advinhar o número
print("PROCESSANDO...")
sleep(2)
if (computador == jogador):
    print("Parabéns! Você me venceu!")
else:
    print(f"Ganhei! Eu escolhi o número {computador} e você colocou o {jogador}")