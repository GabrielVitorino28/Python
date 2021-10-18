# Programa que lê um número e mostra o seu fatorial.
# Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120.

fat = 1
cont = 1
numfat = int(input('Insira um número inteiro para ver seu fatorial: '))

while cont < numfat:
    cont += 1
    fat *= cont

print('O fatorial do número inserido ({}!) é igual a {}.'.format(numfat, fat))