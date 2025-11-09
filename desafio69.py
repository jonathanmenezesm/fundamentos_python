# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
from time import sleep

maioridade = 0
cont_masc = 0
cont_fem = 0
while True:
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).upper().strip()

    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        cont_masc += 1
    if sexo == 'F' and idade < 20:
        cont_fem +=1

    resposta = input('Estamos contabilizando... Deseja continuar? [S/N] ').upper().strip()
    if resposta not in ['S', 'N']:
        resposta = input('Você não digitou uma opção válida. Deseja continuar? [S/N] ').upper().strip()

    if resposta == 'S':
        continue
    else:
        break
print('Encerrando o programa...')
sleep(2)
print(f'''Foram cadastradas:
{maioridade} pessoas na maioridade.
{cont_masc} homens.
{cont_fem} mulheres com menos de 20 anos.''')