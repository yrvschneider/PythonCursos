# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

lista_peso = []

for i in range(6):
    peso = float(input('Digite um peso: '))
    lista_peso.append(peso)
lista_peso.sort()
print('''
    Maior peso: {}
    Menor peso: {}
'''.format(lista_peso[0], lista_peso[-1]))