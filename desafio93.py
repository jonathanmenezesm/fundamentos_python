# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

resumo = dict()
nome = input('Qual o nome do jogador: ')
n_partidas = int(input('Quantas partidas o jogou: '))
gols_partidas = int(input('Quantos gols nas partidas: '))
resumo['nome'] = nome
resumo['n_partidas'] = n_partidas
resumo['gols_partidas'] = gols_partidas
print(resumo)