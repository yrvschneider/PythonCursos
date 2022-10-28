# Um professor quer sortear um dos seus quatro alunos para apagar oquadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.


import random


alu1 = 'Monica'
alu2 = 'Cascao'
alu3 = 'Coelho'
alu4 = 'Alex'

lista = [alu1, alu2, alu3, alu4]
sorteio = random.choice(lista)
print('Aluno Sorteado: ',sorteio)