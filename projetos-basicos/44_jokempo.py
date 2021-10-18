# Programa que joga Jokempô com o usuário.

import random
from time import sleep

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

jokempo = [pedra, papel, tesoura]

escolhac = random.choice(jokempo)

print('Vamos jogar jokempô!')
print('As regras são simples, basta escolher "Pedra", "Papel" ou "Tesoura" quando eu disser "Jokempô!".')

escolhaj = str(input('Insira sua escolha: ')).lower().strip()

print('Jo...')
sleep(1)
print('Kem...')
sleep(1)
print('PÔ!')
sleep(0.5)

if escolhac == escolhaj:
    print('Opa! Também escolhi {}... Parece que empatamos!'.format(escolhac))

elif escolhac == tesoura and escolhaj == papel:
    print('Ganhei! {} corta {}!'.format(escolhac, escolhaj))

elif escolhac == papel and escolhaj == pedra:
    print('Ganhei! {} vence {}!'.format(escolhac, escolhaj))

elif escolhac == pedra and escolhaj == tesoura:
    print('Ganhei! {} quebra {}!'.format(escolhac, escolhaj))

elif escolhac == tesoura and escolhaj == pedra:
    print('Droga! Eu havia escolhido {}... Parece que você ganhou!'.format(escolhac))

elif escolhac == pedra and escolhaj == papel:
    print('Droga! Eu havia escolhido {}... Parece que você ganhou!'.format(escolhac))

elif escolhac == papel and escolhaj == tesoura:
    print('Droga! Eu havia escolhido {}... Parece que você ganhou!'.format(escolhac))

elif papel != escolhaj != tesoura != escolhaj != pedra:
    print('Opa! Essa não era uma das opções.... Melhor reiniciar e tentar novamente!')
