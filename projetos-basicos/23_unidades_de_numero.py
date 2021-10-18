# Programa que lê um número de 0 a 9999 e mostra na tela cada um dos dígitos separados.
# Ex: 1834
# Unidade:4 / Dezena:3 / Centena:8 / Milhar:1

ni = int(input('Informe um número entre 0 e 9999: '))

u = ni // 1 % 10
d = ni // 10 % 10
c = ni // 100 % 10
m = ni // 1000 % 10

print('Analisando o número {}:'.format(ni))
print('Milhar = {}'.format(m))
print('Centena = {}'.format(c))
print('Dezena = {}'.format(d))
print('Unidade = {}'.format(u))
