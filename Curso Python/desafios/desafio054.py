from datetime import date
menores = 0
maiores = 0
for c in range(1, 8):
    nascimento = int(input('Digite um ano de nascimento: ').strip())
    if (date.today().year - nascimento) < 21:
        menores += 1
    else:
        maiores += 1
print(f'{menores} são menores de idade e {maiores} são maiores de idade')