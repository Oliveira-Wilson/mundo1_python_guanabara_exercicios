salario = float(input('Digite seu salario R$ '))
if salario <= 1250.00:
    novo = salario + (salario * 15 / 100) 
else:
    novo = salario + (salario * 10 / 100) 
print(f'Seu novo salario é: R${novo:.2f}')
    