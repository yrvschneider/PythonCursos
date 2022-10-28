# Elabore um programa que calcule o valor a ser pago por um produto,
#  considerando o seu preço e condição de pagamento:
# - À Vista Dinheiro/Cheque: 10% de Desconto
# - À Vista no Cartão: 5% de Desconto
# - Em até 2x no Cartão: Preço Normal
# - 3x ou mais no Cartão: 20% de Juros

preco = float(input('Preço do produto: R$'))
print(''''
    [ 1 ] - À Vista Dinheiro/Cheque: 10% de Desconto
    [ 2 ] - À Vista no Debito: 5% de Desconto
    [ 3 ] - Em até 2x no Cartão: Preço Normal
    [ 4 ] - 3x ou mais no Cartão: 20% de Juros
''')
opcao = int(input('Opção de pagamento: '))

if opcao == 1:
    print('''
    [ 1 ] - Dinheiro
    [ 2 ] - Cheque
    ''')
    escolha = int(input('Forma de pagamento? '))
    if escolha == 1:
        print('''
        Preço Original R${:.2f}
        Desconto de 10% no dinehiro R${:.2f}
        '''.format(preco, preco-((preco*10)/100)))
    elif escolha == 2:
        print('''
        Preço Original R${:.2f}
        Desconto de 10% no cheque R${:.2f}
        '''.format(preco, preco-((preco*10)/100)))
elif opcao == 2:
    print('''
    Preço Original R${:.2f}
    Desconto de 5% debito R${:.2f}
    '''.format(preco, preco-((preco*5)/100)))
elif opcao == 3:
    vezes = int(input('1x ou 2x? '))
    print('''
    No Credito {}x R${:.2f}
    Total R${:.2f}
    '''.format(vezes,preco/vezes,preco))

elif opcao == 4:
    vezes = int(input('3x ou mais? '))
    acrecimo = preco+((preco*20)/100)
    print('''
    Opção com acrecimo de 20%
    No Credito {}x R${:.2f}
    Total R${:.2f}
    '''.format(vezes,acrecimo/vezes,acrecimo))
else:
    print('Não tem esta opção, tente novamente.')