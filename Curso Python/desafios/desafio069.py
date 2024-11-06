maior = masculino = feminino = 0
while True:
    print('---' * 10)
    print('CADASTRE UMA PESSOA')
    print('---' * 10)
    idade = int(input('Idade: ').strip())
    sexo = str(input('Sexo: [M/F] ').strip().upper()[0])
    print('---' * 10)
    if idade >= 18:
            maior += 1
    if sexo == 'M':
            masculino += 1
    if sexo == 'F' and idade < 20:
            feminino += 1
    resposta = str(input('Quer continuar? [S/N]').strip().upper()[0])
    if resposta == 'N':
            break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {masculino} homens cadastrado')
print(f'E temos {feminino} mulher com menos de 20 anos')