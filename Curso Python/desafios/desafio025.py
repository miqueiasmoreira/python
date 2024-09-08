nome_pessoa = str(input("Digite seu nome com sobrenome: ")).strip().upper()
pesquisa_nome = nome_pessoa.find('SILVA')
if (pesquisa_nome >= 0):
    print(f"Seu nome {nome_pessoa} possui o sobrenome 'SILVA'.")
else:
    print(f"Seu nome {nome_pessoa} não possui o 'SILVA'")
    
nome_pessoa = str(input("Digite seu nome com sobrenome: ")).strip().upper()
print(f"Seu nome tem 'SILVA'? {'SILVA' in nome_pessoa}")