# Programa que lê a largura e a altura de uma parede em metros, calcula a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Qual a largura da parede (em metros)? '))
altura = float(input('Qual a altura da parede (em metros)? '))

areaparede = largura * altura
nlatas = areaparede / 2

print('Com uma dimensão de {}m X {}m, a área da parede é de {}m²,\ncomo cada lata de tinta cobre 2m²,\n'
      'você irá precisar de {} latas de tinta.'.format(largura, altura, areaparede, nlatas))