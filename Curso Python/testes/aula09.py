frase = 'Curso em video Python'
print("-".join(frase))

dados_do_usuario = "Bob, 25, Mecânico"
lista = dados_do_usuario.split(",")
nome = lista[0]
idade = lista[1]
profissao = lista[2]
print(f'Olá {nome} sejá bem vindo, você tem {idade} anos e trabalha como {profissao} que legal!')
