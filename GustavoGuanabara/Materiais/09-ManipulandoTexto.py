frase = 'Curso em Video Python'
frase1 = '   Aprenda Python  '

# FATIAMENTO

print(frase[9:13]) # Vai começar do indice 9 e parar no indice 13
print(frase[9:21:2]) # Vai começar no indice 9 e parar no indice 21, mas ele vai pulando 2 indices por vez até chegar no 21
print(frase[:5]) # Vai iniciar do indice 0 até o indice 5
print(frase[15:]) # Vai iniciar no indice 15 e vai até o final
print(frase[9::3]) # Vai iniciar no indice 9 e vai até o final, mas vai pulando a cada 3 indices

# ANÁLISAR

print(len(frase)) # Vai infgormar quantos indices tem
print(frase.count('o')) # Vai contar quantos 'o' tem na frase
print(frase.count('o', 0, 13)) # Vai contar quantos 'o' tem na frase até o indice 13. Sabemos que ele ira ler até o indice 12
print(frase.find('deo')) # Ele ira mostrar em indice a onde começa o 'dao'
print(frase.find('Android')) # Se passar um indice que não existe na variavel, ele ira te retornar -1, e o indice -1 não existe
print('Curso' in frase) # Se escrever desse modo, ele ira procurar se existe este indice e te retornar True ou False. Sabemos que no Pyhton tem a diferença entre letra maiscula e minuscula.

# TRANSFORMAÇÃO

print(frase.replace('Python','Android')) # Ele ira trocar o indice pelo indice informado, de modo segundario que só ira trocar neste momento que utiliza este comando.
print(frase.upper()) # Ira trocar todas as letras que são minusculas por maisculas
print(frase.lower()) # Ira trocar todas as letras maisculas por minusculas
print(frase.capitalize()) # Ira pegar todos os indices que estão maisculos e jogar para minusculo, somente o primeiro indice que ira ficar maisculo.
print(frase.title()) # Ira seperar a frase por palavra e deixar cada palavra com a iniciar maiscula
print(frase1.strip()) # Ira retirar os espaços inuteis, como os espaços que podem estar no inicio de uma frase e no final, que não tem nada a ver com a frase.
print(frase1.rstrip()) # Ira remover somente os espaços desnecessarios da direita da frase
print(frase.lstrip()) # Ira remover somonete os espasços desnecessarios da esquerda da frase
print(frase[::-1]) # Ira inverter a frase ou palavra

# DIVISÃO

print(frase.split()) # Ira separar uma string palavra por palavra e criar uma lista

# JUNÇÃO

print('-'.join(frase)) # Ele ira juntar uma string que esta em lista