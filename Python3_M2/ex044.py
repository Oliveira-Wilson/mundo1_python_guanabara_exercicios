preço = float(input('PREÇO DAS COMPRAS: R$'))

print('''[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opção = int(input('Qual a opção? '))

if opção == 1:
    total = preço - (preço * 10 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}.')
    print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
elif opção == 4:
    total = preço + (preço * 20 / 100)  # Considerando 20% de juros
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R${parcela:.2f} com juros.')
    print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
else:
    print('Opção inválida, TENTE NOVAMENTE!')
