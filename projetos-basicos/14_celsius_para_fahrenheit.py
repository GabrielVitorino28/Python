# Programa que lê uma temperatura digitada em °C e converte-a para °F.

tc = float(input('Insira a temperatura em °C: °'))

tf = (tc * 9 / 5) + 32

print('A temperatura de {}°C corresponde a {}°F!'.format(tc, tf))