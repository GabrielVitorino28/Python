# Programa que lê o sexo de uma pessoa, mas só aceita M ou F. Caso a digitação esteja incorreta, o programa irá solicitar que seja digitado o sexo novamente até receber um valor válido.

sexo = str(input('Qual o seu sexo?\nInsira M para Masculino ou F para Feminino: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('\nO texto inserido não é válido para a identifcação de gênero. Por favor, tente novamente.\n'
                     'Qual é o seu sexo?\nInsira M para Masculino ou F para Feminino: ')).strip().upper()[0]
if sexo == 'M':
    print('\nSexo Masculino registrado com sucesso!')
elif sexo == 'F':
    print('\nSexo Feminino registrado com sucesso!')
