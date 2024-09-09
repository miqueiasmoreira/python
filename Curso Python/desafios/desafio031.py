distancia = int(input("Qual a distância a ser percorrida? "))
if (distancia <= 200):
    print(f"Sua viagem custara R${distancia * 0.50:.2f}")
else:
    print(f"Sua viagem custará R${distancia * 0.45:.2f}")
print("---FIM---")

distancia = int(input("Qual a distância a ser percorrida? "))
if (distancia <= 200):
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"Sua viagem custará R${preco:.2f}")
print("---FIM---")

distancia = int(input("Qual a distância a ser percorrida? "))
preco = (distancia * 0.50 if distancia <= 200 else distancia * 0.45)
print(f"Sua viagem custará R${preco:.2f}")
print("---FIM---")