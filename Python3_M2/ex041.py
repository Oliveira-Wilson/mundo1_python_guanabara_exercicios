from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento. '))
idade = atual - nasc
print(f'sua idade é {idade}')

if idade <=9:
    print(f'Você tem {idade} anos então sua categoria é MIRIM!')

elif idade > 9 and idade <= 14:
     print(f'Você tem {idade} anos então sua categoria é INFANTIL')
elif idade <= 19:
    print(f'Você tem {idade} anos então sua categoria é JUNIOR !')
elif idade <= 25:
    print(f'Você tem {idade} anos então sua categoria é SÊNIOR !')
elif idade > 25:
    print(f'Você tem {idade} anos então sua categoria é MASTER !')

    
