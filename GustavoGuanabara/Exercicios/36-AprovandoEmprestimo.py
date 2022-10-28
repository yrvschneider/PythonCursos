# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Valor do Imovél? R$'))
salario = float(input('Qual seu salário? R$'))
anos = int(input('Em quantos anos quer pagar o Imovél? '))

meses = valorCasa / (12 * anos)
trinta = (salario*30)/100

if meses <= trinta:
    print('Seu emprestimo foi Aprovado!')
    print('Valor da Parcela R${:.2f}'.format(meses))
else:
    print('Seu emprestimo foi Negado!')
    print('Valor da Parcela R${:.2f}'.format(meses))