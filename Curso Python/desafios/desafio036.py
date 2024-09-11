casa = float(input("Valor da casa: "))
salario = float(input("Valor do salário: "))
anos = int(input("Pagará em quantos anos: "))
if (casa / anos > (salario * 0.3)):
    print("Você não pode financiar está casa")
else:
    print("Você pode financiar está casa")
print(salario * 0.3)
print(casa / anos)