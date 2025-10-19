# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelas quais ele foi alugado. Calcule o preço a pagarm sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

km_percorrido = int(input('Quantos KM foram percorridos: '))
dias_alugado = int(input('Quantos dias alugados? '))

km_preco = km_percorrido * 0.15
diaria_preco = dias_alugado * 60
total = km_preco + diaria_preco

print('Você percorreu {} KM \nUtilizou o carro por {} dias. \n--------------------------- \nValor das diárias: R${:.2f} \nValor dos KMs percorridos: R${:.2f} \nTotalizando: R${:.2f}'.format(km_percorrido, dias_alugado, diaria_preco, km_preco, total))

