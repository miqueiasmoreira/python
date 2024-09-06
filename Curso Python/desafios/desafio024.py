nome_cidade = str(input("Nome da cidade: "))
nome_cidade = nome_cidade.upper()
pesquisa = nome_cidade.find('SANTO')
if (pesquisa == 0):
    print(f"A cidade de {nome_cidade} possui o 'SANTO' no nome")
else:
    print(f"A cidade de {nome_cidade} não possui o 'SANTO' no nome")
    

