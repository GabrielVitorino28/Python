# Programa que lê duas notas de um aluno e calcula sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

cores = {'vermelhosub': '\033[4;31m',
         'amarelosub': '\033[4;33m',
         'azulsub': '\033[4;34m',
         'limpa': '\033[m'}

print('{}- Média abaixo de 5.0: Reprovado{}'.format(cores['vermelhosub'], cores['limpa']))
print('{}- Média entre 5.0 e 6.9: Recuperação{}'.format(cores['amarelosub'], cores['limpa']))
print('{}- Média 7.0 ou superior: Aprovado{}'.format(cores['azulsub'], cores['limpa']))
n1 = float(input('Qual foi a sua primeira nota? '))
n2 = float(input('Qual foi a sua segunda nota? '))

m = (n1 + n2) / 2
if m < 5.0:
    print('{}Sua média foi de {}, infelizmente você foi REPROVADO.{}'
          .format(cores['vermelhosub'], m, cores['limpa']))

elif 5.0 <= m < 7.0:
    print('{}Sua média foi de {}, você ficará de RECUPERAÇÃO.{}'
          .format(cores['amarelosub'], m, cores['limpa']))

elif m >= 7.0:
    print('{}Sua média foi de {}. Parabéns!! Você foi aprovado!{}'
          .format(cores['azulsub'], m, cores['limpa']))
