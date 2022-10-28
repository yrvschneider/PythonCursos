# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km/h acima do limite.

carro = int(input('Velocidade do Carro: '))
veloMax = 80
valor = float(7)

if carro > veloMax:
    multa = (carro - veloMax) * valor
    print('''
        Veolcidade da via {}km/h
        Velocidade do carro {}km/h
        Multa R${:.2f}
    '''.format(veloMax,carro,multa))
else:
    print('''
        Velocidade da via {}km/h
        Velocidade do carro {}km/h
    '''.format(veloMax,carro))