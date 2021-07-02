# Ler dois valores numéricos inteiros e caso seja par imprimir uma mensagem informando, do mesmo jeito caso seja ímpar

# Passo 1: Definindo strings
num = float(input('Digite um número: '))

# Passo2: Montando o algoritmo
if num%2 == 0:
    print('O número digitado é par.')
else:
    print('O número digitado é ímpar.')
if num%7 == 0:
    print('O número é multiplo de sete.')