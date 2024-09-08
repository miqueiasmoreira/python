import random
lista = [0, 1, 2, 3, 4, 5]
print("Olá tente descobrir qual número estou pensando de 0 a 5 =)")
num = int(input("Digite um valor de 0 a 5: "))
num_escolhido = random.randint(0, 5)
if (num_escolhido == num):
    print(f"Parabéns você acertou, o número que pensei foi o {num}")
else:
    print(f"Incorreto, o número que pensei foi o {num_escolhido} e você digitou o {num}")
print("---FIM---")