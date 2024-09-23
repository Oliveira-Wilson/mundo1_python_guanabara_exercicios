frase = str(input('Digite uma frase: ')).strip().upper()  # .strip() para remover espaços extras
# Convertendo a frase para minúsculas e contando a letra 'a'

print(f'Quantas vezes aparece a letra A: {frase.count('A')}')
print(f'Em que posição ela aparece a primeira vez.{frase.find('A')+1 } ')
print(f'Em que posição ela aparece pela ultima vez.{frase.rfind('A') +1 } ')
# esse +1 é para sair contando 'da posiçao 1 e não da posição 0'