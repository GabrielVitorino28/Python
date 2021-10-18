# Programa que lê dois valores e dá ao usuário as seguintes opções:
# [1] Somar
# [2] Subtrair
# [3] Multiplicar
# [4] Dividir
# [5] Maior
# [6] Novos Números
# [7] Sair do Programa

from time import sleep

op = 0
n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))

while op != 7:
    op = int(input('\nEscolha uma opção entre 1 e 5 para prosseguir:'
                   '\n[1] Somar os dois valores'
                   '\n[2] Subtrair os dois valores'
                   '\n[3] Multiplicar os dois valores'
                   '\n[4] Dividir os dois valores'
                   '\n[5] Dizer qual dos valores é o maior'
                   '\n[6] Escolher novos valores para trabalhar'
                   '\n[7] Sair do programa'
                   '\nOpção escolhida: '))
    if op > 7 or op < 1:
        print('\n////// Essa não é uma opção válida. Tente novamente. //////')
    elif op == 1:
        print('\n////// A soma dos valores {:.2f} e {:.2f} é igual a {:.2f}. //////'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('\n////// A subtração dos valores {:.2f} e {:.2f} é igual a {:.2f}. //////'.format(n1, n2, n1 - n2))
    elif op == 3:
        print('\n////// A multiplicação dos valores {:.2f} e {:.2f} é igual a {:.2f}. //////'.format(n1, n2, n1 * n2))
    elif op == 4:
        print('\n////// A divisão dos valores {:.2f} e {:.2f} é igual a {:.2f}. //////'.format(n1, n2, n1 / n2))    
    elif op == 5:
        if n1 > n2:
            print('\n////// O primeiro valor inserido ({:.2f}) é maior do que o segundo valor inserido ({:.2f}). //////'.format(n1, n2))
        elif n2 > n1:
            print('\n////// O segundo valor inserido ({:.2f}) é maior do que o primeiro valor inserido ({:.2f}). //////'.format(n2, n1))
        elif n1 == n2:
            print('\n////// O primeiro valor inserido ({:.2f}) e o segundo valor inserido ({:.2f}) são iguais. //////'.format(n1, n2))
    elif op == 6:
        n1 = float(input('\nInsira o primeiro dos novos valores a serem trabalhados: '))
        n2 = float(input('Insira o segundo dos novos valores a serem trabalhados: '))

print('\nEncerrando o programa...')
sleep(1.5)
