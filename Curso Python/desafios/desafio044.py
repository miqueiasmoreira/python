price = float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO")
print("[1] À vista (Dinheiro ou Cheque) com 10% de desconto.")
print("[2] À vista (Cartão) com 5% de desconto.")
print("[3] 2x (Cartão) sem juros")
print("[4] 3x ou mais (Cartão) 20% de juros")
price_option = float(input("Qual é a opção de pagamento? "))
if (price_option == 1):
    print(f"Sua compra de R${price:.2f} vai custar no final R${price - (price * 0.1):.2f}")
elif (price_option == 2):    
    print(f"Sua compra de R${price:.2f} vai custar no final R${price - (price * 0.05):.2f}")
elif (price_option == 3):    
    print(f"Sua compra de R${price:.2f} vai custar no final 2 parcelas de R${price / 2:.2f}")
elif (price_option == 4):
    qtd_parcela = int(input("Quantas parcelas?"))
    print(f"Sua compra será parcelada em {qtd_parcela}x de R${(price + price * 0.2) / qtd_parcela:.2f} com JUROS")
    print(f"Sua compra de R${price} vai custar R${(price + price * 0.2):.2f} no final")
else:
    print("ERRO")
    
    
    
    
    
    