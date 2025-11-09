# escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual o numero escolhido pelo computador.
# o programa devera escrever na tela se o usuário venceu ou perdeu.

import random
numero = random.randrange(0, 5, 1)
escolha = int(input('Tente adivinhar o número entre 0 e 5: '))

if escolha == numero:
    print('Parabéns o número era {}'.format(numero))
else:
    print('Você perdeu!')
