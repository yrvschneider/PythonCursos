# Refaça o RESAFIO 035 dos triangulos, acrecentando o recurso de mostrar que tipo de trianguloserá formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Forma um Triangulo: Equilátero - Todos os lados iguais.')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2:
        print('Forma um Triangulo: Isósceles - Dois lados iguais.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Forma um Triangulo: Escaleno - Todos os lados diferentes.')
else:
    print('Não forma um Triangulo.')