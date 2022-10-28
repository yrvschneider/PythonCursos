# Crie um programa que mostre na tela todos os
#  números pares que estão no intervalo entre 1 e 50.

# for i in range(1+1, 50+1, 2):
#     print(i)

for i in range(1, 50+1):
    par = i % 2
    if par == 0:
        print(i)