# Programa que lê o preço de um produto e mostra o seu novo preço, com 5% de desconto.

po = float(input('Insira o preço do produto: R$'))

d = po / 20
pd = po - d

print('Com o desconto de 5%(R${:.2f}), o novo preço é de R${:.2f}!'.format(d, pd))