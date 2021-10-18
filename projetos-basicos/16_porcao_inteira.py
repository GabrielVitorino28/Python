# Programa que lê um número real qualquer pelo teclado e mostra na tela a sua porção inteira.

from math import trunc

n = float(input('Insira um número real: '))

ni = trunc(n)

print('A porção inteira de {} é {}!'.format(n, ni))