# Faça um programa que calcule a soma entre todos os
#  números impares que são múltiplos de tres e que se
#  encontram no intervalo de 1 até 500.

soma = 0
for i in range(1+2, 500+1, 3):
    soma += i
print('A Soma de todos os números impares multiplos de 3, até 500 da',soma)