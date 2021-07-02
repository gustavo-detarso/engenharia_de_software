# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule o valor do desconto e o preço final do produto.

# Nome do algoritmo
print('Algoritmo para cálculo de desconto')
# Passo 1: definição das strings
id_produto = str(input('Digite a id do produto: '))
preco = float(input('Digite o preço do produto: R$ '))
desconto = float(input('Digite o desconto a ser aplicado (0-100%): '))
valor_final = preco-(preco*(desconto/100))
# Passo 2: montando o algoritmo
print('O produto {} de R$ {}, após desconto de {}%, terá valor final de R$ {}' .format(id_produto,preco,desconto,valor_final))