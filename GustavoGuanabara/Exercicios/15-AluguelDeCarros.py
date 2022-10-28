# Escreva um programa que pergunte a quantidade de km
#  percorridos por um carro alugado e a quantidade de
#  dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

kmP = int(input('KM Percorrido: '))
dias = int(input('Dias com o Carro: '))

km = 0.15
dia = 60

print(''''
    Custo do KM percorrido R${:.2f}
    Custo de dias com o Carro: R${:.2f}
    Valor Total R${:.2f}
'''.format(kmP*km,dia*dias,(kmP*km)+(dia*dias)))