# Programa que lê o ano de nascimento de 7 pessoas e no final, mostra quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
aa = date.today().year
nma = 0
nme = 0

for c in range(1, 8):
    an = int(input('Insira ano de nascimento da {}° pessoa: '.format(c)))
    if aa - an >= 18:
        nma += 1
        print('Essa pessoa é maior de idade.')

    else:
        nme += 1
        print('Essa pessoa é menor de idade.')

if nme == 1:
    print('Das 7 pessoas, {} são maiores de idade e {} é menor.'.format(nma, nme))

elif nma == 1:
    print('Das 7 pessoas, {} é maior de idade e {} são menores.'.format(nma, nme))

elif nme == 0:
    print('Das 7 pessoas, {} são maiores de idade e nenhuma é menor.'.format(nma))

elif nma == 0:
    print('Das 7 pessoas, nenhuma é maior de idade e {} são menores.'.format(nme))

else:
    print('Das 7 pessoas, {} são maiores de idade e {} são menores.'.format(nma, nme))