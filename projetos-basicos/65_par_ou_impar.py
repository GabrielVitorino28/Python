# Programa que joga par ou ímpar com o jogador, parando somente quando o jogador perder, mostrando no final o número de vitórias consecutivas que ele alcançou.

from random import randint
from time import sleep

vitorias = 0

while True:
    print('-'*30)
    while True:
        print('Insira uma opção entre Par ou Ímpar.')
        jogador = str(input('Par ou Ímpar [P/I]? ')).strip().upper()
        if jogador[0] == 'P' or jogador[0] == 'I':
            break
        print('-'*30)
        print('O valor inserido não é uma opção de Par ou Ímpar.')
        
    if jogador[0] == 'P':
        print('-'*30)
        print('Você escolheu PAR.')
        print('Eu escolhi ÍMPAR.')
    elif jogador[0] == 'I':
        print('-'*30)
        print('Você escolheu ÍMPAR.')
        print('Eu escolhi PAR.')

    print('-'*30)

    while True:
        njogador = int(input('Escolha um número inteiro entre 0 e 10: '))
        if 0 <= njogador <= 10:
            break
        print('-'*30)
        print('O valor inserido não é um número entre 0 e 10.')

    ncomp = randint(0, 10)
    soma = njogador + ncomp

    if soma % 2 == 0:
        print('-'*30)
        print(f'Você escolheu {njogador} e eu escolhi {ncomp}, logo a soma dos números é {soma}, que é um número PAR!')
        if jogador[0] == 'P':
            vitorias += 1
            print('Você ganhou! Vamos jogar novamente!')
        elif jogador[0] == 'I':
            break
    elif soma % 2 != 0:
        print('-'*30)
        print(f'Você escolheu {njogador} e eu escolhi {ncomp}, logo a soma dos números é {soma}, que é um número ÍMPAR!')
        if jogador[0] == 'P':
            break
        elif jogador[0] == 'I':
            vitorias += 1
            print('Você ganhou! Vamos jogar novamente!')

print('-'*30)
print(f'Você perdeu!\nVocê conseguiu um total de {vitorias} vitórias!\nFIM DE JOGO')
print('-'*30)
sleep(1)