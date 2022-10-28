# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente.

# Ex: Ana Maria de Souza
# Primeiro: Ana
# Ultimo: Souza

nome = str('Yuri Ricardo Verardo Schneider').split()
pri = nome[0]
ult = nome[len(nome)-1]

print(''''
    Primeiro Nome: {}
    Ultimo Nome: {}
'''.format(pri, ult))