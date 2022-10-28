# # Vai contando de 1 até 10
# for c in range(1,10):
#     print(c)

# print()
# print('--//--//--//--//--')
# print()
# # Vai contando de 1 até 10, mas ele vai pular um número conforme informado
# for c in range(1,10,2):
#     print(c)

# print()
# print('--//--//--//--//--')
# print()

# for i in range(1,7):
#     print('{} Oi'.format(i))
# print('FIM')

# print()
# print('--//--//--//--//--')
# print()

# for i in range(7, 0, -1):
#     print('{} OI'.format(i))
# print('FIM')

# print()
# print('--//--//--//--//--')
# print()

# for i in range(7, 0, -2):
#     print(i)

# print()
# print('--//--//--//--//--')
# print()

# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Pula: '))
# for c in range(i, f+1, p): # Com +1 ele vai somar no ultimo número, em vez de acabar no 9 ele acaba no 10, conforme mencionado no inicio
#     print(c)

# for c in range(0,3):
#     n = int(input('Digite um valor: '))
# print('FIM')

s = 0
for c in range(0,3):
    n = int(input('Digite um Valor: '))
    s += n
print('Fim ',s)