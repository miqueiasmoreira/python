sex = str(input('Digite o sexo [M/F]: ').strip().upper())

while sex != 'M' and sex != 'F':
    print('Valor inválido!')
    sex = str(input('Digite o sexo [M/F]: ').strip().upper())
    '''sex_1 = str(input('Digite o sexo [M/F]: ').strip().upper())
    sex = sex_1'''
print(f'Sexo {sex} registrado com sucesso!')

sexo = str(input('Informe seu sexo: [M/F] ').strip().upper()[0])
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor informe seu sexo: ').strip().upper()[0])
print(f'Sexo {sexo} digitado com sucesso!')
