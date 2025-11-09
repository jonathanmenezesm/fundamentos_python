# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

valor_produto = float(input('Digite o valor do produto: '))

print('''
Escolha a forma de pagamento: 
1 - à vista dinheiro/cheque: 10% de desconto
2 - à vista no cartão: 5% de desconto
3 - em até 2x no cartão: preço normal
4 - 3x ou mais no cartão: 20% de juros''')

modo_pagamento = int(input('Digite o modo de pagamento: '))

if modo_pagamento == 1:
    valor_final = valor_produto - (valor_produto * (10 / 100))
    print(f'Valor do produto fica em: R$ {p1:.2f}')
elif modo_pagamento == 2:
    valor_final = valor_produto - (valor_produto * (5 / 100))
    print(f'Valor do produto fica em: R$ {p2:.2f}')
elif modo_pagamento == 3:
    valor_final = valor_produto / 2
    print(f'O valor fica em 2 parcelas de R$ {p3:.2f}')
elif modo_pagamento == 4:
    numero_parcelas = int(input('Digite o número de parcelas que você deseja pagar: '))
    valor_final = valor_produto + (valor_produto * (20 / 100))
    print(f'O valor fica em {numero_parcelas} ou mais parcelas de R$ {valor_final/numero_parcelas:.2f}')
else:
    print('Digite um modo de pagamento válido!')


