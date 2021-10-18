# Programa que lê um número e mostra o seu dobro, triplo e raíz quadrada.

cores = {'lilassub': '\033[4;35m',
         'verdesub': '\033[4;32m',
         'cianosub': '\033[4;36m',
         'azulsub': '\033[4;34m',
         'limpa': '\033[m'}

n = int(input('Insira um número: '))

dn = n * 2
tn = n * 3
rqn = n ** (1/2)

print('O dobro de {}{}{} é {}{}{}!'
      .format(cores['azulsub'], n, cores['limpa'],
              cores['lilassub'], dn, cores['limpa']))

print('O triplo de {}{}{} é {}{}{}!'
      .format(cores['azulsub'], n, cores['limpa'],
              cores['verdesub'], tn, cores['limpa']))

print('A raíz quadrada de {}{}{} é {}{:.2f}{}!'
      .format(cores['azulsub'], n, cores['limpa'],
              cores['cianosub'], rqn, cores['limpa']))