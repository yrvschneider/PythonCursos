# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alu1 = 'Florinda'
alu2 = 'Madruga'
alu3 = 'Chaves'
alu4 = 'Kiko'

lista = [alu1,alu2,alu3,alu4]
random.shuffle(lista)

print(lista)