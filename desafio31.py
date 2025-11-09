# Desenvolva um programa que pergunte a distancia de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200KM e R$0,45 para viagens mais longas.

distanciaViagem = int(input('Qual é a distancia da sua viagem: '))

if distanciaViagem <= 200:
    valorViagem = distanciaViagem * 0.50
else:
    valorViagem = distanciaViagem * 0.45

print('O valor da viagem é: R${:.2f}'.format(valorViagem))