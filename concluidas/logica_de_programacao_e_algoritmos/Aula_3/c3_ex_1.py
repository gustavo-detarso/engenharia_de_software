# Ler dois valores numéricos inteiros e comparar se o primeiro é maior do que o segundo, utilizando uma condicional simples. Caso seja verdadeiro, ele imprime na tela a mensagem informando que o primeiro valor digitado é maior que o segundo

# Passo 1: Definindo strings
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

# Passo2: Montando o algoritmo
if num1 > num2:
    print('O primeiro número é maior do que o segundo número.')
if num1 < num2:
    print('O segundo número é maior do que o primeiro número.')
if num1 == num2:
    print('Os dois números digitados são iguais.')