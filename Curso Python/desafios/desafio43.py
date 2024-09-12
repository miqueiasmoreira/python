from math import pow
peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / pow(altura, 2)
print(imc)
if (imc < 18.5):
    print("Abaixo do peso")
elif (imc >= 18.5 and imc < 25):
    print("Peso ideal")
elif (imc == 25 or imc < 30):
    print("Sobrepeso")
elif (imc == 30 or imc < 40):
    print("Obesidade")
else:
    print("Obesidade Mórbida")