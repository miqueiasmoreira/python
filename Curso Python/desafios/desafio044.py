price = float(input("Valor do produto: "))
if (price > 0):
    print(f"À vista (Dinheiro ou Cheque): {} com 10% de desconto.")
    print(f"À vista (Cartão): {} com 5% de desconto.")
    print(f"2 vezes (Cartão: {} sem juros")
    print(f"3 vezes ou mais (Cartão {} 20% de juros)")