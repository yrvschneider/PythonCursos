# Crie um algoritimo que leia um número e mostre seu
#  dobro, triplo e raiz quadrada.

import math

n = int(input('Digite um número: '))
print('''
    Entrada: {}
    Resultado
        Dobro: {}
        Triplo: {}
        Raiz Quadrada: {:.2f}
'''.format(n,n*2,n*3,math.sqrt(n)))