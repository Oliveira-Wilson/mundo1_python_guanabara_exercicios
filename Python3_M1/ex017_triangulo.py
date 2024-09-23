from math import hypot
co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('qual a medida do cateto adjacente?' ))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print(f' A hipotenusa e igual á {hi:.2f}')
hi = hypot(co, ca)
print(f'Á hipotenusa vai medir {hi:.2f} ')