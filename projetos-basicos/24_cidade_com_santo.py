# Programa que lê o nome de uma cidade e diz se ele começa ou não com o nome "SANTO".

cidade = str(input('Insira o nome de uma cidade: ')).strip()

print('O nome dessa cidade começa com "Santo"?')
print(cidade[:6].lower() == 'santo ')