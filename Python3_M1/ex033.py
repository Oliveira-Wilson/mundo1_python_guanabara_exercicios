a = int(input('Digite um numero '))
b = int(input('Digite um numero '))
c = int(input('Digite um numero '))
# verificar quem é Menor.
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# verificar quem é Maior.
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O menor valor digitado foi {menor}.')
print(f'O maior valor digitado foi {maior}.')