# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()
while sexo != '' and sexo != 'M' and sexo != 'F':
    sexo = input('Digite um valor válido: ').upper().strip()
print(f'Sexo {sexo} registrado com sucesso')