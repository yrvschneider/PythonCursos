# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todos as letras maisculas.
# O nome com todas letras minusculas.
# Quantas letras ao todo (sem considerar os espaços).
# Quantas letras tem o primeiro nome.

nome = str('Yuri Ricardo Verardo Schneider')

maiscula = nome.upper()
minuscula = nome.lower()
letras = len(nome.replace(' ', ''))
primeiro = nome.split()
print('''
    Letras Maisculas: {}
    Letras Minusculas: {}
    Total de Letras: {}
    Quantas letras tem o primeiro nome: {}
'''.format(maiscula, minuscula, letras, len(primeiro[0])))