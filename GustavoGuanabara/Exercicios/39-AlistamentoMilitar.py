# Faça um programa que leia o ano de nascimento de um jovem e informe,
#  de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
#  se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá msotrar o tempo que falta ou que passou do prazo.

from datetime import date

anoNasc = int(input('Ano de Nascimento: '))
idade = date.today().year - anoNasc
alistamento = 18

if idade < alistamento:
    falta = alistamento - idade
    print('Falta {} anos, para se alistar no serviço Militar.'.format(falta))
elif alistamento < idade:
    falta = idade - alistamento
    print('Já passou {} anos, do alistamento Militar.'.format(falta))
elif idade == alistamento:
    print('Já é hora de se alistar no setviço Militar.')