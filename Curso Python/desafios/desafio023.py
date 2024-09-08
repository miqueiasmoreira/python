numero = (input("Digite um valor de 0 a 9999: "))
print(f"unidade:{numero[3:4]}")
print(f"dezena:{numero[2:3]}")
print(f"centena:{numero[1:2]}")
print(f"milhar:{numero[0:1]}")

numero = int(input("Digite um valor de 0 a 9999: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f"Analisando o número: {numero}")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")