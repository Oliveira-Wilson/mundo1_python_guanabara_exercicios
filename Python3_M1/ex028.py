from random import randint # rand int (randomiza um n inteiro)
from time import sleep     # O sleep faz o computador 'AGUARDAR um tempo/Pocessar/dormir'
computador = randint(0, 5) # faz o computador "PENSAR" 
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Digite um número de 0, a 5. ')) # JOGADOR tenta adivinhar

print('POCESSANDO...') 
sleep(3)

if jogador == computador: 
    print(f'Parabenś voce me  Venceu')
else:
    print(f'Tente novamente,Voce perdeu!, o numero sorteado foi {computador}  ')