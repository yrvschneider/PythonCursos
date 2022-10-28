# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra 'A'.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.

frase = str('Fim da novela Pantanal, eleições e outras frases da semana').upper()
total = frase.count('A')
pri = frase.find('A')
ult = frase.rfind('A')

print('''
    Total de letras A: {}
    Primeira Posição da letra A: {}
    Ultima Posição da Letra A: {}
'''.format(total, pri, ult))