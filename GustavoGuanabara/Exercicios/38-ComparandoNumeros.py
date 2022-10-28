# Escreva um programa que leia dois números inteiros e compare-os,
#  mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existre valor maior, os dois são iguais.

n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))

if n1 > n2:
    print('Primeiro Número é Maior!')
elif n2 > n1:
    print('Segundo Número é Maior!')
elif n1 == n2:
    print('Não existre valor maior, os dois são iguais.')