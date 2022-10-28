# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

n = int(input('Digite um número: '))
resto = n % 2

if resto == 0:
    print('PAR')
elif resto == 1:
    print('IMPAR')