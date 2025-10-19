# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

angulo = float(input('Digite um angulo: '))
rad = math.radians(angulo)

print('O seno do angulo é: {:.2f}'.format(math.sin(rad)))
print('O cosseno do angulo é: {:.2f}'.format((math.cos(rad))))
print('A tangente do angulo é: {:.2f} '.format(math.tan(rad)))
