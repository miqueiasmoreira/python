import random
from time import sleep
# Criar as opções do jogo

op1 = 'PEDRA'
op2 = 'PAPEL'
op3 = 'TESOURA'
lista = [op1, op2, op3]

print("Suas opções:")
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")

# Receber opção do jogador

option = int(input("Qual é a sua jogada? ").strip())

# Mostrar mensagem JO KEN PO!!!

sleep(0.5)
print("JO")
sleep(0.6)
print("KEN")
sleep(0.7)
print("PO!!!")
sleep(0.2)
# Mostrar resultado!

computador = random.choice(lista)
jogador = 'NADA'

print("\033[1;35m-=-\033[m" * 20)
print(f"Computador jogou {computador}")
if option == 0:
    print(f"Jogador jogou PEDRA")
    jogador = 'PEDRA'
elif option == 1:
    print("Jogador jogou PAPEL")
    jogador = 'PAPEL'
elif option == 2:
    print("Jogador jogou TESOURA")
    jogador = 'TESOURA'
else:
    print("ERRO")
print("\033[1;35m-=-\033[m" * 20)

# Resultado de quem venceu

if computador == 'PEDRA' and jogador == 'TESOURA' or computador == 'TESOURA' and jogador == 'PAPEL' or computador == 'PAPEL' and jogador == 'PEDRA':
    print("COMPUTADOR VENCE")
elif computador == jogador:
    print("EMPATE")
else:
    print("JOGADOR VENCE")
print("---FIM---")