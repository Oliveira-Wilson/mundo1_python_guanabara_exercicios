from datetime import date
atual = date.today().year
nasc = int (input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu no ano de {nasc}, tem anos em {idade} anos {atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento sera em {ano}')

elif idade > 18:
    saldo = idade - 18
    print(f'Voce ja deveria ter se alistado há {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}.')
   