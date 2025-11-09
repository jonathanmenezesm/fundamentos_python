# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = float((peso / (altura ** 2)))

if IMC < 18.5:
    print('Você está abaixo do peso!')
elif IMC >= 18.5 and IMC < 25:
    print('Você está no peso ideal!')
elif IMC >= 25 and IMC < 30:
    print('Você está em sobrepeso!')
elif IMC >= 30 and IMC < 40:
    print('Você está em obesidade!')
else:
    print('Você está em obesidade mórbida!')