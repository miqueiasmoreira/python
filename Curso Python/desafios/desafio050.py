soma = 0

for c in range(1, 6+1):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
    else:
        num = 0
print(f"A soma dos 6 valores é de {soma}")
