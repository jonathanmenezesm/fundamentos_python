#faça um programa que leia um numero inteiro e diga se ele e ou nao um numero primo

numero_inteiro = int(input('Digite um número inteiro: '))
divisores = 0

for n in range(1, numero_inteiro + 1):
    if numero_inteiro % n == 0:
        divisores += 1

if divisores == 2:
    print('É um número primo!')
else:
    print('Não é um número primo')