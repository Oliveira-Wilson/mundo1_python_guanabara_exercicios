nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome é {nome}')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

# Extrai o primeiro nome
split = nome.split()[0]

print(f'Seu primeiro nome é {split} e tem ao todo {len(split)} letras')
