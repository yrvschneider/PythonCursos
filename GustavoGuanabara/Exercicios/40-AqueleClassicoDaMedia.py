# Crie um programa que leia duas notas de um aluno e calcule sua média,
#  msotrando uma mensagem no final, de acordo com a média antingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1+n2)/2

if media < 5.0:
    print('REPROVADO - Média {:.2f}'.format(media))
elif media > 5.0 and media < 6.9:
    print('RECUPERAÇÃO - Média {:.2f}'.format(media))
elif media >= 7.0:
    print('APROVADO - Média {:.2f}'.format(media))