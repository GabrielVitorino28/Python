# Programa que lê o nome de uma pessoa e mostra uma mensagem de boas-vindas.

cores = {'sublinhado': '\033[4m',
         'verdenegrito': '\033[1;32m',
         'limpa': '\033[m'}

nome = input('{}Digite seu nome:{} '.format(cores['sublinhado'], cores['limpa']))

print('É um prazer te conhecer, {}{}{}!'.format(cores['verdenegrito'], nome, cores['limpa']))
