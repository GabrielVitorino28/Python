# Programa que lê dois números inteiros e compara-os, mostrando na tela uma das seguintes mensagens:
# - "O primeiro valor é maior"
# - "O segundo valor é maior"
# - "Não existe valor maior, os dois são iguais"

cores = {'azulneg': '\033[1;34m',
         'lilasneg': '\033[1;35m',
         'amareloneg': '\033[1;33m',
         'vermelhoneg': '\033[1;31m',
         'limpa': '\033[m'}

n1 = int(input('Insira o {}primeiro número inteiro{}: '.format(cores['amareloneg'], cores['limpa'])))
n2 = int(input('Insira o {}segundo número inteiro{}: '.format(cores['vermelhoneg'], cores['limpa'])))

if n1 > n2:
    print('O {}primeiro valor{} é o {}maior{}.'
          .format(cores['amareloneg'], cores['limpa'], cores['azulneg'], cores['limpa']))

elif n2 > n1:
    print('O {}segundo valor{} é o {}maior{}.'
          .format(cores['vermelhoneg'], cores['limpa'], cores['azulneg'], cores['limpa']))

elif n2 == n1:
    print('{}Não existe{} valor maior, os dois são {}iguais{}.'
          .format(cores['lilasneg'], cores['limpa'], cores['azulneg'], cores['limpa']))