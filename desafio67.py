# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

numero = 1
while numero > 0:
    numero = int(input('Digite um número: '))
    if numero < 0:
        print('Programa encerrado!')
        break
    else:
        for n in range(1, 11):
            print(f'{numero} x {n} = {n * numero}')
        print('----' * 5)