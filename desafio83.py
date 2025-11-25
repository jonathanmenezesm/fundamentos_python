# 💡 Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input('Digite uma expressão matemática com parentesis ex.: (a+b) x 2: ')
if '(' and ')' in expressao:
    print('Esta expressão é valida!')
else:
    print('Expressão invalida!')