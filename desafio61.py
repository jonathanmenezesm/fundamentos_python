# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

pa = []
pa.append(a1)
a10 = a1 + (10 - 1) * r
an = a1

while an < a10:
    # Atualiza o próximo termo da PA
    an = an + r
    # Adiciona esse novo termo à lista
    pa.append(an)
print(f'Os dez primeiros termos da PA são: {pa}')
