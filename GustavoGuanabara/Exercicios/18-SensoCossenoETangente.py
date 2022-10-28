# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

import math

angulo = float(input('Digite o Angulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(''''
    Angulo: {}
    Seno: {:.2f}
    Cosseno: {:.2f}
    Tangente: {:.2f}
'''.format(angulo,seno,cosseno,tangente))