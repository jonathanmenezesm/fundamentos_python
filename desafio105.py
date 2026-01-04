# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.

def notas(*args, situacao=False):
    """
    Função notas(*args, situacao=False)
    Recebe várias notas e retorna um dicionário com:
    - total de notas
    - maior nota
    - menor nota
    - média da turma
    - situação (opcional, se situacao=True)
    """

    n = dict()
    n['total'] = len(args)
    n['maior'] = max(args)
    n['menor'] = min(args)
    n['media'] = sum(args) / len(args)
    if situacao:
        if n['media'] >= 7:
            n['status'] = 'APROVADO'
        else:
            n['status'] = 'REPROVADO'
    return n

resumo = notas(10, 9, 9, 0, situacao=True)
print(resumo)