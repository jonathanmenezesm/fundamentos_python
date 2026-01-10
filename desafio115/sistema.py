#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#o sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from desafio115.lib.interface import *
from time import sleep

# cabecalho('SISTEMA DE DADOS')
while True:
    resposta = menu(['Listar pessoas cadastradas', 'Cadastrar pessoas', 'Sair'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do programa... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
