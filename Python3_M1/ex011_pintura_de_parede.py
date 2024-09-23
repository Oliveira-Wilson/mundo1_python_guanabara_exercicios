# Entrada do usuário
largura = float(input('Qual a largura da parede em metros? '))
altura = float(input('Qual a altura da parede em metros? '))

# Cálculo da área da parede
area_parede = largura * altura

# Cálculo da quantidade de tinta necessária (assumindo que 1 litro cobre 2 m²)
quantidade_tinta = area_parede / 2

# Impressão dos resultados

print(f'Sua parede tem a dimenção de {largura}x{altura} e sua aréa é de {area_parede:2}m².\nPara pintar essa parede, você vai precisar de {quantidade_tinta}L de tinta ')
