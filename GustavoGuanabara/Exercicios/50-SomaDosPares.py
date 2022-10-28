# Desenvolva um programa que leia seis números inteiros e 
# mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o.

soma = 0
for i in range(1, 6+1):
    n = int(input('Digite um Número: '))
    if n%2 == 0:
        soma += n
print('A soma de todos os números Pares que foi digitado é',soma)