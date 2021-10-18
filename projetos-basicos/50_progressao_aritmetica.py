# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

from time import sleep

pt = int(input('Insira o primeiro termo da progressão aritmética: '))
r = int(input('Agora, insira a razão da progressão aritmética: '))
f = pt + (r * 9)
n = 0

for c in range(pt, f + r, r):
    n += 1
    print('O {}° termo da progressão aritmética é {}.'.format(n, c))
    sleep(0.5)