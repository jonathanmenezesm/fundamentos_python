# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
while len(lista) < 5:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        # se a lista estiver vazia, adiciona direto
        if len(lista) == 0:
            lista.append(valor)
            print(f'O valor {valor} foi adicionado no início da lista.')
        else:
            for indice, n in enumerate(lista):
                if valor <= n:
                    lista.insert(indice, valor)
                    print(f'O valor {valor} foi adicionado na posição {indice}.')
                    break
            else:
                lista.append(valor)
                print(f'O valor {valor} foi adicionado no final da lista.')
    else:
        print(f'O valor {valor} já foi adicionado, tente outro.')

print(f'Lista final ordenada: {lista}')