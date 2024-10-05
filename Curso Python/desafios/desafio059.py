

valor1 = float(input('Valor 1: '))
valor2 = float(input('Valor 2: '))

print(f'''
      [1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Novos números
      [5] Sair do programa''')

option = int(input('Digite sua opção: '))

while option != 5:
    if option == 1:
        print(f'A soma entre {valor1} e {valor2} é {valor1 + valor2}')
        break
    elif option == 2:
        print(f'A multiplicação entre {valor1} e {valor2} é {valor1 * valor2}')
        break
    elif option == 3:
        if valor1 > valor2:
            print(f'O valor1 {valor1} é maior que o valor2 {valor2}')
            break
        else:
            print(f'O valor2 {valor2} é maior que o valor1 {valor1}')
            break
    elif option == 4:
        valor1 = float(input('Valor 1: '))
        valor2 = float(input('Valor 2: '))
        break
    elif option == 5:
        print('Programa encerrado')

    