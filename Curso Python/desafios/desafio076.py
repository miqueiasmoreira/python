print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.20,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for pos in range(0, len(listagem), 2):
    print(f'{listagem[pos]:.<30}' + f' R$ {listagem[pos+1]:>7.2f}')