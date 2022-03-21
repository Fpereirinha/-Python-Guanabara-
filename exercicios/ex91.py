from random import randint
from operator import itemgetter
from time import sleep
'''cont = 0
jogos = {'1': randint(0, 6), '2': randint(0, 6), '3': randint(0, 6), '4': randint(0, 6)}
for key, value in jogos.items():
    print(f'O jogador {key} tirou {value}.')
    sleep(.5)
for key, value in sorted(jogos.items(),key=itemgetter(1), reverse= True):
    cont += 1
    print(f'O jogador {key} tirou {value} e ficou em {cont}° lugar')
    sleep(.5)'''
from random import randint
from time import sleep
resutados = dict()
jogadores = list()
print('Valores sorteados:')
for c in range(0, 4):
    n = randint(1, 6)
    resutados['Jogador'+str(c+1)] = n
    jogadores.append(n)
    sleep(0.5)
    print(f'O {"Jogador"+str(c+1)} tirou {n}')
jogadores.sort(reverse= True)
jogar = 't'
print('Ranking dos jogadores:')
for p in range(0,4):
    print(f'{p+1}º Lugar: ', end='')
    for k, v in resutados.items():
        if v == jogadores[p] and jogar != k:
            sleep(0.1)
            print(k,'com',v)
            jogar = k
            break