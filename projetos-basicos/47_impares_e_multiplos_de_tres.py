# Programa que calcula a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.

s = 0
nim3 = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        nim3 += 1

print('\nA soma total dos {} números ímpares e múltiplos de 3 entre 1 e 500 foi igual a {}'.format(nim3, s))