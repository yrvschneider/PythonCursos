# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Preço Produto: R$'))

print('''
    Preço do Produto: R${:.2f}
    Preço com 5% de desconto: R${:.2f}
'''.format(preco,preco-((preco*5)/100)))