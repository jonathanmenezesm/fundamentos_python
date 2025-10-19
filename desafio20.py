# Um professor, quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

aluno1 = input('Digite o nome do primeito aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

alunos = sample([aluno1, aluno2, aluno3, aluno4], k=4)

print('A ordem para apresentação do trabalho será: 1º {}, 2º {}, 3º {}, 4º {}.'.format(*alunos))