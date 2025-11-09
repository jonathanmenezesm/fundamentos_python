#melhore o jogo desafio 28 onde o computador vai pensar em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randrange
numero = randrange(0, 5)
escolha = int(input('Tente adivinhar um número entre 0 e 5: '))
contador = 1

while escolha != numero:
    contador +=  1
    escolha = int(input('Tente novamente: '))
print(f'Parabéns, você acertou o número era {numero}.')
print(f'Você precisou de {contador} tentativa(s) para acertar!')