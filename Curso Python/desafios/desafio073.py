times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Internacional', 'São Paulo', 'Cruzeiro', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Corinthians')

print(f'Lista de times do Brasileirão: {times}')

print(f'Os 5 primeiros são {times[0:5]}')

print(f'Os 4 últimos são {times[-4:]}')

print(f'Times em ordem alfabética: {sorted(times)}')

cont = 0
for c in times:
    cont += 1
    if c == 'Corinthians':
        break
print(f'O Corinthias está na {cont} posição')