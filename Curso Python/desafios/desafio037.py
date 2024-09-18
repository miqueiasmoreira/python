num = int(input("Digite um número inteiro qualquer: "))
print("Escolha uma das bases para conversão")
print("[1] BINÁRIO")
print("[2] OCTAL")
print("[3] HEXADECIMAL")
opcao = int(input("Sua decisão: "))
if (opcao == 1):
    print(f"{num} convertido para BINÁRIO é igual a {bin(num) [2:]}")
elif (opcao == 2):
    print(f"{num} convertido para OCTAL é igua a {oct(num) [2:]}")
elif (opcao == 3):
    print(f"{num} convetido para HEXADECIMAL é igual a {hex(num) [2:]}")
else:
    print("Opção invalida tente novamente")