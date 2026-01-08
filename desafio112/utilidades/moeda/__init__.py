def aumentar(numero=0, porcento=0, formato=False):
    """
    Calcula o aumento de um valor em determinada porcentagem.

    Args:
        numero (float): Valor base a ser aumentado.
        porcento (float): Percentual de aumento.
        formato (bool, opcional): Se True, retorna o valor formatado como moeda.
                                  Se False, retorna um número float.

    Returns:
        float | str: Valor aumentado, como número ou string formatada.
    """
    porcentagem = (porcento / 100) * numero
    aumento = numero + porcentagem
    return aumento if formato == False else moeda(aumento)


def diminuir(numero=0, porcento=0, formato=False):
    """
    Calcula a redução de um valor em determinada porcentagem.

    Args:
        numero (float): Valor base a ser reduzido.
        porcento (float): Percentual de redução.
        formato (bool, opcional): Se True, retorna o valor formatado como moeda.
                                  Se False, retorna um número float.

    Returns:
        float | str: Valor reduzido, como número ou string formatada.
    """
    porcentagem = (porcento / 100) * numero
    diminuido = numero - porcentagem
    return diminuido if formato == False else moeda(diminuido)


def dobro(numero=0, formato=False):
    """
    Calcula o dobro de um valor.

    Args:
        numero (float): Valor base.
        formato (bool, opcional): Se True, retorna o valor formatado como moeda.
                                  Se False, retorna um número float.

    Returns:
        float | str: Dobro do valor, como número ou string formatada.
    """
    dobrado = numero * 2
    return dobrado if not formato else moeda(dobrado)


def metade(numero=0, formato=False):
    """
    Calcula a metade de um valor.

    Args:
        numero (float): Valor base.
        formato (bool, opcional): Se True, retorna o valor formatado como moeda.
                                  Se False, retorna um número float.

    Returns:
        float | str: Metade do valor, como número ou string formatada.
    """
    dividido = numero / 2
    return dividido if not formato else moeda(dividido)


def moeda(numero=0, moeda='R$'):
    """
    Formata um número como valor monetário.

    Args:
        numero (float): Valor numérico a ser formatado.
        moeda (str, opcional): Símbolo da moeda (padrão 'R$').

    Returns:
        str: Valor formatado como moeda, com duas casas decimais e vírgula como separador.
    """
    return f'{moeda}{numero:.2f}'.replace('.', ',')

def resumo(numero=0, aumento=10, reducao=10):
    print(f'{"-" * 30}')
    print('RESUMO DO VALOR'.center(30))
    print(f'{"-" * 30}')
    print(f'Preço analisado: \t{moeda(numero)}')
    print(f'Dobro do preço: \t{dobro(numero, True)}')
    print(f'Metade do preço: \t{metade(numero, True)}')
    print(f'Aumento de {aumento}%: \t{aumentar(numero, aumento, True)}')
    print(f'Redução de {reducao}%: \t{diminuir(numero, reducao, True)}')




