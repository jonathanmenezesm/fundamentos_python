# faça um programa que leia a largura e a altura de uma parede em metros e calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
rendimento = area / 2

print('Para uma área de {} metros, você irá precisar de {} litros de tinta.'.format(area, rendimento))
