# Crie um programa que faça o computador jogar JOKEMPO com voce.

import random
print('''
    [ 0 ] - Pedra
    [ 1 ] - Papel
    [ 2 ] - Tesoura
''')

opcao = int(input('Opção: '))
pc = random.randint(0,2)
itens = ('Pedra', 'Papel', 'Tesoura')

if opcao == 0 and pc == 2 or opcao == 1 and pc == 0 or opcao == 2 and pc == 1:
    print('''
        GANHOU!
    Escolha: {}
    Computador: {}
    '''.format(itens[opcao],itens[pc]))
elif opcao == pc:
        print('''
        EMPATE!
    Escolha: {}
    Computador: {}
    '''.format(itens[opcao],itens[pc]))
else:
    print('''
        PERDEU!
    Escolha: {}
    Computador: {}
    '''.format(itens[opcao],itens[pc]))