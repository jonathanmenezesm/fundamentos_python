#crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

idades = []
maior = []
menor = []

for i in range(1, 8):
    idade = int(input('Digite uma idade: '))
    idades.append(idade)
    for idade in idades:
        if idade >= 18:
            maior.append(idade)
        else:
            menor.append(idade)

print(f'{len(maior)} são maiores de idade e {len(menor)} ainda não atingiram maior de idade.')