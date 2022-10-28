# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram
#  a maioridade e quantas já são maiores.

from datetime import date

lista_ano_menor = []
lista_ano_maior = []

for i in range(8):
    ano = int(input('Insira o ano de nascimento: '))
    if ano > date.today().year - 18:
        lista_ano_menor.append(ano)
    else:
        lista_ano_maior.append(ano)
print('''
    Total de Menores de idade: {}
    Total de Maiores de idade: {}
'''.format(len(lista_ano_menor),len(lista_ano_maior)))