# Programa que lê o nome de quatro alunos e sorteia uma ordem aleatória para exibi-los

from random import shuffle

a1 = str(input('Insira o nome do(a) primeiro(a) aluno(a): '))
a2 = str(input('Insira o nome do(a) segundo(a) aluno(a): '))
a3 = str(input('Insira o nome do(a) terceiro(a) aluno(a): '))
a4 = str(input('Insira o nome do(a0 quarto(a) aluno(a): '))

lista = [a1, a2, a3, a4]

shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))