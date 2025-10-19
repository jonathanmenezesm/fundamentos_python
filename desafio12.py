# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Qual é o preço do produto: R$ '))
desconto = preco * 0.05
produtofinal = preco - desconto

print('O produto com desconto sai à R${:.2f}.'.format(produtofinal))