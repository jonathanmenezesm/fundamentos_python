# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

numero = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(numero)} é {moeda.metade(numero, True)}')
print(f'O dobro de {moeda.moeda(numero)} é {moeda.dobro(numero, True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(numero, 10, True)}')
print(f'Reduzindo em 10%, temos {moeda.diminuir(numero, 10, True)}')