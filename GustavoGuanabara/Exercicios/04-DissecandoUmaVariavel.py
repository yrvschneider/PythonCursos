# Faça um programa que leia algo pelo teclado e mostre
#  na tela o seu tipo primitivo e todas as informaçoes.

# Tipo Primitivo
# Espaços
# Números
# Alfavetico
# Alfanumerico
# Maisculas
# Capitalizada

n = input('Digite algo: ')

print('Resultados: ')
print('Tipo Primitivo: ', type(n))
print('Espaços: ', n.isspace())
print('Números: ', n.isnumeric())
print('Alfabetico: ', n.isalpha())
print('Alfanumerico', n.isalnum())
print('Maisculas: ', n.isupper())
print('Minusculas: ', n.islower())
print('Capitalizada: ', n.istitle())