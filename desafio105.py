# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.

def notas(*n, situacao=False):
    """
    Função notas()
    Recebe várias notas de alunos e retorna um dicionário com informações:
    - Quantidade de notas
    - Maior nota
    - Menor nota
    - Média da turma
    - Situação (opcional, baseada na média: >=7 Aprovado, <7 Reprovado)

    Retorna:
    dict: dicionário com os dados calculados
    """

    dados_lista = []
    dados_dicionario = {}
    quantidade = int(input('Quantos notas você quer adicionar: '))
    contador = 0

    while contador < quantidade:
        nota = float(input('Informe a nota do aluno: '))
        dados_lista.append(nota)
        contador += 1

    #definindo tamanha, maior e menor nota
    numero_notas = len(dados_lista)
    maior_nota = max(dados_lista)
    menor_nota = min(dados_lista)

    #adicionando ao dicionario
    dados_dicionario['numero_notas'] = numero_notas
    dados_dicionario['maior_nota'] = maior_nota
    dados_dicionario['menor_nota'] = menor_nota

    resultado = sum(dados_lista) / len(dados_lista)
    dados_dicionario['media'] = resultado

    #definindo status
    if dados_dicionario['media'] >= 7:
        dados_dicionario['situacao'] = 'Aprovado'
    else:
        dados_dicionario['situacao'] = 'Reprovado'

    return dados_dicionario

print(notas())



