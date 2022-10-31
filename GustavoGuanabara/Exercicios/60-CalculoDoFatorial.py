# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5! = 5x4x3x2x1 = 120

n = int(input('Digite um valor: '))
fet = n
while n != 1:
    n -= 1
    print('{} * {}'.format(fet,n), end=' = ')
    fet = fet * n
print('{} FIM!'.format(fet))