# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

times_brasileirao_2025 = ("Nulo", "Palmeiras", "Flamengo", "Cruzeiro", "Mirassol", "Bahia", "Botafogo", "Fluminense", "São Paulo", "Atlético-MG", "Vasco", "Red Bull Bragantino", "Ceará", "Corinthians", "Grêmio", "Internacional", "Vitória", "Santos", "Juventude", "Fortaleza", "Sport")

# A) Apenas os 5 primeiros colocados.
print('Os primeiros 5 colocados são:')
posicao = 0
for _ in range(1, 6):
    posicao += 1
    print(f'{posicao}º Lugar - {times_brasileirao_2025[posicao]}')

# B) Os últimos 4 colocados da tabela.
print('\nOs 4 últimos colocados são:')
posicao = 16
for z4 in range(17, 21):
    posicao += 1
    print(f'{posicao}º Lugar - {times_brasileirao_2025[posicao]}')

# C) Uma lista com os times em ordem alfabética.
print('\nEsses são os times em ordem alfabética: ')
print(sorted(times_brasileirao_2025))

# D) Em que posição na tabela está o time do Fluminense.

print(f'\nO Fluminense está na {times_brasileirao_2025.index("Fluminense")}ª posição da tabela!')
