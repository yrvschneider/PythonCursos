nome = str(input('Qual é seu nome? '))

if nome == 'Yuri':
    print('Que nome lindo {}'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome {}'.format(nome))
else: # else pode ser opcional para utilizar em alinhamento.
    print('Seu nome é bem normal, {}'.format(nome))
print('Tenha um bom dia, {}'.format(nome))

