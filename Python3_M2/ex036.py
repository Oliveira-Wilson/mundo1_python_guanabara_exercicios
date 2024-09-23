imovel = float(input('Digite o valor do imovél R$'))
salario = float(input('Digite o o seu salário R$ '))
anos = int(input('Digite em quantos anos será o seu finaciamento '))
prestacao = imovel / (anos * 12)
minimo = salario * 30 /100
print(f'Para pagar um casa de R${imovel:.2f} em {anos} a prestação será de R${prestacao:.2f} ')
if prestacao <= minimo:
    print('EMPRESTIMO pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO!')
    