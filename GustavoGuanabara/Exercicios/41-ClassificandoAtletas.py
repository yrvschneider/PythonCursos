# A Confederação Nacional de Natação precisa de um programa que leia
#  o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SENIOR
# - Acima de 25 anos: MASTER

from datetime import date

ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('MRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')