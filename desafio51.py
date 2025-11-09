# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# formula -> an = a1 + (n-1)r

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

pa = []
for n in range(1, 11):
    an = a1 + (n - 1) * r
    pa.append(an)

print(f'Sua PA é: {pa}')
