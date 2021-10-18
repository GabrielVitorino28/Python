# Programa que lê um número inteiro e informa se ele é par ou ímpar.

nint = int(input("Insira um número inteiro para saber se ele é par ou ímpar: "))

if nint % 2 == 0:
    print("O número {} é par.".format(nint))
else:
    print("O número {} é ímpar.".format(nint))