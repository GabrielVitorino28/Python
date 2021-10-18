# Programa que lê uma frase pelo teclado e mostra:
# * Quantas vezes aparece a letra "A"
# * Em que posição ela aparece pela primeira vez
# * Em que posição ela aparece pela última vez

frase = str(input('Digite uma frase: ')).lower().strip()

print('A letra "A" aparece {} vez(es) na frase.'.format(frase.count('a')))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('a') + 1))
print('A letra "A" aparece pela última vez na posição {}.'.format(frase.rfind('a') + 1))
