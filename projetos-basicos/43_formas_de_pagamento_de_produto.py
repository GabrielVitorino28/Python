# Programa que calcula o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('-=-'*13)
print('Opções de pagamento')
print('1 - Dinheiro - 10% de desconto')
print('2 - Cheque - 10% de desconto')
print('3 - Cartão (à vista) - 5% de desconto')
print('4 - Cartão (2x) - Preço normal')
print('5 - Cartão (3x ou mais) - 20% de juros')
print('-=-'*13)

op = int(input('Insira a opção de pagamento desejada: '))
vi = float(input('Insira o valor do produto: '))

if op == 1 or op == 2:
    d = vi * 0.1
    vf = vi - d
    print('Com o desconto de 10%(R${:.2f}), o preço a pagar será de R${:.2f}!'.format(d, vf))

elif op == 3:
    d = vi * 0.05
    vf = vi - d
    print('Com o desconto de 5%(R${:.2f}), o preço a pagar será de R${:.2f}!'.format(d, vf))

elif op == 4:
    print('Como não haverá desconto, o valor a ser pago é o valor original de R${:.2f}!'.format(vi))

elif op == 5:
    jp = vi * 0.2
    vf = vi + jp
    print('Com os juros de 20%(R${:.2f}), o valor final a ser pago é de R${:.2f}'.format(jp, vf))

elif op < 1 or op > 5:
    print('Esse número não se encaixa em nenhuma das opções. Reinicie o programa e tente novamente.')