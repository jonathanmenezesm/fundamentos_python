# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


dados = list()

while True:
    jogador = dict()
    nome = input('Qual o nome do jogador: ')
    n_partidas = int(input('Quantas partidas o jogou: '))
    gols_partidas = int(input('Quantos gols nas partidas: '))
    jogador['nome'] = nome
    jogador['n_partidas'] = n_partidas
    jogador['gols_partidas'] = gols_partidas
    dados.append(jogador.copy())

    if input('Deseja continuar? [S/N] ').upper().strip() == 'N':
        break
    else:
        continue

for jogador in dados:
    print(f"O jogador {jogador['nome']} fez {jogador['gols_partidas']} gols em {jogador['n_partidas']} partidas.")