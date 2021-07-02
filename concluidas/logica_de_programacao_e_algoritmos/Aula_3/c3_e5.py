# Escreva um algoritmo em Python em que o usuário escolhe se ele quer comprar maçãs, laranjas ou bananas. Deverá ser apresentado na tela com a opção 1 para maçã, 2 para laranja e 3 para banana.
# Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela.
# Considere que uma maçã custa R$ 2.30, uma laranja R$ 3.60 e uma banana R$ 1.85.

# Passo 1: denição de strings

print('Escolha a fruta que deseja comprar')
print('Maçã')
print('Laranja')
print('Banana')
escolha = str(input('Qual fruta deseja comprar? '))
if escolha == 'Maçã' or escolha == 'Laranja' or escolha == 'Banana':
    quantidade = int(input('Quantas unidades? '))
if escolha == 'Maçã':
    total = quantidade*2.3
    print('Você comprou {} {}(s) e o total a se pagar é de: R$ {:.2f}' .format(quantidade,escolha,total))
elif escolha == 'Laranja':
    total = quantidade*3.6
    print('Você comprou {} {}(s) e o total a se pagar é de: R$ {:.2f}' .format(quantidade,escolha,total))
elif escolha == 'Banana':
    total = quantidade*1.85
    print('Você comprou {} {}(s) e o total a se pagar é de: R$ {:.2f}' .format(quantidade,escolha,total))
else:
    print('Produto inexistente ou não digitado exatamente igual conforme apresentado.')