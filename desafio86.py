# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
# EXEMPLO:
# # Digite um valor para [0, 0]: 1
# # Digite um valor para [0, 1]: 2
# # Digite um valor para [0, 2]: 3
# # Digite um valor para [1, 0]: 4
# # Digite um valor para [1, 1]: 5
# # Digite um valor para [1, 2]: 6
# # Digite um valor para [2, 0]: 7
# # Digite um valor para [2, 1]: 8
# # Digite um valor para [2, 2]: 9
#
# # [ 1 ][ 2 ][ 3 ]
# # [ 4 ][ 5 ][ 6 ]
# # [ 7 ][ 8 ][ 9 ]

# Criação da matriz 3x3 inicializada com zeros
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenchendo a matriz com valores lidos pelo teclado
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))

# Exibindo a matriz formatada
print("\nMatriz:")
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[ {matriz[l][c]:^5} ]", end="")
    print()  # quebra de linha ao final de cada linha da matriz
