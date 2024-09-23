numero = int(input('Digite um número qualquer: '))
resultado = numero % 2 # % resto da divisão 

if resultado == 0:
    print(f'O número {numero} é, PAR. ')
else:
    print(f'O numero {numero} é, IPAR. ')