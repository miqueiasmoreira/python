a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
c = int(input("Valor 3: "))
# Verificando quem é menor
menor = a
if (b < a and b < c):
    menor = b
elif (c < a and c < b):
    menor = b
# Verificando quem é o maior
maior = a
if (b > a and b > c):
    maior = b
elif (c > a and c > b):
    maior = c
print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")