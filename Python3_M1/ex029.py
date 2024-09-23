velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade  >=80.001:
    multa = 7.00 * (velocidade - 80)
    print('MULTADO! Você excedeu o limite maximo permiyido que é de 80KM/h: ')
    print(f'Você deve pagar o valor da multa de {multa:.2f}R$. ')
print('Tenha um bom dia e dirija com segurança')
