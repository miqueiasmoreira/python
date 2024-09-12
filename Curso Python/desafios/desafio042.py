print("-=-" * 20)
print("Analisador de triângulos")
print("-=-" * 20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
segmento = (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2)
if (r1 == r2 and r3 and segmento == True):
    print("EQUILÁTERO, todos os lados iguais")
elif (r1 == r2 or r1 == r3 or r2 == r3 and segmento == True):
    print("ISÓSCELES, dois lados iguais")
elif (r1 != r2 or r1 != r3 or r2 != r3 and segmento == True):
    print("ESCALENO, todos os lados diferentes")
else:
    print("Nenhum formou um triangulo")
