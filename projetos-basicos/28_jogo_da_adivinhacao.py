# Programa que "pensa" em um número inteiro entre 0 e 5 e pede para o usuário tentar descobrir qual foi o número escolhido pelo computador, informando então se ele acertou ou errou.

from random import randint
from time import sleep

na = randint(0, 5)

ni = int(input('Estou pensando em um número inteiro entre 0 e 5, qual você acha que é? '))
print('Processando...')
sleep(1)

if ni == na:
    print('Parabéns! Era nesse número que eu estava pensando!')

else:
    print('Você errou, na verdade eu estava pensando no número {}!'.format(na))