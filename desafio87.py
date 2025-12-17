# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

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

#somando os valores pares digitados
soma_pares = 0
for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0:
            soma_pares += elemento
print(f'A soma dos elementos pares é {soma_pares}')

#somando os valores da 3ª coluna digitados
soma_3acoluna = 0
for linha in matriz:
    soma_3acoluna += linha[2]
print(f'A soma dos elementos da 3ª coluna é {soma_3acoluna}')

#pegando o maior valor da segunda linha
maior_valor2linha = max(matriz[1])
print(f'O maior valor da segunda linha é {maior_valor2linha}')