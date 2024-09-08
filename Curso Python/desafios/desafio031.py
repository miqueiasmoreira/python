distancia = int(input("Qual a distância a ser percorrida? "))
if (distancia <= 200):
    print(f"Sua viagem custara R${distancia * 0.50}")
else:
    print(f"Sua viagem custará R${distancia * 0.45}")
print("---FIM---")