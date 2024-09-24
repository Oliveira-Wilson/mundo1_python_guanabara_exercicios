peso    =float(input('Qual a seu peso  (KG) '))
altura = float(input('Qual a sua altura? (M) '))
imc = peso / (altura ** 2)
print(f'O seu IMC é {imc:.1f}  ')

if imc < 18.5:
    print(f'Você esta Abaixo do peso. ')

elif imc >= 18.5 and imc <= 25:

    print(f'Você esta no Peso ideal')
elif imc >= 25 and imc < 30:

    print(f'Você esta com Sobreepeso ')
elif imc >= 30 and imc < 40:

    print(f'com Você esta Obesidade')

elif imc >= 40:
    print('Você esta OBESIDADE MÓRBIDA')
    