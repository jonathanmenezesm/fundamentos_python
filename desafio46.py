# Desafio46 – Crie um programa que exiba na tela uma contagem regressiva de 10 até 0, com uma pausa de 1 segundo entre cada número.
# Ao final da contagem, exiba uma mensagem simulando o estouro de fogos de artifício.

from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('🎉 FOGOS DE ARTIFICIO 🎉')
