# Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada uma em um dicionário.
# Os dicionários devem ser armazenados em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média


pessoas = list()
while True:
    dados = {}
    nome = input('Digite o nome: ')
    dados['nome'] = nome
    sexo = input('Digite o sexo (M/F): ').upper().strip()
    dados['sexo'] = sexo
    idade = int(input('Digite a idade: '))
    dados['idade'] = idade
    pessoas.append(dados.copy())
    dados.clear()

    if input('Deseja continuar(S/N): ').upper().strip() == 'S':
        continue
    else:
        break

#Quantas pessoas foram cadastradas
print(f'Foram cadastradas {len(pessoas)} pessoas.')

#media de idade das pessoas
soma_idade = 0
for i in pessoas:
     soma_idade += i['idade']

media_idades = soma_idade / len(pessoas)
print(f'A média de idade delas é: {media_idades} anos')

#lista com mulheres
mulheres = list()
for mulher in pessoas:
    if mulher['sexo'] == 'F':
        mulheres.append(mulher['nome'])
print(f'Todas as mulheres cadastradas: {mulheres}')

#lista com todas as pessoas acima da idade
maior_idade = list()
for maiores in pessoas:
    if maiores['idade'] >= 18:
        maior_idade.append(maiores['nome'])
print(f'Todas as pessoas maior de idade cadastradas: {maior_idade}')

