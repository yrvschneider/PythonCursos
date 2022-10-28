# Crie um programa que leia quanto dinheiro tem na carteira e mostre  quantos Dolares ela pode comprar.
# Considere US$ 1,00 = R$ 5,33

n = float(input('Quantos reais tem em sua carteira? '))
dolar = 5.33

print('''
    Reais: R${}
    Dolar: ${}
    Posso comprar, ${:.2f} dolar.
'''.format(n,dolar,n/dolar))