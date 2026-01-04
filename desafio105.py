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

    Parâmetros:
    *args (float): notas dos alunos
    situacao (bool): se True, adiciona a situação (Aprovado/Reprovado) baseada na média

    Retorna:
    dict: dicionário com os dados calculados
    """
    n = dict()

    if len(args) == 0:
        # caso não seja passada nenhuma nota
        n['total'] = 0
        n['maior'] = None
        n['menor'] = None
        n['media'] = None
        if situacao:
            n['status'] = 'Sem notas'
        return n

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


# Exemplos de uso:
print('-' * 100)
print(notas(10, 9, 9, 0, situacao=True))
print('-' * 100)
print(notas())  # sem parametros
print('-' * 100)
help(notas) #docstring