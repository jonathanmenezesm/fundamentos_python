# Escreva um programa que pergunte o salario de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a 1250. Calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salario: '))

if salario > 1250:
    salario_reajustado = salario + salario*(10/100)
    print('Seu salário reajustado é {:.2f}'.format(salario_reajustado))
if salario <= 1250:
    salario_reajustado = salario + salario*(15/100)
    print('Seu salário reajustado é {:.2f}'.format(salario_reajustado))

