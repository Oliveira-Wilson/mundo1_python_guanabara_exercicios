dias = int(input('quantos dias voce ficou com o carro?'))
km = float(input('digite quantos km voce percorreu.'))
pago = (dias * 60) + (km * 0.15)

print(f'voce ficou {dias} dias  com o carro, e percorreu {km}KM, portanto voce pagara {pago:.2f}R$')
