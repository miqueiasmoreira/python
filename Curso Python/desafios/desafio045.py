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

print("\033[1;35m-=-\033[m" * 20)
print(f"Computador jogou {computador}")
if option == 0:
    print(f"Jogador jogou PEDRA")
elif option == 1:
    print("Jogador jogou PAPEL")
elif option == 2:
    print("Jogador jogou TESOURA")
else:
    print("ERRO")
print("\033[1;35m-=-\033[m" * 20)

if computador == 'PEDRA' and option == 'TESOURA' or computador == 'TESOURA' and option == 'PAPEL' or computador == 'PAPEL' and option == 'PEDRA':
    print("COMPUTADOR VENCE")
elif computador == option:
    print("EMPATE")
print("---FIM---")