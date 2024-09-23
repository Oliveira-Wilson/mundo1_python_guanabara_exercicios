# Solicita o nome completo do usuário, converte para maiúsculas e remove espaços extras
nom = str(input('Digite o seu nome completo: ')).upper().strip()

# Divide o nome completo em partes
nome = nom.split()

# Imprime o primeiro nome
print(f'Primeiro nome: {nome[0]}')

# Imprime o último nome
print(f'Último nome: {nome[-1]}')
