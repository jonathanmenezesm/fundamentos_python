# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = list()
pares = list()
impares = list()
while len(lista) < 7:
    lista.append(int(input('Digite um valor: ')))

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    elif i % 2 != 0:
        impares.append(i)

lista.sort()
pares.sort()
impares.sort()

print(f'A lista completa {lista}')
print(f'Os valores pares foram {pares}')
print(f'Os valores impares foram {impares}')

