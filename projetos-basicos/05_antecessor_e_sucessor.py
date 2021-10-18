# Programa que lê um número inteiro e mostra na tela seu sucessor e seu antecessor.

cores = {'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'limpa': '\033[m'}

n = int(input('Insira um número inteiro: '))

an = n - 1
sn = n + 1

print('O {}antecessor{} de {}{}{} é {}{}{}!'
      .format(cores['vermelho'], cores['limpa'],
              cores['azul'], n, cores['limpa'],
              cores['vermelho'], an, cores['limpa']))

print('O {}sucessor{} de {}{}{} é {}{}{}!'.
      format(cores['amarelo'], cores['limpa'],
             cores['azul'], n, cores['limpa'],
             cores['amarelo'], sn, cores['limpa']))