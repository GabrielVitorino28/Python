# Versão melhorada do projeto 28 (Jogo da Adivinhação), onde o computador também irá "pensar" em um número entre 0 e 10. No entanto, neste programa o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

nc = randint(0, 10)
nt = 1

nj = int(input('Estou pensando em um número inteiro entre 0 e 10, qual você acha que é? '))

if nj > 10 or nj < 0:
    nt -= 1
    print('\nEsse número não está entre 0 e 10, logo não tem como eu ter pensado nele...')
    print('Vou te ajudar nessa: essa tentativa não irá contar!')

while nj != nc:
    nt += 1
    nj = int(input('\nNão era nesse número que eu estava pensando... Tem algum outro palpite? '))
    if nj > 10 or nj < 0:
        print('\nEsse número não está entre 0 e 10, logo não tem como eu ter pensado nele...')
        print('Vou te ajudar nessa: essa tentativa não irá contar!')
        nt -= 1

if nt > 1:
    print('\nParabéns! Eu estava pensando no número {} e você descobriu isso em apenas {} tentativas!'.format(nc, nt))
if nt == 1:
    print('\nUau! Estou impressionado! Você só precisou de 1 tentativa para descobrir que eu estava pensando'
          ' no número {}!'.format(nc))
