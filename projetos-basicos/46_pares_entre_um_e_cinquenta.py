# Programa que exibe todos os números pares que estão no intervalo entre 1 e 50.

from time import sleep

np = 0

for c in range(2, 51, 2):
    if c % 2 == 0:
        print('O número {} é par.'.format(c))
        np += 1
        sleep(0.25)

print("No total, existem {} números pares entre 1 e 50".format(np))