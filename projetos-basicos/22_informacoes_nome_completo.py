# Programa que lê o nome completo de uma pessoa e mostra:
# * O nome com todas as letras maiúsculas
# * O nome com todas as letras minúsculas
# * Quantas letras ao todo (sem espaços)
# * Quantas letras tem o primeiro nome

nc = str(input('Insira o seu nome completo: ')).strip()

print('Com todas as letras maiúsculas seu nome ficaria:')
print(nc.upper())

print('Com todas as letras minúsculas seu nome ficaria:')
print(nc.lower())

print('No total seu nome possui {} letras.'.format(len(nc) - nc.count(' ')))

ncd = nc.split()
print('Seu primeiro nome é {} e ele possui {} letras.'.format(ncd[0], len(ncd[0])))