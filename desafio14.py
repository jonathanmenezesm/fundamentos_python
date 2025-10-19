# Escreva um programa que converta uma temperatura digitada em celcius para converter em Firegnheit

celcius = float(input('Digite a temperatura em Celsius: '))
farenheit = (celcius * (9/5)) + 32

print('{}ºC equivalem a {}ºF'.format(celcius, farenheit))
