# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = int(input('Digite um numero: '))
soma = numero
while True:
    novo_numero = int(input('Digite um novo número: '))
    if novo_numero == 999:
        soma = soma + 0
        print(f'A soma é {soma}')
        break
    else:
        soma += novo_numero