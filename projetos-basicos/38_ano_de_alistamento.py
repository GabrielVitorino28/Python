# Programa que lê o ano de nascimento de um jovem e informa, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# O programa também informa o tempo que falta ou que passou do prazo

from datetime import date

ano = int(input('Insira o seu ano de nascimento: '))

anoatual = date.today().year
idade = anoatual - ano
excesso = idade - 18

if excesso == 0:
    print('Já está na hora de você se alistar!')

elif excesso > 0:
    print('Já fazem {} anos que você precisa se alistar!'.format(excesso))

elif excesso < 0:
    print('Ainda faltam {} anos para você se alistar!'.format(excesso * -1))
