# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

# Criando o dicionário com os resultados
resultados = {}

# Cada jogador joga o dado
for i in range(1, 5):
    resultados[f'jogador{i}'] = randint(1, 6)

# Mostrando os resultados
print("Resultados dos jogadores:")
for jogador, numero in resultados.items():
    print(f"{jogador} tirou {numero}")

# Montando ranking
ranking = []
for jogador, numero in resultados.items():
    ranking.append((jogador, numero))

#está organizando levando em consideração o índice 1 (x: 'x[1]') - 1º x é a chave, 2º x é o valor!
ranking.sort(key = lambda x:x[1] ,reverse=True)
print('-'*15 + 'Ranking' + '-'*15)

for posicao, (jogador, numero) in enumerate(ranking):
    print(f'{posicao+1} Lugar - {jogador} com {numero}')
    sleep(1)