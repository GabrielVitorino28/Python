# Programa que lê o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

so = float(input('Qual é o seu salário? R$'))

a = so * 0.15
sa = so + a

print('Com o aumento de 15%(R${:.2f}), seu novo salário é de R${:.2f}!'.format(a, sa))

