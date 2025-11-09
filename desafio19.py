# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
alunos = [ 'Jonathan', 'Kael', 'Rodolfo', 'Patrick']
sorteio = choice([ 'Jonathan', 'Kael', 'Rodolfo', 'Patrick'])

print(f'Dentre os alunos {alunos}, o aluno escolhido para apagar o quadro foi {sorteio}')