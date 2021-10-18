# Programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Depois, calcula o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

qkm = float(input('Quantos Km o carro percorreu? '))
qd = int(input('Por quantos dias o carro foi alugado? '))

pkm = qkm * 0.15
pd = qd * 60
pt = pkm + pd

print('O valor total a ser pago é de R${:.2f}'.format(pt))