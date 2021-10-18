# Programa que lê o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcula e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Qual é a medida do cateto oposto? '))
ca = float(input('Qual é a medida do cateto adjacente? '))

h = hypot(co, ca)

print('A medida da hipotenusa é igual a {:.2f}!'.format(h))
