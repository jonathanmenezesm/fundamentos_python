# crie um programa que leia um numero real qualquer e mostre na tela a sua porção inteira
# ex: digite um numero: 6.127 R-> " O numero 6.127 tem a parte inteira 6

import math

numero = float(input('Digite um número real: '))
print('A parte inteira do seu número é {}.'.format(math.trunc(numero)))
# Truncate - retorna somente a parte inteira de um número float