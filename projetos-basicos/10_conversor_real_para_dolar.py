# Programa que lê quantos Reais uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar.
# (Considere US$1.00 = R$5.52).

dr = float(input('Quantos Reais você possui na carteira? R$'))

dd = dr / 5.52

print('Você pode comprar um total de US${:.2f}!'.format(dd))