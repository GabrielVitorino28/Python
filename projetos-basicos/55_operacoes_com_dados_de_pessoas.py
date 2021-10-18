# Programa que lê o nome, a idade e o sexo de 4 pessoas. No final do programa, são exibidos:
# - A média de idade do grupo;
# - O nome do homem mais velho;
# - Quantas mulheres têm menos de 20 anos.

sid = 0
mid = 0
mih = 0
nmv = ''
mm20 = 0
nh = 0


for c in range(1, 5):
    print('========== {}° Pessoa =========='.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    sid += idade
    if sexo in 'Mm':
        nh += 1
        if c == 1 and sexo in 'Mm':
            mih = idade
            nmv = nome
        elif sexo in 'Mm' and idade > mih:
            mih = idade
            nmv = nome
    elif sexo in 'Ff' and idade < 20:
        mm20 += 1

mid = sid / 4
print('A média de idade do grupo é de {} anos.'.format(mid))

if nh > 0:
    print('O homem mais velho é {}, com {} anos.'.format(nmv, mih))
elif nh == 0:
    print('Nenhuma das pessoas cadastradas é homem.')

if mm20 > 1:
    print('No total, {} mullheres têm menos de 20 anos.'.format(mm20))
elif mm20 == 0:
    print('Nenhuma das mulheres cadastradas têm menos de 20 anos.')
elif mm20 == 1:
    print('Apenas 1 mulher cadastrada tem menos de 20 anos.')
