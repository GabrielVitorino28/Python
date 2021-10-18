# Programa que lê um número inteiro e diz se ele é ou não um número primo.

cores = {'verdenegrito': '\033[1;32m',
         'vermelhornegrito': '\033[1:31m',
         'limpa': '\033[m'}

n = int(input('Insira um número inteiro: '))
nd = 0

for c in range(1, n + 1):
    if n % c == 0:
        nd += 1
        print('{}{}{}'.format(cores['verdenegrito'], c, cores['limpa']), end=', ')

    elif n % c != 0:
        print('{}{}{}'.format(cores['vermelhornegrito'], c, cores['limpa']), end=', ')

if nd == 2:
    print('\nO número {} só é divisível 2 vezes, por 1 e por {}, logo ele é primo.'.format(n, n))

elif 1 != nd != 2:
    print('\nO número {} foi divisível por {} números, logo ele não é primo'.format(n, nd))

elif n == 1:
    print('\nO número 1 só é divisível por ele mesmo, logo ele é primo')
