# escreva um programa que leia a velocidade de um carro
# se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite.
# Ex.:
# Passou a 90km/h, foi multado em 70 reais (7x10 km excedente)

velocidadeAtual = float(input('Qual a velocidade atual do carro? '))

if velocidadeAtual > 80:
    multa = (velocidadeAtual - 80) * 7
    print('Você passou a {}km/h e foi multado em R${}'.format(velocidadeAtual, (multa)))
