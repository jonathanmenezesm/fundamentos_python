# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

#criar tupla
extensos = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

#defini uma variável para ser meu index dentro da tupla
index = int(input("Qual número você deseja escrever por extenso (0 - 20): "))

#Uma variável pra receber a junção do input que será o index da tupla que contém os números escritos por extenso.
numeroPorExtenso = extensos[index]

print(numeroPorExtenso)