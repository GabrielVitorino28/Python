# Programa que irá aprovar ou negar o empréstimo bancário para a compra de uma casa, com base nos requisitos:
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar, e então calcular o valor da prestação mensal. A prestação mensal não pode exceder 30% do salário, e o empréstimo será negado se ela ultrapassar esse valor.

cores = {'vermelhosub': '\033[4;31m',
         'verdesub': '\033[4;32m',
         'azulneg': '\033[1;34m',
         'azulsub': '\033[4;34m',
         'limpa': '\033[m'}

print('{}Para que o empréstimo seja possível, o valor da prestação mensal não pode exceder 30% do seu salário.{}'
      .format(cores['azulsub'], cores['limpa']))

vc = float(input('Qual o valor da casa que pretende comprar? R$'))
s = float(input('Qual o seu salário? R$'))
pa = int(input('Em quantos anos pretende pagar a casa? '))

ls = s * 0.3
pm = pa * 12
vpm = vc / pm
pps = (vpm / s) * 100

print('O valor da prestação mensal será de {}R${:.2f}{}, durante {}{}{} meses.'
      .format(cores['azulneg'], vpm, cores['limpa'],
              cores['azulneg'], pm, cores['limpa']))

if vpm > ls or pps > 30:
    print('{}Infelizmente o valor da prestação representa {:.2f}% do seu salário, então seu empréstimo foi recusado.{}'
          .format(cores['vermelhosub'], (pps), cores['limpa']))
elif vpm <= ls or pps <= 30:
    print('{}Boas notícias! Como o valor da prestação representa apenas {:.2f}% do seu salário, seu empréstimo foi aprovado!{}'
          .format(cores['verdesub'], (pps), cores['limpa']))