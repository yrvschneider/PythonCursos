# Desenvolva um programa que leia o primeiro termos e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

for i in range(0, 10):
    print('{} '.format(termo), end='-> ')
    termo += razao
print('ACABOU')