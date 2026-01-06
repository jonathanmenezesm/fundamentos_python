# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from desafio107.moeda import aumentar, diminuir, dobro, metade

numero = float(input('Digite um preço: R$'))
print(f'A metade de {numero} é {metade(numero)}')
print(f'O dobro de {numero} é {dobro(numero)}')
print(f'Aumentando em 10%, temos {aumentar(numero, 10)}')
print(f'Reduzindo em 10%, temos {diminuir(numero, 10)}')
