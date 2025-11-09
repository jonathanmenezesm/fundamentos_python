# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# a media de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

maior_idade_homem = 0
mulheres_menores_20 = 0
soma_idade = 0
quantidade_idades = 0
nome_homem_mais_velho = ''

for c in range(1,5):
    nome = input(f'Digite o {c}º nome: ')
    idade = int(input(f'Digite a {c}ª idade: '))
    sexo = input('Digite o sexo (M/F): ').upper()

    # Media de idades recebe cada elemento c que seja adicionado em idade e divide pela quantidade c de elementos
    soma_idade += idade
    quantidade_idades += 1

    #Se for Homem e com idade MAIOR que a MAIOR IDADE de homem já resgistrada na variavel, iremos pegar o valor novo e substituir
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menores_20 += 1

print("\nResultado Final")
print("-" * 30)
print(f"Média de idade do grupo: {soma_idade / quantidade_idades:.1f} anos")

if nome_homem_mais_velho:
    print(f"Homem mais velho: {nome_homem_mais_velho} ({maior_idade_homem} anos)")
else:
    print("Não há homens no grupo.")

print(f"Mulheres com menos de 20 anos: {mulheres_menores_20}")
print("-" * 30)
