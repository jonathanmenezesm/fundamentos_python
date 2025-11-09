# Refaça o desafio 9, mostrando a tabuada de um número que o usuario escolher, só que agora utilizando um laço for

n = int(input('Digite um numero: '))
for c in range(1, 11):
    p = c*n
    print(f'{n} x {c} = {p}')


