# Desenvolva um programa que pergunte a distancia de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.

viagemKM = int(201)
km = 200
cob1 = 0.50
cob2 = 0.45

if viagemKM <= km:
    preco = cob1 * viagemKM
    print('Sua viagem vai custar R${:.2f}'.format(preco))
elif viagemKM > km:
    preco = cob2 * viagemKM
    print('Sua viagem vai custar R${:.2f}'.format(preco))