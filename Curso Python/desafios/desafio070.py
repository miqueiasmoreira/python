print('---' * 10)
print('LOJA SUPER BARATÃO')
print('---' * 10)

totCompra = maiorMil = cont = menor = 0

while True:
    nomeProduto = str(input('Nome do Produto: ').strip())
    preco = float(input('Preço: R$').strip())
    
    totCompra += preco
    if preco > 1000:
        maiorMil += 1
        
    if menor == 0 or preco < menor:
        menor = preco
        nomeMenor = nomeProduto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if resp == 'N':
        break
    
print('---' * 3 + ' FIM DO PROGRAMA ' + '---' * 3)

print(f'O total da compra foi R${totCompra:.2f}')
print(f'Temos {maiorMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi a {nomeMenor} que custa R${menor:.2f}')