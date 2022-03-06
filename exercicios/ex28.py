from random import randint
import time
n = randint(0,5)
r = int(input('Em que número eu pensei ?'))
print('-=-' * 20)
print('Estou processando o número...')
time.sleep(3)
if r == n:
    print('Você acertou !!')
else:
    print('Errou !')
print('O numero é {}'.format(n))