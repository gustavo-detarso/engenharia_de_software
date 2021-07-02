# Escreva um algoritmo que lê um valor inteiro qualquer. Após, verifique se este valor está contido dentro dos seguintes intervalos -100 < x < -1 e 1<x<100. Imprima na tela uma mensagem caso ele esteja em um dos intervalos.

# Passo 1: definindo variáveis

num = int(input('Digite um valor inteiro: '))
if num >= -100 and num <= -1 or num >= 1 and num <= 100:
    print('Um dos critérios foi atendido')