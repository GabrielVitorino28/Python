# Programa que lê a velocidade de um carro. Se ele ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado, com o valor da multa sendo R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual a sua velocidade no momento em que passou pelo radar? "))
excesso = velocidade - 80

if velocidade > 80:
    multa = excesso * 7
    print("Você estava {:.2f}Km/h acima do limite de velocidade e foi multado em R${:.2f}".format(excesso, multa))

elif velocidade <= 80:
    print("Você estava dentro do limite de velocidade e não foi multado.")