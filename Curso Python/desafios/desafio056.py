
somaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totalMulher20 = 0
for p in range(1, 5):
    print(f'----- {p}° PESSOA -----')
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: ').strip())
    sexo = str(input('Sexo [M/F]: ').strip())
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher20 += 1
mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é de {mediaIdade:.0f} anos')
print(f'O homem mais velho tem {maiorIdadeHomem} e se chama {nomeVelho}')
print(f'Ao todo são {totalMulher20} mulher com menos de 20 anos')