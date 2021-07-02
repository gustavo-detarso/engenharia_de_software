# Desenvolva um algoritmo que converta uma temperatura em Celsius (C) para Fahrenheit (F).
# Passo 1: criando as strings
# Definição do que o algoritmo se propõe:
print('Conversor de Celsius para Fahrenheit')
celsius = float(input('Digite a temperatura em graus Celsius (ºC): '))
conversao = (9*celsius)/5+32
# Passo 2: Montando o algoritmo
print('A temperatura de {}ºC corresponde a {}ºF' .format(celsius,conversao))