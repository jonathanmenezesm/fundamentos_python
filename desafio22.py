#Crie um programa que leia o nome completo de uma pessoa OK
#Mostre o nome com todas as letras maiusculas e minusculas OK
#Quantas letras ao todo(sem considerar espaços) (22 total)
# quantas letras tem no primeiro nome (8 primeiro nome)

#Ler o nome completo
nome_completo = str(input("Digite o seu nome completo: "))

# Transforma em maiusculo e minusculo
p_nome = nome_completo.split() #separa os nomes na string
print('Em maiusculo: ',nome_completo.upper()) #coloca em caixa alta
print('Em minusculo: ',nome_completo.lower()) #caixa baixa

nome_separado = nome_completo.split() #separa os nomes para extrair o primeiro nome
nome_completo_sem_espaco = ''.join(nome_separado) #join sem espaço '' para contar todas as letras do nome

print('Ao todo são {} letras'.format(len(nome_completo_sem_espaco)))
print('Seu primeiro nome possui {} letras'.format(len(p_nome[0])))

