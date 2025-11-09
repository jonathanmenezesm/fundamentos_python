# Desafio 53
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
# Exemplos de palíndromos: (le de tras pra frente e é a mesma coisa, sem considerar os espaços)
# - APOS A SOPA
# - A SACADA DA CASA
# - A TORRE DA DERROTA
# - O LOBO AMA O BOLO
# - ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: '))
frase_sem_espaco = frase.replace(' ', '').lower()

if frase_sem_espaco == frase_sem_espaco[::-1]:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')
