# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo numa lista composta.
#use timer para exibir os jogos zerados
#os numeros nao podem se repetir no mesmo jogo




from random import randint
from time import sleep

# 1 - Perguntar quantos jogos serao gerados
quantidade_jogos = int(input('Quantos jogos deseja gerar: '))
jogos = []

while len(jogos) < quantidade_jogos:
    jogo = []
    # 2 - Sortear 6 numeros de 1 a 60 e cadastrar esses numeros em uma lista composta
    for n in range(0, 6):
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogos.append(jogo)

#Mostrando cada jogo com timer, pulando linhas:
contador = 0
for c in range(0, quantidade_jogos):
    contador += 1
    print(f'O Jogo {contador} é: {jogos[c]}', end='\n')
    sleep(1)
print('Boa sorte!')

