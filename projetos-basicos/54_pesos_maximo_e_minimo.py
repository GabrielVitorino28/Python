# Programa que lê o peso de 5 pessoas e mostra quais foram o maior e o menor pesos lidos.

map = 0
mep = 0

for c in range(1, 6):
    p = float(input('Insira o peso da {}° pessoa: '.format(c)))
    if map == 0 and mep == 0:
        map = p
        mep = p
    elif p > map:
        map = p
    elif p < mep:
        mep = p

print('O maior peso lido foi de {:.2f}Kg e o menor foi de {:.2f}Kg.'.format(map, mep))
