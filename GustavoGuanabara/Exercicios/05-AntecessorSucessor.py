# Faça um programa que leia um número inteiro
#  e mostre na tela o seu sucessor e antecessor.

n = int(input('Digite um número: '))
print('''
    Número: {}
    Sucessor: {}
    Antecessor: {}
'''.format(n,n+1,n-1))