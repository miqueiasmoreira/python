 #Ler o tipo de chá
 
T = int(input().strip())

# Ler a resposta dos competidores

respostas = list(map(int, input().strip().split()))

# Inicializar o contador de acertos

acertos = 0

# Verificar quantos concorrentes acertaram

for resposta in respostas:
    if resposta == T:
        acertos += 1
        
# Exibir o número de acertos

print(Acertos)
    



