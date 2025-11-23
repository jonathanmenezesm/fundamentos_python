# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for n in range (0,5):
    a = input('Digite um número: ')
    lista.append(a)
print(f'A Lista é: {lista} com {len(lista)} elementos')
print(f'O maior valor é: {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor é: {min(lista)} na posição {lista.index(min(lista))}')