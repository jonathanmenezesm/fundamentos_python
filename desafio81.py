# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    escolha = input('Deseja continuar [S/N]? ').upper().strip()
    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
print(f'Foram digitados {len(lista)} números')
print(f'A lista em ordem decrescente {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi digitado.')