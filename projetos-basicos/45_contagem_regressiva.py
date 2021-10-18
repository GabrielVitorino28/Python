# Programa que faz uma contagem regressiva para a queima de fogos de artifício na virada do ano.

from time import sleep

print('A contagem regressiva para a virada está prestes a começar!')

sleep(1)

for c in range(10, -1, -1):
    print('Faltam {} segundos'.format(c))
    sleep(1)

print('\nBUUUUM! FELIZ ANO NOVO!!')
