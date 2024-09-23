numero = int(input('Digite um número inteiro- '))
print('''ESCOLHA umas das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3]converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'convertido para BINÁRIO é igual a {numero}')
elif opção == 2:
    print(f'convertido para OCTAL é igual a {numero}')
elif opção == 3:
    print(f'convertido para HEXADECIMAL é igual a {numero}')
else:
    print('Opção INVALIDA. Tente novamente')


22