# Programa que lê um ano e mostra se ele é BISSEXTO.

from datetime import date

a = int(input('Que ano você quer analisar? Coloque "0" para analisar o ano atual: '))

if a == 0:
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {} é bissexto!'.format(a))

else:
    print('O ano de {} não é bissexto!'.format(a))
