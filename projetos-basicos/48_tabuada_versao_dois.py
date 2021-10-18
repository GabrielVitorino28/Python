# Programa que lê dois números inteiros e calcula a tabuada do primeiro até chegar no seu produto com o segundo número.

from time import sleep

n = int(input('Insira um número inteiro para ver sua tabuada: '))
l = int(input('Até qual múltiplo você gostaria de ver a tabuada? '))

print('='*20)

for c in range(1, l + 1):
    mp = n * c
    print('{} x {} = {}'.format(n, c, mp))
    print('='*20)
    sleep(0.5)
