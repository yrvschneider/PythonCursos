# Escreva um programa que converta uma temperatura digitada em 
# °C e converta para °F.

grauC = int(input('Grau Celsius: '))
grauF = (grauC * 9/5) + 32

print('''
    Grau Celsius {:.0f}°C
    Grau Fahrenheit {:.0f}°F
'''.format(grauC,grauF))