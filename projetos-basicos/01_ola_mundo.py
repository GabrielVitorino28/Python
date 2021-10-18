# Programa que escreve "Olá, Mundo!" na tela.

cores = {'azulnegrito': '\033[1;34m',
         'limpa': '\033[m'}

print('{}Olá, Mundo!{}'.format(cores['azulnegrito'], cores['limpa']))
