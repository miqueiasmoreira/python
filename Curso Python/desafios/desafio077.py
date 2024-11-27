tupla = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')

vogals = ('a', 'e', 'i', 'o', 'u')

for words in tupla:
    print(f'Na palavra {words.upper()} temos', end=' ')

    for l in words:
        if l.lower() in vogals:
            print(f'\033[1;33m{ l.lower()}\033[m', end=' ')
    print()