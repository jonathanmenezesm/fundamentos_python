# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numero = int(input('Digite um valor inteiro: '))
soma = 0
escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
valores = []

while escolha != 'N':
    soma += numero
    valores.append(numero)
    numero = int(input('Digite outro valor inteiro: '))
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()

if escolha == 'N':
    soma += numero
    valores.append(numero)
    media = soma / len(valores)
    print(f'A média dos números digitados é: {media}')
    print(f'O maior número é: {max(valores)}')
    print(f'O menor valor é : {min(valores)}')