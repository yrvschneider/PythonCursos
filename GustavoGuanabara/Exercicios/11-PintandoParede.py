# Faça um programa que leia a largura e a altura de uma parede em metros,
#  calcule a sua área e a quantidade de tinta necessária para pintá-la,
#  sabendo que cada litro de tinta, pinta uma área de 2m quadrado.

l = float(input('Largura: '))
a = float(input('Altura: '))

m2 = l*a

print(''''
    Metro Quadrado: {:.2f}
    Tinta Nescessaria: {:.3f}L
'''.format(m2,m2/2))