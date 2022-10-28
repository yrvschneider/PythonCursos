# Escreva um progama que faça o computador "pensar"
#  em um número inteiro entre 0 e 5 e peça para o
#  usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

pc = random.randrange(5)
n = int(input('Digite um número de 0 até 5: '))

if n == pc:
    print('Voce Ganhou!')
else:
    print('Voce Perdeu!')

print('Numero Sorteado! ',pc)