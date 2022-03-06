from math import hypot
n1 = float(input('Qual o comprimento do cateto oposto?'))
n2 = float(input('Qual o comorimento do cateto adjascente?'))
print('O comprimento da hipotenusa é {:.2f}'.format(hypot(n1, n2)))
