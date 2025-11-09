# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes a aparece a letra "a"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: '))

print('Quantas vezes aparece a letra "a": ', frase.count('a'))

print('Primeira aparição na posição: ', frase.find('a'))

print('Ultima aparição na posição: ', frase.rfind('a'))