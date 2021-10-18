# Programa que lê dois números e mostra a soma entre eles.

cores = {'azulsublinhado': '\033[4;34m',
         'amarelosublinhado': '\033[4;33m',
         'verdesublinhado': '\033[4;32m',
         'limpa': '\033[m'}

n1 = int(input('Digite o {}Primeiro Número{} da soma: '.format(cores['azulsublinhado'], cores['limpa'])))
n2 = int(input('Digite o {}Segundo Número{} da soma: '.format(cores['amarelosublinhado'], cores['limpa'])))
s = n1 + n2

print('O resultado da soma entre {}{}{} e {}{}{} é igual a {}{}{}!'
      .format(cores['azulsublinhado'], n1, cores['limpa'],
              cores['amarelosublinhado'], n2, cores['limpa'],
              cores['verdesublinhado'], s, cores['limpa']))
