# Programa que lê a idade e o sexo de várias pessoas, parando apenas ao comando do usuário. No final, o programa exibirá:
# 1 - Quantas pessoas têm mais de 18 anos
# 2 - Quantos homens foram cadastrados
# 3 - Quantas mulheres têm menos de 20 anos

from time import sleep

maiores = 0
homens = 0
mulheresmenores = 0

while True:

    print('-' * 30)
    print('      Cadastro de Pessoas')
    print('-' * 30)

    while True:
        idade = int(input('Insira a idade: '))
        if 0 <= idade <= 150:
            break
        print('A idade inserida não é um número válido.')
        print('-' * 30)

    while True:
        sexo = str(input('Insira o gênero [M/F]: ')).strip().upper()
        if sexo[0] == 'M' or sexo[0] == 'F':
            break
        print('O valor inserido não se encontra nas opções de gênero.')
        print('-' * 30)

    if idade > 18:
        maiores += 1
    if sexo[0] == 'M':
        homens += 1
    if sexo[0] == 'F' and idade < 20:
        mulheresmenores += 1

    while True:
        print('-' * 30)
        continuar = str(input('Gostaria de continuar [S/N]? ')).strip().upper()
        if continuar[0] == 'S' or continuar[0] == 'N':
            break
        print('O valor inserido não é uma opção válida.')
    if continuar[0] == 'N':
        break

print('-' * 30)
print(f'Foram cadastradas {maiores} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulheresmenores} mulheres com menos de 20 anos.')
print('-' * 30)
print('Encerrando Programa...')
sleep(1)