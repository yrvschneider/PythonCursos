# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#  calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

altura = float(input('Digite sua altura em centimetros: '))
peso = int(input('Digite seu peso: '))
imc = peso / (altura*altura)

if imc < 18.5:
    print('Seu IMC é {:.2f} - Abaixo do Peso'.format(imc))
elif imc < 25:
    print('Seu IMC é {:.2f} - Peso Ideal'.format(imc))
elif imc < 30:
    print('Seu IMC é {:.2f} - Sobrepeso'.format(imc))
elif imc < 40:
    print('Seu IMC é {:.2f} - Obesidade'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f} - Obesidade Mórbida'.format(imc))