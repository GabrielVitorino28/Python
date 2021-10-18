# Programa que lê o nome de quatro alunos, e sorteia um aluno aleatório entre eles

import random

aum = str(input('Insira o nome do(a) primeiro(a) aluno(a): '))
adois = str(input('Insira o nome do(a) segundo(a) aluno(a): '))
atres = str(input('Insira o nome do(a) terceiro(a) aluno(a): '))
aquatro = str(input('Insira o nome do(a) quarto(a) aluno(a): '))

lista = [aum, adois, atres, aquatro]

aesc = random.choice(lista)

print('O(a) aluno(a) escolhido(a) foi {}!'.format(aesc))

