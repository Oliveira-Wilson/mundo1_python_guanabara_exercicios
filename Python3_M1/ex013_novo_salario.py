# Entrada do usuário
salario = float(input('Digite o seu salário: '))

# Cálculo do aumento (15%)
aumento = salario * 15 / 100

# Cálculo do novo salário
novo_salario = salario + aumento

# Impressão do novo salário com formatação
print(f'Parabéns!! O seu novo salário com aumento de 15% é: {novo_salario:.2f} R$')
