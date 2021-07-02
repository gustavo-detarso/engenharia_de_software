# Algoritmo para aprovação em três matérias (média > 7). Caso não possua aprovação em uma delas, deverá repetir o semestre.

# Passo 1: definição de variáveis
nome = str(input('Digite o nome do aluno: '))
disciplina1 = str(input('Digite o nome da disciplina: '))
nota1_disciplina1 = float(input('Digite a primeira nota da disciplina {}: ' .format(disciplina1))) 
nota2_disciplina1 = float(input('Digite a segunda nota da disciplina {}: ' .format(disciplina1))) 
nota3_disciplina1 = float(input('Digite a terceira nota da disciplina {}: ' .format(disciplina1)))
media_disciplina1 = (nota1_disciplina1+nota2_disciplina1+nota3_disciplina1)/3
disciplina2 = str(input('Digite o nome da disciplina: '))
nota1_disciplina2 = float(input('Digite a primeira nota da disciplina {}: ' .format(disciplina2))) 
nota2_disciplina2 = float(input('Digite a segunda nota da disciplina {}: ' .format(disciplina2))) 
nota3_disciplina2 = float(input('Digite a terceira nota da disciplina {}: ' .format(disciplina2)))
media_disciplina2 = (nota1_disciplina2+nota2_disciplina2+nota3_disciplina2)/3
disciplina3 = str(input('Digite o nome da disciplina: '))
nota1_disciplina3 = float(input('Digite a primeira nota da disciplina {}: ' .format(disciplina3))) 
nota2_disciplina3 = float(input('Digite a segunda nota da disciplina {}: ' .format(disciplina3))) 
nota3_disciplina3 = float(input('Digite a terceira nota da disciplina {}: ' .format(disciplina3)))
media_disciplina3 = (nota1_disciplina3+nota2_disciplina3+nota3_disciplina3)/3

# Passo 2: montando o algoritmo
if media_disciplina1 and media_disciplina2 and media_disciplina3:
    print('Parabéns, você está aprovado em todas as disciplinas com as médias de {:.2f} em {}, {:.2f} em {} e {:.2f} em {}' .format(media_disciplina1,disciplina1,media_disciplina2,disciplina2,media_disciplina3,disciplina3))
else:
    print('Infelizmente você terá que repetir o semestre, seu burro!')