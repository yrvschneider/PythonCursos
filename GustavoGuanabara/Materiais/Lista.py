# lista_comopras = ['banana', 'maçã', 'laranja']
# print(lista_comopras)
# print()
# print(lista_comopras[1])
# print()
# lista_comopras.append('beterraba') # Ira iraadicionar o item no fim da lista.
# print(lista_comopras)
# print()
# lista_comopras.insert(1, 'chocolate') # Ira adionar um item na posição que escolher. Ele não ira apagar o item que estiver na posição e sim, empurrar ele para frente
# print(lista_comopras)
# print()
# del lista_comopras[4] # Ira deletar o item que esolher., usando o indice da posição.
# print(lista_comopras)
# print()
# lista_comopras.remove('chocolate') # Ira remover o item escolhido, mas ira digitar o nome do item.
# print(lista_comopras)
# print()
# lista_comopras.append('carro')
# print(lista_comopras)
# print()

# lista_sonhos = [] # Criando nova lista
# sonho = lista_comopras.pop(-1) # Ira retirar o ultimo item da lista para adicionar na variavel sonho
# print(lista_comopras)
# print(sonho)
# print()
# lista_sonhos.append(sonho) # Agora ira adicionar o item da variavel sonho na lista_sonhos
# print(lista_comopras)
# print(lista_sonhos)

# tarefas = []
# tarefa = input('Insira uma tarefa: ')
# while tarefa != '':
#     tarefa = input('Insira uma tarefa: ')
#     tarefas.append(tarefa)
# del tarefas[-1]
# print(tarefas)

lojas = ['Rio de Janeiro', 'São Paulo', 'Porto Alegre']
faturamento = [10000, 20000, 5000]
print(lojas)
print(faturamento)
print()
#faturamento.sort()
#faturamento.sort(reverse = True) # 'sort' sempre ira ordernar do Menor para o Maior. 'reverse = True' vai ordernar do Maior para o Menor
print(faturamento)
print()
resultados = []
for i in range(3):
    tupla = (lojas[i-1], faturamento[i-1]) # Aqui estamos cliando uma tupla, que ira juntar informações de varias listas e criar uma lista organizada das caracteristicas dos itens.
    resultados.append(tupla)
print(resultados)
print()
print(resultados[1][1])