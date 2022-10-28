# Refaça o DESAFIO 009, mostrando a tabuada de um
#  número que o usuário escolher, só que agora
#  utilizando um laço for.

print('ESCOLHA UM NÚMERO PARA VER SUA TABUADA')
n = int(input('Digite um número: '))
print()
print('TABUADA de',n)
for i in range(1,10+1):
    tabu = n * i
    print('{} x {} = {}'.format(i,n,tabu))