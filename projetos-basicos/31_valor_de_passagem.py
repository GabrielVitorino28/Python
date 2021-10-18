# Programa que pergunta a distância de uma viagem em Km e calcula o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

import math

print('='*45)
print('Valor da passagem, arredondando para cima:')
print('Abaixo ou igual a 200km: R$0,50/Km.')
print('Acima de 200Km: R$0.45/Km.')
print('='*45)
dv = float(input('Qual a distância (em Km) da sua viagem? '))

div = math.ceil(dv)

if div <= 200:
    pp = div * 0.5
    print('Considerando R$0,50 o preço por Km, o preço da sua passagem será de R${:.2f}'.format(pp))

else:
    pp = div * 0.45
    print('Considerando R$0,45 o preço por Km, o preço da sua passagem será de R${:.2f}'.format(pp))