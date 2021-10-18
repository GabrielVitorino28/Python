# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.

sp = 0
np = 0
ni = 0

for c in range(1, 7):
    n = int(input('Insira o {}° dos 6 números inteiros: '.format(c)))
    if n % 2 == 0:
        sp += n
        np += 1

if np != 0:
    print('\nA soma dos {} números pares inseridos foi igual a {}'.format(np, sp))

elif np == 0:
    print('\nNenhum número par foi inserido, logo, a soma dos pares foi igual a 0')