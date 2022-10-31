## Repetidor com limite já informado.
# c = 1
# while c < 10+1:
#     print(c)
#     c += 1
# print('FIM')

## Repetidor com limete que ira ser digitado quando quiser parar
# n = 1
# while n != 0:
#     n = int(input('Digite um valor: '))
# print('FIM')

## Repetidor com continuação Sim ou Não
# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N] ')).upper()
# print('FIM')

## 
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        elif n % 2 == 1:
            impar += 1
print('Acabou!')
print('Pares', par)
print('Impares', impar)