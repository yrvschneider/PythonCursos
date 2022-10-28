# Faça um programa que leia o comprimento do cateto oposto
#  e do cateto adjacente de um triangulo, retangulo,
#  calcule e mostre o comprimento da hipotenusa.

ca = float(input('Cateto: '))
ad = float(input('Adjacente: '))
hi = (ca ** 2 + ad ** 2) ** (1/2)

print('Cumprimento da Hipotenusa {:.2f}'.format(hi))