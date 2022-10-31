# Crie um programa que leia dois valores e mostre um menu.
# Seu programa deverá realizar a operação solicitada em cada caso.

# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Números
# [5] Sair do Programa

n1 = 0
n2 = 0
opcao = 0

while opcao != 5:
    n1 = int(input('Valor 1: '))
    n2 = int(input('Valor 2: '))
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
    ''')
    opcao = int(input('Opção: '))
    
    if opcao == 1:
        print('A Soma entre {} e {} = {}'.format(n1,n2,n1+n2))
    elif opcao == 2:
        print('A Multiplicação entre {} e {} = {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('O Maior número entre {} e {} é {}'.format(n1,n2,n1))
        else:
            print('O Maior número entre {} e {} é {}'.format(n1,n2,n2))
    elif opcao == 4:
        print('Digite novos números')
print('Fim!')