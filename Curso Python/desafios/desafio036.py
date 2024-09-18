casa = float(input("Valor da casa: R$"))
salario = float(input("Valor do salário: R$"))
anos = int(input("Pagará em quantos anos: "))
prestacao = casa / (anos * 12)
print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos de prestação será de R${prestacao:.2f} por parcela.")
if (prestacao > (salario * 0.3)):
    print("Você não pode financiar está casa")
else:
    print("Você pode financiar está casa")
