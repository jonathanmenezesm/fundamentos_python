# Desafio 48
# Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
for n in range(1, 501):
    if n % 2 != 0 and n % 3 == 0:
        soma = soma + n
print(soma)