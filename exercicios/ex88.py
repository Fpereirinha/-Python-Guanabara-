from random import randint
'''x = int(input('Quantos jogos quer que eu sorteie ?'))
geral = []
for c in range(x):
    geral.append([])
    for d in range(6):
        x = randint(0, 60)
        while x in geral[c]:
            x = randint(0, 60)
        geral[c].append(x)
for njogo, jogo in enumerate(geral):
    print(f'O {njogo+1}° é {sorted(jogo)}')'''
x = int(input('Quantos jogos quer fazer ?'))
for d in range(x):
    jogo = []
    for c in range(6):
        x = randint(0, 60)
        while x in jogo:
            x = randint(0, 60)
        jogo.append(x)
    print(f'O {d+1}° jogo é {sorted(jogo)}')
