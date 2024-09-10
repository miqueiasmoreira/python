salario_antigo = float(input("Qual é o salário? "))
if (salario_antigo >= 1250.00):
    salario_novo = salario_antigo + (salario_antigo * 0.10)
else:
    salario_novo = salario_antigo + (salario_antigo * 0.15)
print(f"Quem ganhava R${salario_antigo:.2f} passa a ganhar R${salario_novo:.2f}") 