# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário quer continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

carrinho = {}
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('valor: R$ '))

    # adiciona os inputs ao dicionário sem sobrescrever
    carrinho[nome] = valor

    continuar = ''
    while continuar not in ['SIM', 'NAO']:
        continuar = input('Deseja continuar? [SIM/NAO] ').strip().upper()
        if continuar not in ['SIM', 'NAO']:
            print('Opção inválida! Digite SIM ou NAO.')

    if continuar == 'NAO':
        break

# A) Total gasto na compra
total = sum(carrinho.values())
print(f'O total deu: {total:.2f}')

# B) Quantos produtos custam mais de R$1000
item_caro = 0
for n in carrinho.keys():
    if carrinho[n] > 1000:
        item_caro += 1
print(f'{item_caro} produto(s) custa(m) mais de R$ 1000.00')

# C) Nome do produto mais barato
barato = min(carrinho.keys(), key=carrinho.get)
print(f'O item mais barato é: {barato}')