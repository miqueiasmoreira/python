nome = str(input("Digite seu nome completo: ")).strip()
print(f"Seu nome em Maiúsculas: {nome.upper()}")
print(f"Seu nome em Minúsculas: {nome.lower()}")
print(f"Seu nome tem {len(nome.replace(" ", ""))} letras")
lista_primeiro_nome = nome.split(" ", 1)
primeiro_nome = lista_primeiro_nome [0]
print(f"Seu primeiro nome tem {len(primeiro_nome)} letras")
print(lista_primeiro_nome)

nome = str(input("Digite seu nome completo: ")).strip()
print(f"Seu nome em Maiúsculas: {nome.upper()}")
print(f"Seu nome em Minúsculas: {nome.lower()}")
print(f"Seu nome tem {(len(nome) - nome.count(' '))} letras")
print(f"Seu primeiro nome tem {nome.find(' ')} letras")