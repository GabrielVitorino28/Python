# Programa que lê o nome e o preço de vários produtos, parando apenas ao comando do usuário. No final, o programa exibirá:
# 1 - Qual o total gasto na compra
# 2 - Quantos produtos custam mais de R$1000
# 3 - Qual é o nome do produto mais barato

from time import sleep

total = 0
produtoscaros = 0
nomemaisbarato = ''
maisbarato = 0

print('=' * 35)
print(' Boas vindas à Loja Super Baratão!')
print('=' * 35)

while True:
    
    print('-' * 30)
    nome = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: R$'))
    print('-' * 30)

    if preco > 1000:
        produtoscaros += 1

    if maisbarato == 0:
        maisbarato = preco
        nomemaisbarato = nome
    elif preco < maisbarato:
        maisbarato = preco
        nomemaisbarato = nome

    total += preco

    while True:
        continuar = str(input('Gostaria de continuar [S/N] ')).strip().upper()
        if continuar[0] == 'S' or continuar[0] == 'N':
            break
        print('O valor inserido não é uma opção válida.')
        print('-' * 30)
    if continuar[0] == 'N':
        break

print('-' * 30)
print(f'O valor total da compra é de R${total:.2f}.')
print(f'Nesta compra, {produtoscaros} produtos custam mais de R$1000.00.')
print(f'O produto mais barato na compra é {nomemaisbarato}, que custa R${maisbarato:.2f}.')
print('-' * 30)
print('Encerrando Programa...')
sleep(1)