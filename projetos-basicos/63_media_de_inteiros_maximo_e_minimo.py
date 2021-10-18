# Programa que lê vários números inteiros pelo teclado, parando apenas sob o comando do usuário. No final da execução, ele exibe a média entre todos os valores e quais foram o maior e o menor valores lidos.

qdm = 'S'
nv = 0
sv = 0
mav = 0
mev = 0

while qdm == 'S':
    v = int(input('Insira um número inteiro: '))
    sv += v
    nv += 1
    if mav == 0 and mev == 0:
        mav = v
        mev = v
    elif v > mav:
        mav = v
    elif v < mev:
        mev = v
    qdm = str(input('Gostaria de inserir mais um valor? (S/N) ')).upper().strip()
    while qdm not in 'SN':
        qdm = str(input('O texto inserido é inválido, tente responder usando apenas S para Sim ou N para Não.'
                        '\nGostaria de inserir mais um valor? (S/N) ')).upper().strip()

medv = sv / nv

print('No total foram inseridos {} valores, e a média entre todos eles foi de {:.2f}.'.format(nv, medv))
print('O maior valor inserido foi {} e o menor foi {}.'.format(mav, mev))
