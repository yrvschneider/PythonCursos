# Crie um programa que leia uma frase qualquer e
#  diga se ela é um palindromo, desconsiderando os espaços.

# Exemplo:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).upper().strip().split()
junta = ''.join(frase)
inverter = str(junta[::-1])

if junta == inverter:
    print('É um Palindromo!')
else:
    print('Não é um Palindromo!')