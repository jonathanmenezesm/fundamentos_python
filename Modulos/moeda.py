# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(numero, porcento):
    porcentagem = (porcento / 100) * numero
    aumento = numero + porcentagem
    print(f'O número {numero} + {porcento}% é {aumento}')
    return aumento

def diminuir(numero, porcento):
    porcentagem = (porcento / 100) * numero
    diminuido = numero - porcentagem
    print(f'O número {numero} - {porcento}% é {diminuido}')
    return diminuido

def dobro(numero):
    dobrado = numero * 2
    print(f'O dobro de {numero} = {dobrado}')
    return dobro

def metade(numero):
    metade = numero / 2
    print(f'Metade de {numero} = {metade}')
    return metade

