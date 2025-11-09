# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

# Escolhas entre impar
humano_escolha = str(input('Escolha entre IMPAR ou PAR: ')).upper().strip()
#Validando entrada da escolha
while humano_escolha not in ['IMPAR', 'PAR']:
    print('Digite uma opção válida!')
    humano_escolha = str(input('Escolha entre IMPAR ou PAR: ')).upper().strip()
#alternando escolhas
if humano_escolha == 'IMPAR':
    maquina_escolha = 'PAR'
elif humano_escolha == 'PAR':
    maquina_escolha = 'IMPAR'


contador_vitorias = 0
soma = 0
while True:
    humano_numero = int(input('Escolha um número: '))
    maquina_numero = randint(1, 2)
    soma = humano_numero + maquina_numero

    if humano_escolha == 'PAR' and soma % 2 == 0 or humano_escolha == 'IMPAR' and soma % 2 != 0:
        contador_vitorias += 1
        print(f'{contador_vitorias} vitória(s). Você escolheu {humano_numero} e a máquina {maquina_numero}')
    else:
        break
print(f'Você perdeu, pois, a máquina escolheu {maquina_numero} e você {humano_numero}. Você teve {contador_vitorias} vitorias seguidas!')