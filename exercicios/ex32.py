from time import sleep
from datetime import date
n = int(input('Que ano deseja calcular se é bissexto ?'))
if n == 0:
    n = date.today().year
print('=--='*100)
print('Estou calculando, um momento')
print('=-=-'*100)
sleep(2)
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano é bissexto.')
else:
    print('O ano não pe bissexto.')
