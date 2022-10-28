# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1.250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salaraio = float(input('Digite o seu salario: '))
base = 1250.00

if salaraio > base:
    aumento = salaraio+((salaraio*10)/100)
    print('Novo salario {:.2f}'.format(aumento))
elif salaraio <= base:
    aumento = salaraio+((salaraio*15)/100)
    print('Novo salario {:.2f}'.format(aumento))