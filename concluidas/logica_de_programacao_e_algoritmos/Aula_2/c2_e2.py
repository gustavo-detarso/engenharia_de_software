# Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos e de segundos. Calcule o total de segundos e imprima na tela para o usuário.

# Passo 1: definição da strings:
# Tela de indicativo a que se propõe o programa
print('Conversor para segundos')
dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))
soma = (dias*24*60*60)+(horas*60*60)+(minutos*60)+segundos
# Passo 2: Montagem do programa:
print('A conversão dos valores para segundos é de: {}' .format(soma))