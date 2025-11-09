# Escreva um programa que leia um número n inteiro qualquer
# e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex:
# 0 → 1 → 1 → 2 → 3 → 5 → 8

n = int(input('Digite um número inteiro qualquer: '))

t1 = 0
t2 = 1
t3 = 0
fibonacci = []
while t3 < n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    t3 = t3
    fibonacci.append(t3)
print(fibonacci)