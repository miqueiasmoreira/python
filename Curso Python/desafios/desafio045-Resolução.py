# RESOLUÇÃO DO PROFESSOR GUANABARA
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[0] PEDRA
[1] PAPEL
[3] TESOURA''')
jogador = int(input("Qual é a sua jogada? ").strip())

sleep(0.2)
print("JO")
sleep(0.5)
print("KEN")
sleep(0.7)
print("PO!!!")
sleep(0.5)

print("-=" * 11)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("-=" * 11)

# Guanabara parte:

if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA!")
print("---FIM---")

#Minha parte otimizando linhas

if (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
    print("COMPUTADOR VENCE")
elif computador == jogador:
    print("EMPATE")
else:
    print("JOGADA INVÁLIDA!")