# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint
numeros = list()

def sorteia():
    while len(numeros) < 5:
        numeros.append(randint(1, 20))

def somarPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    return soma

sorteia()
print(f'Os numeros sorteados foram {numeros}')
print(f'A soma de todos os pares é {somarPar()}')
