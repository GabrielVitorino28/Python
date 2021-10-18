# Programa que lê um valor pelo teclado e mostra na tela todas as informaçôes possíveis sobre ele.

cores = {'verdesublinhado': '\033[4;32m',
         'vermelhosublinhado': '\033[4;31m',
         'limpa': '\033[m'}

x = input('Digite algo: ')

print('O tipo primitivo desse valor é:', type(x))
print('-=-' * 11)
print('// {}True = Sim{} // {}False = Não{} //'
      .format(cores['verdesublinhado'], cores['limpa'], cores['vermelhosublinhado'], cores['limpa']))
print('-=-' * 11)
print('Só tem espaços? {}.'.format(x.isspace()))
print('É um número? {}.'.format(x.isnumeric()))
print('É alfabético? {}.'.format(x.isalpha()))
print('É alfanumérico? {}.'.format(x.isalnum()))
print('Está em maiúsculas? {}.'.format(x.isupper()))
print('Está em minúsculas? {}.'.format(x.islower()))
print('Está capitalizada? {}.'.format(x.istitle()))