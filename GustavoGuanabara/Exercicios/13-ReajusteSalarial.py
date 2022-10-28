# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Salário R$'))
aumento = 15

print(''''
    Salário R${:.2f}
    Novo Salário R${:.2f}
    Aumento de {}% R${:.2f}
'''.format(salario,salario+((salario*aumento)/100),aumento,(salario*aumento)/100))