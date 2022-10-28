# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1


n = int(input('Digite um número entre 0 até 9999: '))
un = n // 1 % 10
de = n // 10 % 10
ce = n // 100 % 10
mi = n // 1000 % 10

print(''''
    Unidade: {}
    Dezena: {}
    Centena: {}
    Milhar: {}
'''.format(un, de, ce, mi))