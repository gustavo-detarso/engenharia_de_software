# Faça um algoritmo que leia o valor total de uma compra e calcule o valor do pagamento final de acordo com a opção escolhida.
# Se a escolha do pagamento for parcelado, clacule também o valor de cada parcela. Al final apresente o valor total da compra e o valor das parcelas.
# Pagamento a vista conceder 5% de desconto
# Pagamento em 3x o valor não sofre alterações
# Pagamento em 5x acréscimo de 2%
# Pagamento em 10x acréscimo de 8%

print('CÁLCULO DE OPÇÕES DE COMPRA:')
valor = float(input('Qual o valor da compra? '))
print('Selecione dentre as seguintes opções:')
print('1 - Pagamento a vista - 5% de desconto')
print('2 - Pagamento em 3x - sem alterações')
print('3 - Pagamento em 5x - 2% de acréscimo')
print('4 - Pagamento em 10x - 8% de acréscimo')
escolha = int(input('Qual opção de pagamento desejada? '))
if escolha == 1: # Pagamento a vista conceder 5% de desconto
    valor_final = valor*0.95
    print('O valor da compra foi de {:.2f} e a opção de pagamento foi a vista, sendo aplicado desconto de 5% no valor total da compra. Valor final de {:.2f}' .format(valor,valor_final))
elif escolha == 2: # Pagamento em 3x o valor não sofre alterações
    valor_final = valor
    print('O valor da compra foi de {:.2f} e a opção de pagamento foi parcelado em 3x. Valor final de {:.2f}' .format(valor,valor))
elif escolha == 3: # Pagamento em 5x acréscimo de 2%
    valor_final = valor*1.02
    print('O valor da compra foi de {:.2f} e a opção de pagamento foi parcelado em 5x. Valor final de {:.2f}' .format(valor,valor_final))
elif escolha == 4: # Pagamento em 10x acréscimo de 8%
    valor_final = valor*1.08
    print('O valor da compra foi de {:.2f} e a opção de pagamento foi parcelado em 10x. Valor final de {:.2f}' .format(valor,valor_final))
else:
    print('Operação inválida!')