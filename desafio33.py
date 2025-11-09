# faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

n1 = int(input('Escreva o primeiro numero: '))
n2 = int(input('Escreva o segundo numero: '))
n3 = int(input('Escreva o terceiro numero: '))

maior = n1
menor = n3

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O maior número é {}'.format(maior))

if n2 < menor:
    menor = n2
if n1 < menor:
    menor = n1
print('O menor número é {}'.format(menor))
