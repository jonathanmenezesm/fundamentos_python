# (assistir aula 42 da resolução)
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes


l1 = int(input('Digite o tamanho da primeira reta: '))
l2 = int(input('Digite o tamanho da segunda reta: '))
l3 = int(input('Digite o tamanho da terceira reta: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Você poderá formar um triângulo!')
    # escrevendo qual tipo de triângulo
    if l1 == l2 and l2 == l3:
        print('Seu triângulo é equilátero!')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Seu triângulo é isósceles!')
    elif l1 != l2 or l2 != l3 or l3 != l1:
        print('Seu triângulo é Escaleno!')
else:
    print('Você não conseguirá formar um triângulo!')


