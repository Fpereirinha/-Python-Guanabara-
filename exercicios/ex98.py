from time import sleep


def contagem(x, y, z):
    '''print(f'Contagem de 1 até 10 de 1 em 1.')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(.2)
    print(f'\nContagem de 10 até 0 de 2 em 2.')
    for c in range(10, -1, -2):
        print(c, end=' ')
        sleep(.2)
    print(f'\nAgora é sua vez de contar !')
    x = int(input('Inicio: '))
    y = int(input('Fim: '))
    z = int(input('Passo'))'''
    print(f'Contagem de {x} até {y}, com passo de {z}')
    if x < y:
        if z < 0:
            z = -z
    if y < 0:
        y -= 1
        if z > 0:
            z = -z
    else:
        y += 1

    for c in range(x, y, z):
        print(c, end=' ')
        sleep(.5)
    print()

contagem(-10, 10, -4)
contagem(100, -10, 2)

