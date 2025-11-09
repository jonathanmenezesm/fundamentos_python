# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint

print('Vamos jogar Jokenpô?')
print(''' Escolha sua opção: 
[ 1 ] para Pedra
[ 2 ] para Papel
[ 3 ] para Tesoura''')

escolha = int(input('Sua escolha: '))
maquina = randint(1, 3)
elementos = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

if escolha == maquina:
    print(f'Deu empate, você escolheu {elementos[escolha]} a máquina escolheu {elementos[maquina]}')
elif escolha != maquina:
    if escolha == 1 and maquina == 2 or escolha == 2 and maquina == 3 or escolha == 3 and maquina == 1:
        print(f'Você perdeu porque escolheu {elementos[escolha]} a máquina escolheu {elementos[maquina]}')
    elif escolha == 1 and maquina == 3 or escolha == 3 and maquina == 2 or escolha == 2 and maquina == 1:
        print(f'Você venceu porque escolheu {elementos[escolha]} a máquina escolheu {elementos[maquina]}')
else:
    print('Escolha uma opção válida!')