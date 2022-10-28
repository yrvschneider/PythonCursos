# Desenvolva um programa que leia o comprimento de
#  tres retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma im Triangulo!')
else:
    print('Não forma um Triangulo!')