# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex:
# 5! = 5x4x3x2x1 = 120

from math import factorial
resultado = int(input("Digite um valor inteiro: "))
#contador auxiliar para adicionar os números do fatorial em lista
lista = []
contador = 0
while contador != resultado:
    contador += 1
    lista.append(contador)
lista.reverse()

#conversão em string para interpolar 'x' entre os números da lista
lista_string = []
for n in lista:
    lista_string.append(str(n))
lista_interpolada = "x".join(lista_string)
print(f' {resultado}! = {lista_interpolada} = {factorial(resultado)}')
