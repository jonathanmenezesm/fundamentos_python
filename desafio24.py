# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nome_cidade = str(input('Digite o nome de uma cidade: '))
print('{} começa com o nome "Santo?"'.format(nome_cidade))
print('Santo' in nome_cidade)