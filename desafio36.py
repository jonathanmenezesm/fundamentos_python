# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos_financiamento = int(input('Digite em quantos anos será o financiamento: '))

parcela = valor_casa / (anos_financiamento * 12)

if parcela >= salario * (30/100):
    print('Seu financiamento foi negado, devido ao alto valor da parcela.')
else:
    print(f'''Seu financiamento foi aprovado!
    {anos_financiamento*12} parcelas de R${parcela:.2f}''')