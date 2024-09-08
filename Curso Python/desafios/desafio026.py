frase = str(input("Digite uma frase: ")).strip().lower()
print(f"A quantidade de letras 'A' no texto é: {frase.count('a')}")
print(f"A primeira letra 'A' foi encontrada na posição: {frase.find('a')+1}")
print(f"A última letra 'A' apareceu na posição: {frase.rfind('a')+1}")