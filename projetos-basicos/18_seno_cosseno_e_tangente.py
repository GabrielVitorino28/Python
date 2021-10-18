# Programa que lê um ângulo qualquer e mostra os valores do seno, cosseno e tangente desse ângulo.

import math

ag = float(input('Insira o valor de um ângulo qualquer (em graus): '))

ar = math.radians(ag)

sa = math.sin(ar)
ca = math.cos(ar)
ta = math.tan(ar)

print('O seno de {}° é igual a {:.2f}!'.format(ag, sa))
print('O cosseno de {}° é igual a {:.2f}!'.format(ag, ca))
print('A tangente de {}° é igual a {:.2f}!'.format(ag, ta))