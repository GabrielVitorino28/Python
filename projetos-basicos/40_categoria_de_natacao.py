# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - De 10 até 14 anos: INFANTIL
# - De 15 até 19 anos: JÚNIOR
# - De 20 até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

cores = {'vermelhosub': '\033[4;31m',
         'lilasneg': '\033[1;35m',
         'verdeneg': '\033[1;32m',
         'amareloneg': '\033[1;33m',
         'azulneg': '\033[1;34m',
         'cianoneg': '\033[1;36m',
         'limpa': '\033[m'}

an = int(input('Em que ano você nasceu? '))

ac = date.today().year
id = ac - an

if ac < an:
    print('{}Ano de nascimento inválido. Atualmente estamos no ano de {}. Reinicie o programa e tente novamente.{}'
          .format(cores['vermelhosub'], ac, cores['limpa']))

elif id <= 9:
    print('Você tem {}{}{} anos de idade, logo se encontra na categoria {}MIRIM{}.'
          .format(cores['lilasneg'], id, cores['limpa'], cores['lilasneg'], cores['limpa']))

elif 9 < id <= 14:
    print('Você tem {}{}{} anos de idade, logo se encontra na categoria {}INFANTIL{}.'
          .format(cores['amareloneg'], id, cores['limpa'], cores['amareloneg'], cores['limpa']))

elif 14 < id <= 19:
    print('Você tem {}{}{} anos de idade, logo se encontra na categoria {}JÚNIOR{}.'
          .format(cores['verdeneg'], id, cores['limpa'], cores['verdeneg'], cores['limpa']))

elif 19 < id <= 25:
    print('Você tem {}{}{} anos de idade, logo se encontra na categoria {}SÊNIOR{}.'
          .format(cores['azulneg'], id, cores['limpa'], cores['azulneg'], cores['limpa']))

elif id > 25:
    print('Como você já está acima dos 20 anos, com {}{}{} anos, você se encontra na categoria {}MASTER{}.'
          .format(cores['cianoneg'], id, cores['limpa'], cores['cianoneg'], cores['limpa']))
