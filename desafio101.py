# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
from datetime import date
def voto(ano_nascimento):
    # ano_nascimento = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano_nascimento
    if idade >= 18:
        print('O seu voto é OBRIGATÓRIO!')
    elif idade >= 16 and idade < 18:
        print('Seu voto é OPCIONAL!')
    else:
        print('Seu voto é NEGADO, devido não ter idade mínima (16 anos).')

voto(int(input('Digite o ano de nascimento: ')))