# Faça um programa que leia um número inteiro e
#  diga se ele é ou não um número primo.

n = int(input('Digite um Número: '))
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[m O Número {} foi divisível {}x'.format(n, total))
if total == 2:
    print('\033[34m É número Primo!')
else:
    print('\033[31m Não é número Primo!')