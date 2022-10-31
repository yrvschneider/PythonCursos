# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
n = ''
while n != 'M' and n != 'F':
    n = str(input('Digite seu sexo [M/F]: ')).upper()
    if n == 'M':
        print('Seu sexo é Masculino!')
    elif n == 'F':
        print('Seu sexo é Feminino!')
print('Fim!')