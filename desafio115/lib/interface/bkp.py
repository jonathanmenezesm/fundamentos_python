from time import sleep

def menu():
    print('-' * 60)
    print('MENU PRINCIPAL'.center(60))
    print('-' * 60)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar novas pessoas')
    print('3 - Sair do sistema')
    print('-' * 60)


def lerDados():
    with open("dados.txt", "r", encoding="utf-8") as f:
        for linha in f:
            print(linha, end="")


def cadastrarPessoa():
    with open("dados.txt", "a", encoding="utf-8") as f:
        nome = input('Digite o nome: ')
        idade = input('Digite sua idade: ')
        f.write(f"{nome} \t\t {idade} \n")


#programa principal:
def sistema():
    while True:
        menu()
        opcao = int(input('Sua opção: ').strip())
        if opcao == 1:
            lerDados()
            sleep(2)
        elif opcao == 2:
            cadastrarPessoa()
        elif opcao == 3:
            print('-' * 60)
            print('Sistema fechando...'.center(60))
            sleep(2)
            print('VOLTE SEMPRE!'.center(60))
            print('-' * 60)
            exit()