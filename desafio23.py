# faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separado
# Ex:
# Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1


numero = int(input('Digite um número entre 0 e 9999: '))

m = (numero // 1000) % 10
c = (numero // 100) % 10
d = (numero // 10) % 10
u = numero % 10
print(""" 
Milhar: {}
Centena: {}
Dezena: {}
Unidade: {}
""".format(m, c, d, u))


