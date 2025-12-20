# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um.
# Permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()
turma = list()

while True:
    dados = list()

    aluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a 1a nota: '))
    nota2 = float(input('Digite a 2a nota: '))
    turma.append([aluno, nota1, nota2])

    #Controle de parada
    if input('Deseja continuar? [S/N] ').upper() == 'N':
        break

#Boletim com médias
print('-' * 40)
print(f'{"Nº":<5}{"Aluno":<15}{"Média":>10}')
print('-' * 40)
for i, (aluno, nota1, nota2) in enumerate(turma, start=1):
    media = (nota1 + nota2) / 2
    print(f'{i:<5}{aluno:<15}{media:>10.2f}')
print('-' * 40)


# Consulta de notas individuais
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if opcao == 999:
        print("Encerrando consulta de notas...")
        break

    if 1 <= opcao <= len(turma):
        aluno, nota1, nota2 = turma[opcao - 1]
        print(f'Notas de {aluno} são [{nota1}, {nota2}]')
    else:
        print('Aluno não encontrado.')

    print('-' * 40)
