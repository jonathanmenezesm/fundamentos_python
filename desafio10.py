# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# considere US$1.00 = R$3,27

valor = float(input('Digite quantos reais você tem na carteira: '))
print('Você pode comprar US${:.2f}.'.format(valor/3.27))