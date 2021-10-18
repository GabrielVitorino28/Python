# Programa que lê uma frase qualquer e diz se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Insira uma frase (Usando apenas números ou letras sem acentuação): ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#inverso = ''

print('Você digitou a frase {}'.format(junto))

#for c in range(len(junto) -1, -1, -1):
#   inverso += junto[c]

if inverso == junto:
    print('O inverso de {} é {}.'.format(junto, inverso))
    print('A frase {} é um palíndromo.'.format(junto))

else:
    print('O inverso de {} é {}.'.format(junto, inverso))
    print('A frase {} não é um palíndromo.'.format(junto))
