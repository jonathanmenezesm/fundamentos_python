# Melhore o DESAFIO61 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

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

escolha = str(input('Deseja mostrar mais termos? (SIM/NAO) ').upper())
if escolha == 'SIM':
    quantidade_termos = int(input('Deseja mostrar quantos termos: '))
    for _ in range(quantidade_termos):
        an = an + r
        pa.append(an)
print(pa)