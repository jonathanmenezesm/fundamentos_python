# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
#
# Se quiser, posso te ajudar a formatar essa listagem com alinhamento elegante ou até incluir símbolos de moeda!
# #A saída deve ser igual o exemplo abaixo
# --------------------------------------
# 	LISTAGEM DE PREÇOS
# --------------------------------------
# Lápis.........................R$  1.75
# Borracha......................R$  2.00
# Caderno.......................R$ 15.90
# Estojo........................R$ 25.00
# Transferidor..................R$  4.20
# Compasso......................R$  9.99
# Mochila.......................R$120.32
# Canetas.......................R$ 22.30
# Livro.........................R$ 34.90
# --------------------------------------

estoque = ('trufa', 3.00, 'sanduiche', 5.00, 'suco', 6.00, 'salgado', 13.00)

print('-' * 40)
print(f'\tLISTAGEM DE PREÇOS')
print('-' * 40)

for i in range(0, len(estoque), 2):
    nome = estoque[i]
    preco = estoque[i + 1]
    print(f'{nome:.<30}R$ {preco:6.2f}')

print('-' * 40)