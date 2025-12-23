# Crie um programa que leia nome,
# ano de nascimento
# e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
carteira = {}

nome = str(input('Digite seu nome: '))
dt_nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - dt_nascimento
CPTS = int(input('Possui carteira de trabalho (1 para SIM / 0 para Não): '))

if CPTS == 1:
    carteira['nome'] = nome
    carteira['idade'] = idade
    carteira['primeiro_contrato'] = int(input('Digite o ano do seu primeiro contrato: '))
    carteira['salario'] = int(input('Digite o salario do seu primeiro contrato: '))

    #calculando tempo de contribuição
    contribuicao = date.today().year - carteira['primeiro_contrato']
    carteira['contribuicao'] = contribuicao

    #calculando tempo para aposentadoria
    tempo_para_aposentadoria = 35 - contribuicao
    carteira['tempo_para_aposentadoria'] = tempo_para_aposentadoria
    idade_aposentadoria = idade + tempo_para_aposentadoria
    carteira['idade_aposentadoria'] = idade_aposentadoria

else:
    print(f'{nome}, você não possui contribuição, portanto, não podemos calcular os anos para aposentadoria.')

print('-' * 30)
print(f'{"Carteira de trabalho":^30}')
print('-' * 30)
for k, v in carteira.items():
    print(f'{k} - tem o valor {v}')