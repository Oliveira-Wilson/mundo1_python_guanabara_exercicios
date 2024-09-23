km = int(input('Quanto a distancia  você vai viajar? '))
if  km <=200:
    preço = km * 0.50
else:
    preço = km * 0.45
print(f'O Preço  da sua passagem é: R${preço:.2f}')
