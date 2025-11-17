# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Leitura dos valores
tupla = (
    int(input('Digite o 1º valor: ')),
    int(input('Digite o 2º valor: ')),
    int(input('Digite o 3º valor: ')),
    int(input('Digite o 4º valor: '))
)

# A) Quantas vezes apareceu o valor 9
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')

# B) Em que posição foi digitado o primeiro valor 3
if 3 in tupla:
    print(f'O número 3 apareceu primeiro na posição {tupla.index(3) + 1}.')
else:
    print('O número 3 não foi digitado.')

# C) Quais foram os números pares
print('Os números pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')