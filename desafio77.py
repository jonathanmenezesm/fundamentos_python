# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('surf', 'skate', 'futebol', 'basquete', 'corrida', 'banana')
vogais = ('a', 'e', 'i', 'o', 'u')
for v in tupla:
    print(f'\n As vogais em {v} são -> ', end =' ')
    for letra in v:
        if letra in vogais:
            print(letra, end=' ')