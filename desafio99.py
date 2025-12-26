# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores
# e dizer qual deles é o maior.

numeros = []

def maior(numeros):
    while True:
        numeros.append(int(input('Digite um numero: ')))
        escolha = input('deseja continuar? [S/N] ').strip().upper()
        if escolha in 'N':
            break

maior(numeros)

print('-'*40)
print(f'Os valores digitados foram {numeros}')
print(f'O maior valor digitado foi {max(numeros)}')
print('-'*40)