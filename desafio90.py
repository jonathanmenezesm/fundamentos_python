#Faça um programa que leia nome e media de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.

# 1 - iniciando dicionario
aluno = dict()
# 2 - lendo os dados
nome = str(input('Qual o seu nome: '))
media = float(input('Qual a sua média: '))

# 3 adicionando no dicionario
aluno['nome'] = nome
aluno['media'] = media

# 4 exibindo dict
print(aluno)