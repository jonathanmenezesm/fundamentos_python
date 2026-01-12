# DESAFIO 113
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except ValueError:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return inteiro


def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada interrompida pelo usuário.\033[m')
            return 0
        else:
            return inteiro


def leiaFloat(msg):
    while True:
        entrada = input(msg)
        if "." not in entrada:  # regra extra: precisa ter ponto decimal
            print('\033[0;31mERRO! Digite um número real com ponto decimal.\033[m')
            continue
        try:
            real = float(entrada)
        except ValueError:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada interrompida pelo usuário.\033[m')
            return 0.0
        else:
            return real


# Programa principal
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número inteiro: {n}')

f = leiaFloat('Digite um número real (com ponto decimal): ')
print(f'Você digitou o número real: {f}')