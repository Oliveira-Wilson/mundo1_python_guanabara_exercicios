# Entrada do usuário

preco = float(input('Digite o preço do produto: '))

#calculo do desconto

novo = preco - (preco * 5/ 100) 

# impressão dos resultados

print(f'O produto que custava R${preco}, na promoção com 5% de desconto, vai custar R${novo:.2f}R$.') 