# Desenvolva um programa que leia as duas notas de um aluno, cacule e mostre a média.

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

print('''
    Nota 1: {}
    Nota 2: {}
    Média: {:.2f}
'''.format(n1,n2,(n1+n2)/2))