# Programa que lê vários números inteiros pelo teclado, parando apenas quando o usuário digitar o valor 999, que é a condição de parada. No final, o programa exibe quantos números foram digitados e qual foi a soma entre eles (desconsiderando o valor de parada).

s = 0
qn = 0
n = 0

while n != 999:
    n = int(input('Agora, insira o próximo número inteiro (Para parar de adicionar números, insira o valor 999): '))
    if n == 999:
        break
    s += n
    qn += 1

if qn > 1:
    print('\nNo total foram inseridos {} números inteiros e a soma deles foi igual a {}'.format(qn, s))
elif qn == 1:
    print('\nNo total, apenas um número inteiro foi inserido, logo o resultado final da soma é {}'.format(qn, s))
elif qn == 0:
    print('\nNenhum número inteiro foi inserido, logo o resultado final da soma é 0.')