# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Digite um valor para o cateto oposto: '))
ca = float(input('Digite um valor para o cateto adjacente: '))

hi = math.sqrt(ca**2 + co**2)
print('A hipotenusa vai medir {}'.format(int(hi)))
