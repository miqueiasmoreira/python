sex = str(input('Digite o sexo [M/F]: ').strip().upper())

while sex != 'M' and sex != 'F':
    print('Valor inválido!')
    sex = str(input('Digite o sexo [M/F]: ').strip().upper())
    '''sex_1 = str(input('Digite o sexo [M/F]: ').strip().upper())
    sex = sex_1'''