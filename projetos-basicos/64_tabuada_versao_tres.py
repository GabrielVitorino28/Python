# Programa que lê um número inteiro e exibe os 10 primeiros valores da tabuada do número lido, repetindo esse processo até o usuário inserir um valor negativo.

from time import sleep

while True:
    n = int(input('Insira um número inteiro para ver sua tabuada (digite um número negativo para parar): '))
    if n < 0:
        break
    print('='*30)
    for t in range(1, 11, 1):
        p = n * t
        print(f'{n} X {t} = {p}')
    print('='*30)
print('='*30)
print('Encerrando programa...')
sleep(1)