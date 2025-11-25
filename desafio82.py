# 💡 Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    escolha = input('Deseja continuar[S/N]? ').strip().upper()

    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 != 0:
        impares.append(valor)

    if escolha in 'N':
        break
    elif escolha in 'S':
        continue

print(f'''
Lista completa: {lista}
Pares: {pares}
Impares: {impares}
''')