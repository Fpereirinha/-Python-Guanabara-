from random import randint
from operator import itemgetter
from time import sleep
cont = 0
jogos = {'1': randint(0, 6), '2': randint(0, 6), '3': randint(0, 6), '4': randint(0, 6)}
for key, value in jogos.items():
    print(f'O jogador {key} tirou {value}.')
    sleep(.5)
for key, value in sorted(jogos.items(),key=itemgetter(1), reverse= True):
    cont += 1
    print(f'O jogador {key} tirou {value} e ficou em {cont}° lugar')
    sleep(.5)