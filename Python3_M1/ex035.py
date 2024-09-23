from time import sleep
print('-=-'*20)
print('Analizador de Triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Terceiro segmento '))
print('PRFOCESSANDO...') 
sleep(1)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR TRIANGULOS')
else:
    print('Os seguimentos acima NÂO PODEM FORMAR TRIANGULOS')