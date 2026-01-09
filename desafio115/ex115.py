#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#o sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.


def menu():
    print('-' * 60)
    print('MENU PRINCIPAL'.center(60))
    print('-' * 60)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar novas pessoas')
    print('3 - Sair do sistema')
    print('-' * 60)
    opcao = input('Sua opção: ')


def lerDados():
    with open("dados.txt", "r", encoding="utf-8") as f:
        for linha in f:
            print(linha)
lerDados()

def cadastrarPessoa():
    with open("dados.txt", "a", encoding="utf-8") as f:
        nome = input('Digite o nome: ')
        idade = input('Digite sua idade: ')
        f.write(f"{nome}, {idade}\n")

cadastrarPessoa()


