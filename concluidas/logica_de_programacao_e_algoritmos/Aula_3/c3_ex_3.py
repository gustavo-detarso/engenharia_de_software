# Escreva um algoritmo que leia o salário do funcionário e seu tempo de empresa, e apresente a bonificação de cada funcionário na tela (30% para mais de dez anos, 20% para mais de cinco anos de empresa e 10% para todos os outros).

# Passo 1: definição de strings
salario = float(input('Digite o salário do funcionário: R$ '))
ano_de_admissao = int(input('Digite o ano de admissão na empresa: '))
ano_corrente = int(input('Digite o ano atual: '))
tempo_de_servico = ano_corrente - ano_de_admissao

# Passo 2: Montando o algoritmo
if tempo_de_servico > 10:
    bonus = salario*0.3
else:
    if tempo_de_servico > 5:
        bonus = salario*0.2
    else:
        if tempo_de_servico < 5:
            bonus = salario*0.1
print('Você tem {} anos na empresa, portanto direito a bonificação de {}% no salário. O valor a ser acrescentado no seu salário é de R$ {:.2f} sendo corrigido para R$ {:.2f}' .format(tempo_de_servico,(bonus/salario)*100,bonus,salario+bonus))