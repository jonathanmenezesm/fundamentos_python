# Crie um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# - Quantas pessoas foram cadastradas.
# - Uma listagem com as pessoas mais pesadas.
# - Uma listagem com as pessoas mais leves.

pessoas = list()
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])
    escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha in 'N':
        break

print(f'\n{len(pessoas)} pessoa(s) foram cadastradas.')

# Criar lista de pesos
pesos = []
for p in pessoas:
    pesos.append(p[1])

# Descobrir maior e menor
maior = max(pesos)
menor = min(pesos)

# Mostrar quem tem o maior peso
print(f'O maior peso foi {maior}Kg. Pessoa(s): ', end=' ')
for nome, peso in pessoas:
    if peso == maior:
        print(f'{nome} ')

# Mostrar quem tem o menor peso
print(f'O menor peso foi {menor}Kg. Pessoa(s): ', end=' ')
for nome, peso in pessoas:
    if peso == menor:
        print(f'{nome} ')