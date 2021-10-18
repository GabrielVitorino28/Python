# Programa que simula o funcionamento de um caixa eletrônico na função saque, lendo um número inteiro em Reais e informando quantas cédulas de cada valor serão entregues, considerando que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

notascinquenta = 0
notasvinte = 0
notasdez = 0
notasum = 0
valororiginal = 0

print('=' * 20)
print('      Banco GV')
print('=' * 20)

valor = int(input('Insira o valor que deseja sacar: R$'))
valororiginal = valor

while valor >= 50:
    valor -= 50
    notascinquenta += 1

while valor >= 20:
    valor -= 20
    notasvinte += 1

while valor >= 10:
    valor -= 10
    notasdez += 1

while valor >= 1:
    valor -= 1
    notasum += 1

print(f'O valor de R${valororiginal} será sacado em:')
if notascinquenta > 0:
    print(f'{notascinquenta} nota(s) de R$50.00')
if notasvinte > 0:
    print(f'{notasvinte} nota(s) de R$20.00')
if notasdez > 0:
    print(f'{notasdez} nota(s) de R$10.00')
if notasum > 0:
    print(f'{notasum} nota(s) de R$1.00')
