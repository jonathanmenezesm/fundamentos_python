# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
import moeda

numero = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(numero)} é {moeda.moeda(moeda.metade(numero))}')
print(f'O dobro de {moeda.moeda(numero)} é {moeda.moeda(moeda.dobro(numero))}')
print(f'Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(numero, 10))}')
print(f'Reduzindo em 10%, temos {moeda.moeda(moeda.diminuir(numero, 10))}')