vel = int(input('Velocidade do veículo: '))
if (vel > 80):
    print("Multado! Veiculo transitando acima da velocidade permitida.")
    print(f"Valor da multa: R$ {(vel-80) * 7}")
print("---FIM---")