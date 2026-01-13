#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from desafio115.lib.arquivo import *
from desafio115.lib.interface import *
from time import sleep

from desafio115.lib.interface import leiaInt
from desafio115.lib.interface.bkp import cadastrarPessoa

arq = 'dados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

# cabecalho('SISTEMA DE DADOS')
while True:
    resposta = menu(['Listar pessoas cadastradas', 'Cadastrar pessoas', 'Sair'])
    if resposta == 1:
        #Listar as pessoas cadastradas no arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do programa... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
