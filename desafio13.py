# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

salario = float(input('Digite o seu salário: '))
aumento = salario * 0.15
salario_reajustado = salario + aumento

print('Seu salário reajustado com aumento fica em: R${:.2f}.'.format(salario_reajustado))
print('Isso significa um aumento de {} reais.'.format(aumento))