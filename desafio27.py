# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome da pessoa separadamente.
# Ex: Ana Maria Braga
# primeiro = Ana
# último = Braga

nome_completo = str(input('Digite o nome completo: '))
nome_completo = nome_completo.split()
print('Seu primeiro nome é: ', nome_completo[0])
print('Seu útimo nome é: ', nome_completo[-1])