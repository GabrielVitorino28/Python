# Programa que lê o nome de uma pessoa e diz se ele contém "SILVA".

n = str(input('Qual o seu nome completo: '))
nd = n.lower().split()

print('O seu nome completo contém a palavra "Silva?": ')
print('silva' in nd)
