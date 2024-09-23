nota1 = float(input('Digite a sua nota '))
nota2 = float(input('Digite a sua nota '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'A media de sua nota foi {media:.1f}:PARABÉNS! APROVADO.')
elif media < 5:
    print(f'A media de suas notas foi {media:.1f}:REPROVADO, estude mais ')
else:
    print(f'A media de sua nota foi {media:.1f}: Voce ficou de RECUPERAÇÂO')