# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
from random import choice

alunos = choice([ 'joao', 'maria', 'caio', 'bruna'])

print('O aluno escolhido foi {}'.format(alunos))