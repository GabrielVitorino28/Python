# Programa que lê um valor em metros e o exibe convertido em outras medidas.

nm = float(input('Insira um valor em metros: '))

nkm = nm / 1000
nhm = nm / 100
ndam = nm / 10
ndm = nm * 10
ncm = nm * 100
nmm = nm * 1000

print('{}m é igual a {}km!'.format(nm, nkm))
print('{}m é igual a {}hm!'.format(nm, nhm))
print('{}m é igual a {}dam!'.format(nm, ndam))
print('{}m é igual a {}dm!'.format(nm, ndm))
print('{}m é igual a {}cm!'.format(nm, ncm))
print('{}m é igual a {}mm!'.format(nm, nmm))