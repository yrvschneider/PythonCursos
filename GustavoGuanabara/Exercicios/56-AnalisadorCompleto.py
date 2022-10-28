# Desenvolva um programa que leia o nome, idade e sexo
#  de 4 pessoas. No final mostre:

# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

lista_Masculino = []
menos_de_20 = 0
media_idade = int(0)
for i in range(5):
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo Masculino M ou Feminino F: ')).upper()
    media_idade += idade

    if sexo == 'M':
        tupla = (idade, nome)
        lista_Masculino.append(tupla)
    if sexo == 'F' and idade < 20:
        menos_de_20 += 1

lista_Masculino.sort()

print('''
    Média de idade do grupo: {:.0f}
    Homem mais velho: {}
    Total de Mulheres com menos de 20 anos: {}
'''.format(media_idade/2, lista_Masculino[-1][-1], menos_de_20))