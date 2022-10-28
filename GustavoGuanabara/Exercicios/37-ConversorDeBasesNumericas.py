# Escreva um programa que leia um número inteiro qaulquer e peça para o usuário escolher qual será a base de conversão.
# 1 para Binário
# 2 para Octal
# 3 para Hexadecimal

print('Vamos converter um número inteiro para Binário, Octal ou Hexadecimal.')
print()
n = int(input('Digite um número: '))
print(''''
    [1] - BINÁRIO
    [2] - OCTAL
    [3] - HEXADECIMAL
''')
opcao = int(input('Opção: '))

if opcao == 1:
    binario = bin(n)
    print('Binário: {}'.format(binario[2:]))
elif opcao == 2:
    octal = oct(n)
    print('Octal: {}'.format(octal[2:]))
elif opcao == 3:
    hexadecimal = hex(n)
    print('Hexadecimal: {}'.format(hexadecimal[2:]))
else:
    print('opção incorreta, tente novamente.')