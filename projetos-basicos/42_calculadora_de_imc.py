# Calculadora de IMC, de acordo com os dados abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print('-=-'*6)
print('Calculadora de IMC')
print('-=-'*6)

p = float(input('Insira seu peso em Kg: '))
a = float(input('Insira sua altura em M: '))

imc = p / (a**2)

if imc < 18.5:
    print('Seu IMC é igual a {:.2f}, logo você está ABAIXO DO PESO.'.format(imc))

elif 18.5 <= imc < 25:
    print('Seu IMC é igual a {:.2f}, logo você está no PESO IDEAL.'.format(imc))

elif 25 <= imc < 30:
    print('Seu IMC é igual a {:.2f}, logo você está ACIMA DO PESO.'.format(imc))

elif 30 <= imc < 40:
    print('Seu IMC é igual a {:.2f}. Você está no nível de OBESIDADE.'.format(imc))

elif imc >= 40:
    print('Seu IMC é igual a {:.2f}. Cuidado! Você está no nível de OBESIDADE MÓRBIDA.'.format(imc))