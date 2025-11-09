# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year

if ano_atual - ano_nascimento < 18:
    falta = abs((ano_atual - ano_nascimento) - 18)
    print(f'Você ainda não está na idade para se alistar, faltam {falta} ano(s)')
elif ano_atual - ano_nascimento == 18:
    print('Você está no ano certo para alistamento, compareça a uma junta militar!')
else:
    print('Você passou do tempo de se alistar!')
