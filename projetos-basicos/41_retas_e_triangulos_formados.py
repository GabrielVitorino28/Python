# Programa que lê a medida de 3 retas e diz se elas podem formar um triângulo. Caso possam, também será informado o tipo de triângulo formado.

cores = {'cianosub': '\033[4;36m',
         'vermelhosub': '\033[4;31m',
         'azulsub': '\033[4;34m',
         'amarelosub': '\033[4;33m',
         'verdesub': '\033[4;32m',
         'limpa': '\033[m'}

l1 = float(input('Insira o comprimento da primeira reta: '))
l2 = float(input('Insira o comprimento da segunda reta: '))
l3 = float(input('Insira o comprimento da terceira reta: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('{}Essas 3 retas podem formar um triângulo!{}'.format(cores['cianosub'], cores['limpa']))
    if l1 == l2 == l3:
        print('Elas formarão um triângulo {}EQUILÁTERO{}.'.format(cores['azulsub'], cores['limpa']))

    elif l1 != l2 != l3 != l1:
        print('Elas formarão um triângulo {}ESCALENO{}.'.format(cores['amarelosub'], cores['limpa']))

    elif l3 != l1 == l2 != l3 or l2 != l1 == l3 != l2 or l1 != l2 == l3 != l1:
        print('Elas formarão um triângulo {}ISÓCELES.'.format(cores['verdesub'], cores['limpa']))

else:
    print('{}Essas 3 retas não podem formar um triângulo!{}'.format(cores['vermelhosub'], cores['limpa']))