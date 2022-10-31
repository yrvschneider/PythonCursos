# Refaça o DESAFIO 051, lendo o primeiro termo
#  e a razão de uma PA, mostrando os 10 primeiros
#  termos da progressão usando a estrutura while.

termo = int(input('Termo: '))
razao = int(input('Razão: '))
pro = 10
while pro != 1:
    print('{} '.format(termo), end=' -> ')
    termo += razao
    pro -= 1
print('Fim!')