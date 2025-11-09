# faça um programa que leia um ano qualquer e mostre se ele é bissexto.
anob = int(input('Digite um ano qualquer: '))
if anob % 4 == 0:
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')