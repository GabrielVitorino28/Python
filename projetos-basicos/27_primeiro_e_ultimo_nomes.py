# Programa que lê o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# Primeiro Nome: Ana
# Último Nome: Souza

nc = str(input('Qual o seu nome completo: '))

ncd = nc.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}!'.format(ncd[0]))
print('Seu segundo nome é {}!'.format(ncd[len(ncd) - 1]))
