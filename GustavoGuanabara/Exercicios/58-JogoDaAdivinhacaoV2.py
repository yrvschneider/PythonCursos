# Melhore o jogo do DESAFIO 028 onde o computador
#  vai "pensar" em um número entre 0 e 10.
# Só que agora o jogardor vai tentar adivinhar até
#  acertar, mostrando no final quantos palpites foram
#  necessários para vencer.

import random

pc = 0
eu = 1
contador = 0

while pc != eu:
    pc = random.randrange(10)
    eu = random.randrange(10)#int(input('Digite um valor de 1 até 10: '))
    contador += 1
    if eu == pc:
        print('\033[34mVoce Ganhou!')
        print('[PC {}] x [Tu {}]'.format(pc, eu))
    elif pc != eu:
        print('\033[31mPerdeu!')
        print('[PC {}] x [Tu {}]'.format(pc, eu))
print('Tentativas', contador)
print('Fim!')