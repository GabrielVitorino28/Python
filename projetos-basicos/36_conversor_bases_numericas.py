# Programa que lê um número inteiro qualquer e pergunta ao usuário qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

n = int(input('Insira um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] - Converter para BINÁRIO
[ 2 ] - Converter para OCTAL
[ 3 ] - Converter para HEXADECIMAL''')

e = int(input('Sua escolha de base: '))

if e == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))

elif e == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))

elif e == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))

elif e < 1 or e > 3:
    print('{} não era uma das opções válidas. Reinicie o programa e tente novamente.'.format(e))
