# Programa que pergunta o salário de um funcionário e calcula o valor de seu aumento.
# Para salários superiores a R$1250, o aumento é de 10%
# Para salários inferiores ou iguais, o aumento é de 15%

s = float(input('Qual é o seu salário? R$'))

if s > 1250:
    a = s * 0.1
    sa = s + a
    print('Com o aumento de 10%({:.2f}), seu novo salário é de {:.2f}'.format(a, sa))

else:
    a = s * 0.15
    sa = s + a
    print('Com o aumento de 15%({:.2f}), seu novo salário é de {:.2f}'.format(a, sa))
