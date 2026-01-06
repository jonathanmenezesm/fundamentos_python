# desafio107
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

#desafio 108
# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

def aumentar(numero = 0, porcento = 0):
    porcentagem = (porcento / 100) * numero
    aumento = numero + porcentagem
    return aumento

def diminuir(numero = 0, porcento = 0):
    porcentagem = (porcento / 100) * numero
    diminuido = numero - porcentagem
    return diminuido

def dobro(numero = 0):
    dobrado = numero * 2
    return dobrado

def metade(numero = 0):
    dividido = numero / 2
    return dividido

def moeda(numero = 0, moeda = 'R$'):
    return f'{moeda}{numero}'.replace('.', ',')
