# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

l1 = int(input('Digite o tamanho da primeira reta: '))
l2 = int(input('Digite o tamanho da segunda reta: '))
l3 = int(input('Digite o tamanho da terceira reta: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Você poderá formar um triângulo!')
else:
    print('Você não conseguirá formar um triângulo!')

