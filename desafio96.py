# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.

def area(l, c):
    a = largura * comprimento
    print(f'A área de {largura}x{comprimento} possui {a}m².')


largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area(largura, comprimento)