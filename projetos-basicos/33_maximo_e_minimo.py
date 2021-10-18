# Programa que lê 3 números e mostra qual é o maior e qual é o menor.

n1 = int(input('Insira o primeiro número inteiro: '))
n2 = int(input('Insira o segundo número inteiro: '))
n3 = int(input('Insira o terceiro número inteiro: '))

menor = 0
maior = 0

numeros = [n1, n2, n3]
for c in range(1, len(numeros) + 1):
    if menor == 0 and maior == 0:
        menor = numeros[c - 1]
        maior = numeros[c - 1]
    elif numeros[c - 1] > maior:
        maior = numeros[c - 1]
    elif numeros[c - 1] < menor:
        menor = numeros[c - 1]

print('O menor número inserido foi: {}'.format(menor))
print('O maior número inserido foi: {}'.format(maior))