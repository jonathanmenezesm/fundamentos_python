# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo
# e realize a contagem.
#
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada.
# Na 'c' a contagem deve identificar se o inicio é maior que o fim e decrementar, se o fim é maior que o inicio, incrementar e considerar também números positivos e negativos diferentes de 0

from time import sleep

def contador(i, f, p):

    #contagem personalizada
    if not p or p == 0:
        if i < f:
            p = 1
        else:
            p = -1
    print(f"Contagem de {i} até {f} de {p} em {p}:")
    sleep(1)

    if p > 0:
        while i <= f:
            print(i, end=' ')
            i += p
            sleep(0.5)
    else:
        while i >= f:
            print(i, end=' ')
            i += p
            sleep(0.5)
    print("Fim!\n")

    # if i <= f:
        #     p = 1
        #     while i <= f:
        #         print(i, end=' ')
        #         i += p
        #         sleep(0.5)
        #     print('Fim!')
        #
        # if p > 0:
        #     while i >= f:
        #         print(i, end=' ')
        #         i += p
        #         sleep(0.5)
        #     print('Fim!')

# a) De 1 até 10, de 1 em 1
# contador(1, 10, 1)

# b) De 10 até 0, de 2 em 2
# contador(10, 0, -2)

inicio = int(input('Defina o número de início: '))
fim = int(input('Defina o número do final: '))
entrada_passo = input('Defina o número do passo: ')

if entrada_passo.strip() != "":
    passo = int(entrada_passo)
else:
    passo = None

contador(inicio, fim, passo)