# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.



def fatorial(n, show=False):
    resultado = 1
    for x in range(n, 0, -1):
        resultado *= x
        if show:
            print(x, end=' x ' if x > 1 else ' = ')
    print(f'{n}! = {resultado}')

fatorial(int(input("Deseja o fatorial de: ")),show=False)



