import math
angulo = float(input('Digite o angulo que voce deseja '))
seno = math.sin(math.radians(angulo))
print(f'O seno de {angulo} graus é: {seno:.2f} ')
cosseno = math.cos(math.radians(angulo))
print(f'O cosseno de {angulo} graus é: {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'A tangente de {angulo} graus é: {tangente:.2f}')
