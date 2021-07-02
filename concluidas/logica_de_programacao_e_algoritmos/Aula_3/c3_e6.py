# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba o resultado da operação na tela.

print('CALCULADORA SIMPLES ENTRE DOIS NÚMEROS')
print('Operações disponíveis:')
print('Adição (+)')
print('subtração (-)')
print('Multiplicação (*)')
print('Divisão (/)')
print('Pressione qualquer tecla para sair!')
num1 = float(input('Digite O PRIMEIRO número: '))
num2 = float(input('Digite o SEGUNDO número: '))
escolha = input('Qual operação deseja fazer: ')
if escolha == '+':
   resultado = num1+num2 
   print('O resultado da adição entre {} e {} é: {:.2f}' .format(num1,num2,resultado))
elif escolha == '-':
    resultado = num1-num2 
    print('O resultado da subtração entre {} e {} é: {:.2f}' .format(num1,num2,resultado))
elif escolha == '*':
    resultado = num1*num2 
    print('O resultado da multiplicação entre {} e {} é: {:.2f}' .format(num1,num2,resultado))
elif escolha == '/':
    resultado = num1/num2 
    print('O resultado da divisão entre {} e {} é: {:.2f}' .format(num1,num2,resultado))
else:
    print('Operação inexistente!')