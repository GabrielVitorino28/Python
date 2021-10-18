# Evolução do Projeto 50 (Progressão Aritmética), onde a estrutura For foi substituída pela estrutura While, e o programa pergunta ao usuário quantos termos ele gostaria de ver.

from time import sleep

pt = int(input('Insira o primeiro termo da progressão aritmética: '))
r = int(input('Agora, insira a razão da progressão aritmética: '))
t = int(input('Quantos termos você gostaria de visualizar? '))
pa = pt
f = 1

while f <= t:
    pa = pt + (r * (f - 1))
    print('O {}° termo da progressão aritmética é {}.'.format(f, pa))
    sleep(0.5)
    f += 1

fo = f

fad = int(input('Quantos termos a mais você gostaria de ver? Caso não queira ver mais nenhum, digite 0: '))

while fad != 0:
    while f <= (fo + fad):
        pa = pt + (r * (f - 1))
        print('O {}° termo da progressão aritmética é {}.'.format(f, pa))
        sleep(0.5)
        f += 1
    fo = f
    fad = int(input('Quantos termos a mais você gostaria de ver? Caso não queira ver mais nenhum, digite 0: '))

print('\nEncerrando o programa.')
sleep(1)