# desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares, se forem impares, desconsidere-o.

for c in range(1, 7):
    inteiro = int(input('Digite um número inteiro: '))
    if inteiro % 2 == 0:
        inteiro = inteiro + c
print(f'A soma dos números pares é {inteiro}')
