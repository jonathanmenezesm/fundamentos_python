# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        valor = input('o valor já foi adicionado, tente novamente: ')
        print(f'O valor {valor} foi adicionado')
        lista.append(valor)
    elif valor not in lista:
        lista.append(valor)
        print(f'O valor {valor} foi adicionado')
        escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()
        if escolha == 'N':
            break
        elif escolha == 'S':
            continue
print(f'Programa Finalizado com {len(lista)} elementos')
print(f'A Lista é {sorted(lista)} em ordem crescente.')