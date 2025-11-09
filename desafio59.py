# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

print('''
    -------- MENU --------
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ----------------------
    ''')

escolha = int(input('Digite uma opção: '))

while escolha != 5:

    print('''
    -------- MENU --------
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ----------------------
    ''')

    if escolha == 1:
        somar = valor1 + valor2
        print(f'A soma é {somar}')

    elif escolha == 2:
        multiplicar = valor1 * valor2
        print(f'O produto da multiplicação é {multiplicar}')

    elif escolha == 3:
        escolha = 3
        if valor1 > valor2:
            maior = valor1
            print(f'O maior número é {maior}')

        else:
            maior = valor2
            print(f'O maior número é {maior}')

    elif escolha == 4:
        escolha = 4
        valor1 = int(input('Digite o primeiro valor novamente: '))
        valor2 = int(input('Digite o segundo valor novamente: '))
    escolha = int(input('Digite uma opção: '))
print('Fechando o programa...')