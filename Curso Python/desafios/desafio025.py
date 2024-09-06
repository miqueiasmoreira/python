nome_pessoa = str(input("Digite seu nome com sobrenome: "))
nome_pessoa = nome_pessoa.upper()
pesquisa_nome = nome_pessoa.find('SILVA')
if (pesquisa_nome >= 0):
    print(f"Seu nome {nome_pessoa} possui o sobrenome 'SILVA'.")
else:
    print(f"Seu nome {nome_pessoa} não possui o 'SILVA'")