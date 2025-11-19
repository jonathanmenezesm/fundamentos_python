# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('''-----------------------------------------
    Seja bem vindo ao Jony's Bank
-----------------------------------------''')

saque = int(input('Digite o valor que você deseja sacar: '))
cedulas = [50, 20, 10, 1]
i = 0

while saque > 0 and i < len(cedulas):
    valor = cedulas[i]
    quantidade = saque // valor
    if quantidade > 0:
        print(f'{quantidade} cédula(s) de R${valor}')
        saque -= quantidade * valor
    i += 1