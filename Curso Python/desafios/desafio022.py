nome = str(input("Digite seu nome completo: "))
print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ", "")))
lista_primeiro_nome = nome.split(" ", 1)
primeiro_nome = lista_primeiro_nome [0]
print(len(primeiro_nome))
print(lista_primeiro_nome)


