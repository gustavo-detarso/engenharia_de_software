# Desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual. Calcule sua idade e apresente na tela. Após, verifique se a idade é maior ou menor do que dezoito anos.

# Passo 1: definição de strings
ano_nasc = int(input('Digite o seu ano de nascimento: '))
ano_corrente = int(input('Digite seu ano atual: '))
idade = ano_corrente - ano_nasc

# Passo 2: montando o algoritmo
print('Você nasceu em {} e tem {} anos de idade.' .format(ano_nasc,idade))
if idade > 18:
    print('Parabéns! Você é maior de idade e já pode ser preso!')
else:
    print('Você é menor de idade, não pode comprar bebida alcóolica ainda, seu trouxa, ou então pede pra alguém maior de idade comprar pra você, seu animal!')
