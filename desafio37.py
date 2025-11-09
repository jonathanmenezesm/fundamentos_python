# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# — 1 para binário
# — 2 para octal
# — 3 para hexadecimal

numero = int(input('Escolha um número inteiro qualquer: '))
print('''Escolha qual será a base de conversão: 
1 - Binário
2 - Octal
3 - Hexadecimal''')
escolha = int(input('Escolha: '))

if escolha == 1:
    print(f'{numero} convertido para BINÁRIO é {bin(numero)[2:]}')
elif escolha == 2:
    print(f'{numero} convertido para OCTAL é {oct(numero)[2:]}')
elif escolha == 3:
    print(f'{numero} convertido para HEXADECIMAL é {hex(numero)[2:]}')
else:
    print('Opção inválida. Por favor, escolha 1, 2 ou 3.')

